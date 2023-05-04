from xml.etree import ElementTree
from config import hero_config_data, villain_config_data
MARVEL_CHAMPIONS_ID="285774"


def create_string_replacements(config_data):
    replace_data = {}
    for hero_villain in config_data.keys():
        replace_data[hero_villain.lower()] = hero_villain
        if(config_data[hero_villain]["replacements"][0] is not None):
            for replace in config_data[ hero_villain]["replacements"]:
                replace_data[replace.lower()] = hero_villain
        
    return replace_data
"""
Data to extract:

    Villain:
    Difficulty:
    Heroes: [(Hero, Aspect, Win)] (it's a list because i could play more than one hero solo)
    Date:  this is for debugging

"""

def extract_villain(play_comment):
    replace_check = create_string_replacements(villain_config_data)
    for check in replace_check.keys():
        if(check in play_comment.lower()):
            return replace_check[check]
    return "UNKNOWN"

def which_standard(play_comment):
    if("standard 2" in play_comment.lower() or "standard ii" in play_comment.lower()):
        return "S2"
    return "S1"

def extract_difficulty(play_comment):
    if("s1e1" in play_comment.lower()):
        return "S1E1"
    if("s2e1" in play_comment.lower()):
        return "S2E1"
    if("s2e2" in play_comment.lower()):
        return "S2E2"
    if("s1e2" in play_comment.lower()):
        return "S1E2"
    if("s2" in play_comment.lower()):
        return "S2"
    if("expert" in play_comment.lower()):
        if("expert 2" in play_comment.lower() or "expert ii" in play_comment.lower()):
            return (which_standard(play_comment) + "E2")
        return (which_standard(play_comment) + "E1")
    if("standard" in play_comment.lower()):
        return which_standard(play_comment)
    if("heroic" in play_comment.lower()):
        return "Heroic"
    return "S1"

 
    
    
def clean_up_hero_name(hero_name):
    """
    #This function will fix the hero name with a consistent naming scheme
    """
    hero_name_replace = create_string_replacements(hero_config_data)
    try:
        return hero_name_replace[hero_name]
    except KeyError:
        print("Can't find {} hero".format(hero_name))
        return hero_name




#walk the list of pages and return a list of all the marvel champions play data
#return the list of plays
def extract_marvel_champions_play_data(xml_play_data, user):
    play_data = {}
    play_data["Date"] = xml_play_data.attrib["date"]
    hero_list = []
    player_count = 0
    play_data["Multiplayer"] = False
    play_data["True_Solo"] = False
    for player in xml_play_data.find("players").findall("./player"):
        hero_list.append({"Hero":clean_up_hero_name(player.attrib["startposition"].lower().rstrip().strip()), "Aspect":player.attrib["color"], "Win":int(player.attrib["win"])})
        if player.attrib["username"] == user:
            if player_count == 0:
                play_data["True_Solo"] = True
            else:
                play_data["True_Solo"] = False
        else:
            play_data["Multiplayer"] = True
        player_count +=1

    play_data["Heroes"] = hero_list

    play_comment = xml_play_data.find("comments").text
    play_data["Villain"] = extract_villain(play_comment)
    play_data["Difficulty"] = extract_difficulty(play_comment)

    return play_data



#parse the list of xml data plays and just return the marvel champion data in a list
def find_the_marvel_champion_plays(all_xml_data, user):
    marvel_champion_plays = []
    for page in all_xml_data:
        page_root = ElementTree.fromstring(page)
        for play in page_root.findall("./play"):
            if play.find('item').attrib['objectid'] == MARVEL_CHAMPIONS_ID:
                marvel_champion_plays.append(extract_marvel_champions_play_data(play, user))

    print("Total plays retrieved: {}".format(len(marvel_champion_plays)))
    return marvel_champion_plays


