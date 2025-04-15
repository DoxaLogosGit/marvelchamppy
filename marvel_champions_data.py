#!/usr/bin/python3
#This module is designed to retrieve my marvel champions data from BGG.  Eventually, I plan to make a web app to
#display statistics that like H-index, how many plays, win percenter per hero, per villain etc.

from xml.etree import ElementTree
import simplejson as json
from retrieve_data import retrieve_play_data_from_bgg
from extract_data import find_the_marvel_champion_plays
from analyze_data import Statistics, find_diff_data
from argparse import ArgumentParser
from upload import UploadData
from excel import ExcelData
from os import path
import shutil

USER='DoxaLogos'


def download_data():
    print("Begin collecting data")
    xml_data = retrieve_play_data_from_bgg(USER)
    print("Done collecting data")

    xml_string = "".join(xml_data)
    with open("play_data.xml","w") as xml_play_data:
        xml_play_data.write(xml_string)
    print("Extracting data")
    marvel_plays = find_the_marvel_champion_plays(xml_data, USER)

    with open("marvel_play_data.json","w") as play_data:
        play_data.write(json.dumps(marvel_plays, sort_keys=True, indent=2 * ' '))
    return marvel_plays
    

#main loop function
def main():
    parser = ArgumentParser()

    parser.add_argument("-j", "--analyze-json", action="store_true",
                        help="analyze the default json file only")

    parser.add_argument("-u", "--upload_data", action="store_true",
                        help="upload the data to google spreadsheets")

    parser.add_argument("-s", "--skip_found", action="store_true",
                        help="skip upload on found worksheets")

    parser.add_argument("-n", "--newest_data", action="store_true",
                        help="do an upload of just the newest plays")

    parser.add_argument("-x", "--excel_data", action="store_true",
                        help="write the data to an excel spreadsheet: statistics.xlsx")

    args = parser.parse_args()

    #check for old data
    if(args.newest_data and not args.analyze_json):
        if(path.isfile("marvel_play_data.json")):
            #backup file
            shutil.copyfile("marvel_play_data.json", "marvel_play_data_bak.json")
        else:
            #no recent file to disable newest upload
            args.newest_data=False



    if(not args.analyze_json):
        marvel_plays = download_data()
    else:
        marvel_plays = None
        with open("marvel_play_data.json") as play_data:
             marvel_plays = json.loads(play_data.read())

    #check for old data
    if(args.newest_data):
        with open("marvel_play_data_bak.json") as play_data:
            marvel_plays_bak = json.loads(play_data.read())

        diff_data = find_diff_data(marvel_plays, marvel_plays_bak)
        print(diff_data)
        if(diff_data[0] == -1):
            print("something was deleted, restoring old data")
            marvel_plays = marvel_plays_bak
            diff_data = None
    else:
        diff_data = None

    statistics = Statistics(marvel_plays)
    statistics.analyze_play_data()

    if(args.upload_data):
        data = UploadData(statistics, args.skip_found, diff_data)
        data.perform_upload()

    if(args.excel_data):
        data = ExcelData(statistics, args.skip_found, diff_data)
        data.perform_write()




if __name__ == '__main__':
    main()


