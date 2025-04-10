import json
from xml.etree import ElementTree
from retrieve_data import retrieve_play_data_from_bgg
from extract_data import find_the_marvel_champion_plays
from analyze_data import Statistics

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

def read_data(marvel_plays=None):
    #if marvel_plays is None:
    #    with open("marvel_play_data.json") as play_data:
    #        marvel_plays = json.load(play_data)

    statistics = Statistics(marvel_plays)
    statistics.analyze_play_data()
    return statistics
