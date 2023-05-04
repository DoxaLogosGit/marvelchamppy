#!/usr/bin/python3
#This module is designed to retrieve my marvel champions data from BGG.  Eventually, I plan to make a web app to
#display statistics that like H-index, how many plays, win percenter per hero, per villain etc.

from xml.etree import ElementTree
import simplejson as json
from retrieve_data import retrieve_play_data_from_bgg
from extract_data import find_the_marvel_champion_plays
from analyze_data import Statistics
from argparse import ArgumentParser

USER='DoxaLogos'
#OLD_USER='jgatkinsn' #old username
START_DATE =  (2019, 11, 6)



#main loop function
def main():
    parser = ArgumentParser()

    parser.add_argument("-j", "--analyze-json", action="store_true",
                        help="analyze the default json file only")

    parser.add_argument("-x", "--extract_data", action="store_true",
                        help="test extraction on xml data")
    args = parser.parse_args()

    if(not args.analyze_json and not args.extract_data):
        print("Begin collecting data")
        xml_data = retrieve_play_data_from_bgg(USER)
        print("Done collecting data")

        with open("play_data.xml","w") as xml_play_data:
            xml_play_data.writelines(xml_data)
        print("Extracting data")
        marvel_plays = find_the_marvel_champion_plays(xml_data, USER)

        with open("marvel_play_data.json","w") as play_data:
            play_data.write(json.dumps(marvel_plays, sort_keys=True, indent=2 * ' '))
    elif(args.extract_data):
        with open("play_data.xml") as xml_play_data:
            xml_data = xml_play_data.read()
        print("Extracting data")
        marvel_plays = find_the_marvel_champion_plays(xml_data, USER)

        with open("marvel_play_data.json","w") as play_data:
            play_data.write(json.dumps(marvel_plays, sort_keys=True, indent=2 * ' '))
    else:
         marvel_plays = None
         with open("marvel_play_data.json") as play_data:
             marvel_plays = json.loads(play_data.read())

    statistics = Statistics(marvel_plays)
    statistics.analyze_play_data()
    print(statistics)




if __name__ == '__main__':
    main()


