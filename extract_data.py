from xml.etree import ElementTree
MARVEL_CHAMPIONS_ID="285774"

"""
Data to extract:

    Villain:
    Difficulty:
    Heroes: [(Hero, Aspect, Win)] (it's a list because i could play more than one hero solo)
    Date:  this is for debugging

"""

def extract_villain(play_comment):
    if("brotherhood of badoon" in play_comment.lower()):
        return "Drang"
    if("ultron" in play_comment.lower()):
        return "Ultron"
    if("absorbing" in play_comment.lower()):
        return "Absorbing Man"
    if("klaw" in play_comment.lower()):
        return "Klaw"
    if("rhino" in play_comment.lower()):
        return "Rhino"
    if("kang" in play_comment.lower()):
        return "Kang"
    if("green goblin" in play_comment.lower()):
        if("risky" in play_comment.lower()):
            return "Green Goblin - Risky Business"
        else:
            return "Green Goblin - Mutagen Formula"
    if("crossbones" in play_comment.lower()):
        return "Crossbones"
    if("taskmaster" in play_comment.lower()):
        return "Taskmaster"
    if("zola" in play_comment.lower()):
        return "Amin Zola"
    if("red skull" in play_comment.lower()):
        return "Red Skull"
    if("nebula" in play_comment.lower()):
        return "Nebula"
    if("drang" in play_comment.lower()):
        return "Drang"
    if("ronan" in play_comment.lower()):
        return "Ronan"
    if("ebony maw" in play_comment.lower()):
        return "Ebony Maw"
    if("thano" in play_comment.lower()):
        return "Thanos"
    if("thanos" in play_comment.lower()):
        return "Thanos"
    if("the hood" in play_comment.lower()):
        return "Hood"
    if("hood" in play_comment.lower()):
        return "Hood"
    if("tower defense" in play_comment.lower()):
        return "Tower Defense"
    if("corvious" in play_comment.lower()):
        return "Tower Defense"
    if("proxima" in play_comment.lower()):
        return "Tower Defense"
    if("loki" in play_comment.lower()):
        return "Loki"
    if("hela" in play_comment.lower()):
        return "Hela"
    if("venom villain" in play_comment.lower()):
        return "Venom"
    if("sinister six" in play_comment.lower()):
        return "Sinister Six"
    if("vengoblin" in play_comment.lower()):
        return "Venom Goblin"
    if("sandman" in play_comment.lower()):
        return "Sandman"
    if("mysterio" in play_comment.lower()):
        return "Mysterio"
    if("collector" in play_comment.lower()):
        if("infiltrate" in play_comment.lower()):
            return "The Collector - Infiltrate the Museum"
        else:
            return "The Collector - Escape the Museum"
    if("wrecking crew" in play_comment.lower()):
        return "Wrecking Crew"
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
    hero_name_replace = {
        "spiderwoman":"Spider Woman",
        "spider woman":"Spider Woman",
        "spider-woman":"Spider Woman",
        "spiderman":"Spider Man",
        "spider man":"Spider Man",
        "spider-man":"Spider Man",
        "ghostspider":"Spider Gwen",
        "ghost spider":"Spider Man",
        "spider gwen":"Spider Gwen",
        "spider-gwen":"Spider Gwen",
        "spidergwen":"Spider Gwen",
        "ant man":"Ant Man",
        "miles morales":"Miles Morales",
        "antman":"Ant Man",
        "scarlet witch":"Scarlet Witch",
        "scarlet-witch":"Scarlet Witch",
        "scarlett witch":"Scarlet Witch",
        "scarlett-witch":"Scarlet Witch",
        "scarlettwitch":"Scarlet Witch",
        "scarletwitch":"Scarlet Witch",
        "iron man":"Iron Man",
        "iron-man":"Iron Man",
        "ironman":"Iron Man",
        "black widow":"Black Widow",
        "black-widow":"Black Widow",
        "blackwidow":"Black Widow",
        "ant man":"Ant Man",
        "ant-man":"Ant Man",
        "antman":"Ant Man",
        "she hulk":"She-Hulk",
        "she-hulk":"She-Hulk",
        "shehulk":"She-Hulk",
        "black panther":"Black Panther",
        "black-panther":"Black Panther",
        "blackpanther":"Black Panther",
        "captain marvel":"Captain Marvel",
        "captain-marvel":"Captain Marvel",
        "captainmarvel":"Captain Marvel",
        "captain america":"Captain America",
        "captain-america":"Captain America",
        "captainamerica":"Captain America",
        "ms. marvel":"Ms. Marvel",
        "ms.marvel":"Ms. Marvel",
        "msmarvel":"Ms. Marvel",
        "ms marvel":"Ms. Marvel",
        "msmarvel":"Ms. Marvel",
        "dr. strange":"Doctor Strange",
        "dr.strange":"Doctor Strange",
        "drstrange":"Doctor Strange",
        "dr strange":"Doctor Strange",
        "doctor strange":"Doctor Strange",
        "doctorstrange":"Doctor Strange",
        "hulk":"Hulk",
        "nova":"Nova",
        "wasp":"Wasp",
        "thor":"Thor",
        "quicksilver":"Quicksilver",
        "hawkeye":"Hawkeye",
        "hawk eye":"Hawkeye",
        "hawk-eye":"Hawkeye",
        "rocket":"Rocket Raccoon",
        "rocket raccoon":"Rocket Raccoon",
        "rocket racoon":"Rocket Raccoon",
        "groot":"Groot",
        "drax":"Drax",
        "gamora":"Gamora",
        "starlord":"Star Lord",
        "star lord":"Star Lord",
        "star-lord":"Star Lord",
        "venom":"Venom",
        "adam warlock":"Adam Warlock",
        "adamwarlock":"Adam Warlock",
        "spectrum":"Spectrum",
        "nebula":"Nebula",
        "war machine":"War Machine",
        "war-machine":"War Machine",
        "warmachine":"War Machine",
        "vision":"Vision",
        "valkyrie":"Valkyrie",
        "miles morales":"Miles Morales",
        "spidergwen":"Spider Gwen",
        "spider gwen":"Spider Gwen",
        "ghost spider":"Spider Gwen",
    }
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


