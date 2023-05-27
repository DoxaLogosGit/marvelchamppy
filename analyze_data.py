from config import hero_config_data, villain_config_data, Traits, expansions
import sys

#load up traits from config file
HeroTraits = Traits["Hero_Traits"]
TeamTraits = Traits["Team_Traits"]
BigBoxes = expansions["bigbox"]
ScenarioPacks = expansions["scenario_packs"]
CoreSet = ["Core Set"]

def find_diff_data(play_data_new, play_data_old):


    new_size = len(play_data_new)
    old_size = len(play_data_old)

    if(new_size == old_size):
        return ([],[])
    elif(new_size < old_size):
        return (-1, -1)
    else:
        delta_data = play_data_new[:new_size-old_size]
    #get villains
    villains = [x["Villain"] for x in delta_data]
    
    #get heroes
    heroes = []
    for play in delta_data:
        for hero in play["Heroes"]:
            heroes.append(hero["Hero"])

    return (set(villains), set(heroes))

class AspectData:
    def __init__(self):
        self.leadership_plays = 0
        self.leadership_wins = 0
        self.leadership_win_percentage = 0
        self.justice_plays = 0
        self.justice_wins = 0
        self.justice_win_percentage = 0
        self.protection_plays = 0
        self.protection_wins = 0
        self.protection_win_percentage = 0
        self.aggression_plays = 0
        self.aggression_wins = 0
        self.aggression_win_percentage = 0
        self.basic_plays = 0
        self.basic_wins = 0
        self.basic_win_percentage = 0
        self.bgg_format = True

    def add_play(self, play, this_was_a_win, hero):
        if hero == "Adam Warlock":
            if "basic" in play["Aspect"].lower():
                self.basic_plays +=1
                self.basic_wins += this_was_a_win
            else:
                self.justice_plays += 1
                self.justice_wins += this_was_a_win
                self.protection_wins += this_was_a_win
                self.aggression_plays += 1
                self.aggression_wins += this_was_a_win
                self.leadership_plays += 1
                self.leadership_wins += this_was_a_win
        else:
            if "justice" in play["Aspect"].lower():
                self.justice_plays += 1
                self.justice_wins += this_was_a_win
            if "protection" in play["Aspect"].lower():
                self.protection_plays += 1
                self.protection_wins += this_was_a_win
            if "aggression" in play["Aspect"].lower():
                self.aggression_plays += 1
                self.aggression_wins += this_was_a_win
            if "leadership" in play["Aspect"].lower():
                self.leadership_plays += 1
                self.leadership_wins += this_was_a_win
            if "basic" in play["Aspect"].lower():
                self.basic_plays += 1
                self.basic_wins += this_was_a_win

    def calculate_percentages(self, bgg_format=True):
        self.bgg_format = bgg_format
        if self.leadership_plays:
            self.leadership_win_percentage = self.leadership_wins/self.leadership_plays
        if self.justice_plays:
            self.justice_win_percentage = self.justice_wins/self.justice_plays
        if self.protection_plays:
            self.protection_win_percentage = self.protection_wins/self.protection_plays
        if self.basic_plays:
            self.basic_win_percentage = self.basic_wins/self.basic_plays
        if self.aggression_plays:
            self.aggression_win_percentage = self.aggression_wins/self.aggression_plays

    def smarter_string(self):
        smart_string = "\n[b]Aspect Data:[/b]"
        if(self.leadership_plays > 0):
            if self.bgg_format:
                smart_string += f"\n[b][COLOR=#00CCCC]Leadership Plays: {self.leadership_plays}"
            else:
                smart_string += f"\nLeadership Plays: {self.leadership_plays}"
            smart_string += f"\nLeadership Wins: {self.leadership_wins}"
            smart_string += f"\nLeadership Win %: {self.leadership_win_percentage:.1%}"
            if self.bgg_format:
                smart_string += f"[/COLOR][/b]"
            else:
                smart_string += f""

        if(self.aggression_plays > 0):
            if self.bgg_format:
                smart_string += f"\n[b][COLOR=#FF0000]Aggression Plays: {self.aggression_plays}"
            else:
                smart_string += f"\nAggression Plays: {self.aggression_plays}"
            smart_string += f"\nAggression Wins: {self.aggression_wins}"
            smart_string += f"\nAggression Win %: {self.aggression_win_percentage:.1%}"
            if self.bgg_format:
                smart_string += f"[/COLOR][/b]"
            else:
                smart_string += f""
        if(self.justice_plays > 0):
            if self.bgg_format:
                smart_string += f"\n[b][BGCOLOR=#003399][COLOR=#FFFF00]Justice Plays: {self.justice_plays}"
            else:
                smart_string += f"\nJustice Plays: {self.justice_plays}"
            smart_string += f"\nJustice Wins: {self.justice_wins}"
            smart_string += f"\nJustice Win %: {self.justice_win_percentage:.1%}"
            if self.bgg_format:
                smart_string += f"[/COLOR][/BGCOLOR][/b]"
            else:
                smart_string += f""
        if(self.protection_plays > 0):
            if self.bgg_format:
                smart_string += f"\n[b][COLOR=#00FF33]Protection Plays: {self.protection_plays}"
            else:
                smart_string += f"\nProtection Plays: {self.protection_plays}"
            smart_string += f"\nProtection Wins: {self.protection_wins}"
            smart_string += f"\nProtection Win %: {self.protection_win_percentage:.1%}"
            if self.bgg_format:
                smart_string += f"[/COLOR][/b]"
            else:
                smart_string += f""
        if(self.basic_plays > 0):
            if self.bgg_format:
                smart_string += f"\n[b][COLOR=#808080]All Basic Plays: {self.basic_plays}"
            else:
                smart_string += f"\nAll Basic Plays: {self.basic_plays}"
            smart_string += f"\nAll Basic Wins: {self.basic_wins}"
            smart_string += f"\nAll Basic Win %: {self.basic_win_percentage:.1%}"
            if self.bgg_format:
                smart_string += f"[/COLOR][/b]"
            else:
                smart_string += f""
        return smart_string

    def __repr__(self):
        return (self.smarter_string())


class HeroBase:
    def __init__(self, name):
        self.name = name
        self.total_plays = 0
        self.total_wins = 0
        self.aspect_data = AspectData()
        self.difficulty_data = DifficultyStats()
        self.win_percentage = 0
        self.villains_played = set()
        self.villains_defeated = set()
        self.villains_not_played = set()

    def add_play(self, hero, full_play):
        """
        Assumes the caller has matched up the hero
        """
        self.total_plays += 1
        this_was_a_win = hero["Win"]
        self.total_wins += this_was_a_win
        self.aspect_data.add_play(hero, this_was_a_win, self.name)
        self.difficulty_data.add_play(full_play, this_was_a_win)
        self.villains_played.add(full_play["Villain"])
        if this_was_a_win:
            self.villains_defeated.add(full_play["Villain"])
        self.villains_not_played = VILLAIN_DATA_SET.difference(self.villains_played)


    def smarter_string(self):
        smart_string = ("[b]Overall Data[/b]" +
                        f"\nTotal Plays: {self.total_plays}" +
                        f"\nTotal Wins: {self.total_wins}" +
                        f"\nTotal Win  %: {self.win_percentage:.1%}" +
                        "\n[b]Difficulty Data:[/b]")
        smart_string += self.difficulty_data.smarter_string()
        smart_string += self.aspect_data.smarter_string()
        smart_string += (f"\nVillains Unplayed: {len(self.villains_not_played)}\n {str(self.villains_not_played)}")
        return smart_string

    def __repr__(self):
        return (self.smarter_string())


    def calculate_percentages(self, bgg_format=True):
        if self.total_plays:
            self.win_percentage = self.total_wins/self.total_plays
        self.aspect_data.calculate_percentages(bgg_format)
        self.difficulty_data.calculate_percentages(bgg_format)
        
class HeroData(HeroBase):
    def __init__(self, hero, traits):
        super().__init__(hero)
        self.traits = traits
        self.team = []

    def add_play(self, hero, full_play):
        """
        Assumes the caller has matched up the hero
        """
        super().add_play(hero, full_play)
        for team in self.team:
            team.add_play(hero,full_play)

    def add_team(self, team):
        self.team.append(team)


class TeamData(HeroBase):
    def __init__(self, team):
        super().__init__(team)


class DifficultyStats:
    def __init__(self):
        self.expert1_plays = 0
        self.expert1_wins = 0
        self.expert1_win_percentage = 0
        self.expert2_plays = 0
        self.expert2_wins = 0
        self.expert2_win_percentage = 0
        self.expert3_plays = 0
        self.expert3_wins = 0
        self.expert3_win_percentage = 0
        self.expert4_plays = 0
        self.expert4_wins = 0
        self.expert4_win_percentage = 0
        self.standard1_plays = 0
        self.standard1_wins = 0
        self.standard1_win_percentage = 0
        self.standard2_plays = 0
        self.standard2_wins = 0
        self.standard2_win_percentage = 0
        self.heroic_plays = 0
        self.heroic_wins = 0
        self.heroic_win_percentage = 0

    def add_play(self, play, this_was_a_win):
        if play["Difficulty"] == "S2E2":
            self.expert4_plays += 1
            self.expert4_wins += this_was_a_win
        elif play["Difficulty"] == "S2E1":
            self.expert3_plays += 1
            self.expert3_wins += this_was_a_win
        elif play["Difficulty"] == "S1E2":
            self.expert2_plays += 1
            self.expert2_wins += this_was_a_win
        elif play["Difficulty"] == "S1E1":
            self.expert1_plays += 1
            self.expert1_wins += this_was_a_win
        elif play["Difficulty"] == "S2":
            self.standard2_plays += 1
            self.standard2_wins += this_was_a_win
        elif play["Difficulty"] == "S1":
            self.standard1_plays += 1
            self.standard1_wins += this_was_a_win
        elif play["Difficulty"] == "Heroic":
            self.heroic_plays += 1
            self.heroic_wins += this_was_a_win

    def calculate_percentages(self, bgg_format=True):
        self.bgg_format = bgg_format
        if self.expert1_plays:
            self.expert1_win_percentage = self.expert1_wins/self.expert1_plays
        if self.expert2_plays:
            self.expert2_win_percentage = self.expert2_wins/self.expert2_plays
        if self.expert3_plays:
            self.expert3_win_percentage = self.expert3_wins/self.expert3_plays
        if self.expert4_plays:
            self.expert4_win_percentage = self.expert4_wins/self.expert4_plays
        if self.standard1_plays:
            self.standard1_win_percentage = self.standard1_wins/self.standard1_plays
        if self.standard2_plays:
            self.standard2_win_percentage = self.standard2_wins/self.standard2_plays
        if self.heroic_plays:
            self.heroic_win_percentage = self.heroic_wins/self.heroic_plays

    def smarter_string(self):
        smart_string = ""
        if(self.expert1_plays > 0):
            smart_string += f"\nS1E1 Plays: {self.expert1_plays}"
            smart_string += f"\nS1E1 Wins: {self.expert1_wins}"
            smart_string += f"\nS1E1 Wins %: {self.expert1_win_percentage:.1%}"
        if(self.expert2_plays > 0):
            smart_string += f"\nS1E2 Plays: {self.expert2_plays}"
            smart_string += f"\nS1E2 Wins: {self.expert2_wins}"
            smart_string += f"\nS1E2 Wins %: {self.expert2_win_percentage:.1%}"
        if(self.expert3_plays > 0):
            smart_string += f"\nS2E1 Plays: {self.expert3_plays}"
            smart_string += f"\nS2E1 Wins: {self.expert3_wins}"
            smart_string += f"\nS2E1 Wins %: {self.expert3_win_percentage:.1%}"
        if(self.expert4_plays > 0):
            smart_string += f"\nS2E2 Plays: {self.expert4_plays}"
            smart_string += f"\nS2E2 Wins: {self.expert4_wins}"
            smart_string += f"\nS2E2 Wins %: {self.expert4_win_percentage:.1%}"
        if(self.standard1_plays > 0):
            smart_string += f"\nS1 Plays: {self.standard1_plays}"
            smart_string += f"\nS1 Wins: {self.standard1_wins}"
            smart_string += f"\nS1 Wins %: {self.standard1_win_percentage:.1%}"
        if(self.standard2_plays > 0):
            smart_string += f"\nS2 Plays: {self.standard2_plays}"
            smart_string += f"\nS2 Wins: {self.standard2_wins}"
            smart_string += f"\nS2 Wins %: {self.standard2_win_percentage:.1%}"
        if(self.heroic_plays > 0):
            smart_string += f"\nHeroic Plays: {self.heroic_plays}"
            smart_string += f"\nHeroic Wins: {self.heroic_wins}"
            smart_string += f"\nHeroic Wins %: {self.heroic_win_percentage:.1%}"
        return smart_string

    def __repr__(self):
        return (self.smarter_string())

class VillainBase:
    def __init__(self, name):
        self.name = name
        self.total_plays = 0
        self.total_wins = 0
        self.win_percentage = 0
        self.difficulty_data = DifficultyStats()
        self.aspect_data = AspectData()
        self.heroes_played = set()
        self.heroes_not_played = set()

    def add_play(self, play):
        self.total_plays += 1
        this_was_a_win = play["Heroes"][0]["Win"]
        self.total_wins += this_was_a_win
        self.difficulty_data.add_play(play, this_was_a_win)
        for hero_play in play["Heroes"]:
            self.aspect_data.add_play(hero_play, this_was_a_win, hero_play["Hero"])
            self.heroes_played.add(hero_play["Hero"])
            self.heroes_not_played = HERO_DATA_SET.difference(self.heroes_played)

    def __repr__(self):
        return (f"Total Plays: {self.total_plays}" +
        f"\nTotal Wins: {self.total_wins}" +
        f"\nTotal Win  %: {self.win_percentage:.1%}" +
        self.difficulty_data.__repr__() +
        self.aspect_data.__repr__() + 
        f"\nHeroes Unplayed: {len(self.heroes_not_played)}\n{str(self.heroes_not_played)}")

    def calculate_percentages(self, bgg_format=True):
        if self.total_plays:
            self.win_percentage = self.total_wins/self.total_plays
        self.difficulty_data.calculate_percentages(bgg_format)
        self.aspect_data.calculate_percentages(bgg_format)

class VillainData(VillainBase):
    def __init__(self, name, expansion):
        super().__init__(name)
        self.expansion = expansion
        self.expansion_data = None

    def add_expansion(self, expansion_data):
        self.expansion_data = expansion_data
        
    def add_play(self, play):
        super().add_play(play)
        self.expansion_data.add_play(play)


class ExpansionData(VillainBase):
    def __init__(self, name):
        super().__init__(name)


class OverallData:

    def __init__(self, all_plays):
        self.all_plays = all_plays
        self.overall_plays = len(all_plays)
        self.overall_wins = 0
        self.overall_win_percentage = 0
        self.overall_solo_plays = 0
        self.overall_true_solo_plays = 0
        self.overall_multi_plays = 0
        self.aspect_data = AspectData()
        self.difficulty_data = DifficultyStats()

    def calculate_percentages(self, bgg_format=True):
        if self.overall_plays:
            self.overall_win_percentage = self.overall_wins/self.overall_plays
        self.difficulty_data.calculate_percentages(bgg_format)
        self.aspect_data.calculate_percentages(bgg_format)
        return None


    def __repr__(self):
        return ("[b]Overall Data[/b][b]" +
        f"\nTotal Plays: {self.overall_plays}" +
        f"\nTotal Wins: {self.overall_wins}" +
        f"\nTotal Win  %: {self.overall_win_percentage:.1%}" +
        f"\nTotal True Solo Plays: {self.overall_true_solo_plays}" +
        f"\nTotal Multihanded Solo Plays: {self.overall_solo_plays}" +
        f"\nTotal Multiplayer Plays: {self.overall_multi_plays}" +
        "\n[b]Difficulty Data:[/b]" +
        self.difficulty_data.__repr__() +
        self.aspect_data.__repr__())


    def analyze_overall_data(self,bgg_format=True):
        """
        Main function to analyze the overall data
        """
        for play in self.all_plays:
            this_was_a_win = play["Heroes"][0]["Win"]
            self.overall_wins += this_was_a_win

            if play["Multiplayer"] == True:
                self.overall_multi_plays += 1
            elif play["True_Solo"] == True:
                self.overall_true_solo_plays += 1
            else:
                self.overall_solo_plays += 1

            self.difficulty_data.add_play(play, this_was_a_win)
            for hero in play["Heroes"]:
                self.aspect_data.add_play(hero, this_was_a_win, hero["Hero"])


        self.calculate_percentages(bgg_format)


HERO_INIT_DATA = {x:HeroData(x, hero_config_data[x]["traits"]) for x in hero_config_data.keys()}
HERO_DATA_SET = set(HERO_INIT_DATA.keys())
VILLAIN_INIT_DATA = {x:VillainData(x, villain_config_data[x]['expansion']) for x in villain_config_data.keys()}
VILLAIN_DATA_SET = set(VILLAIN_INIT_DATA.keys())
BIG_BOX_INIT_DATA = {x:ExpansionData(x) for  x in BigBoxes}
SCENARIO_PACK_INIT_DATA = {x:ExpansionData(x) for  x in ScenarioPacks}
CORE_SET_INIT_DATA = {x:ExpansionData(x) for  x in CoreSet}
TEAM_INIT_DATA = {x:TeamData(x) for  x in TeamTraits}

class Statistics:
    def __init__(self, all_plays, bgg_format=True):
        self.all_plays = all_plays
        self.overall_data = OverallData(all_plays)
        self.hero_data = HERO_INIT_DATA
        self.villain_data = VILLAIN_INIT_DATA
        self.villain_h_index = 0
        self.hero_h_index = 0
        self.bgg_format=bgg_format
        self.sorted_team_list = []
        self.sorted_heroes = None
        self.sorted_villains = None
        self.team_data = TEAM_INIT_DATA
        self.big_box_data = BIG_BOX_INIT_DATA
        self.core_set_data = CORE_SET_INIT_DATA
        self.scenario_pack_data = SCENARIO_PACK_INIT_DATA
        #setup big boxes in villains
        for villain in self.villain_data.keys():
            expansion_found = False
            for big_box in self.big_box_data.keys():
                if big_box == self.villain_data[villain].expansion:
                    self.villain_data[villain].add_expansion(self.big_box_data[big_box])
                    expansion_found = True
                    break
            if expansion_found == False:
                for scenario_pack in self.scenario_pack_data.keys():
                    if scenario_pack == self.villain_data[villain].expansion:
                        self.villain_data[villain].add_expansion(self.scenario_pack_data[scenario_pack])
                        expansion_found = True
                        break
            if expansion_found == False:
                for core_set in self.core_set_data.keys():
                    if core_set == self.villain_data[villain].expansion:
                        self.villain_data[villain].add_expansion(self.core_set_data[core_set])
                        expansion_found = True
                        break

        #setup the team data in heroes
        for team in self.team_data.keys():
            for hero in self.hero_data.keys():
                if team in self.hero_data[hero].traits:
                    self.hero_data[hero].add_team(self.team_data[team])
                

    def analyze_hero_data(self):
        for play in self.all_plays:
            for hero in play["Heroes"]:
                self.hero_data[hero["Hero"]].add_play(hero, play)

        for hero in self.hero_data:
            self.hero_data[hero].calculate_percentages(self.bgg_format)

        for team in self.team_data:
            self.team_data[team].calculate_percentages(self.bgg_format)

    def generate_team_plays(self):
        team_play_list = [ (x, self.team_data[x].total_plays) for x in self.team_data.keys()]
        self.sorted_team_list = sorted(team_play_list, key=lambda x: x[1], reverse=True)

    def print_team_plays(self):
        plays_tally = "[b]Team Data:[/b]"
        for team, plays in self.sorted_team_list:
            plays_tally = plays_tally + f"\n{team}: {plays}"
        return plays_tally

    def analyze_villain_data(self):
        for play in self.all_plays:
            self.villain_data[play["Villain"]].add_play(play)

        for villain in self.villain_data:
            self.villain_data[villain].calculate_percentages(self.bgg_format)

        for big_box in self.big_box_data:
            self.big_box_data[big_box].calculate_percentages(self.bgg_format)


    def calculate_h_indices(self):
        self.sorted_heroes = sorted(self.hero_data.items(), key=lambda x: x[1].total_plays, reverse=True)
        for i, h in enumerate(self.sorted_heroes):
            if self.hero_h_index < h[1].total_plays :
                self.hero_h_index += 1

        self.sorted_villains = sorted(self.villain_data.items(), key=lambda x: x[1].total_plays, reverse=True)
        for i, h in enumerate(self.sorted_villains):
            if self.villain_h_index < h[1].total_plays :
                self.villain_h_index += 1

        return None

    def __repr__(self):
        repr_string = "===========================================================\n"
        repr_string += self.overall_data.__repr__() + "\n"
        repr_string += "===========================================================\n"
        repr_string += self.print_team_plays() + "\n"
        repr_string += "===========================================================\n"
        repr_string += f"Hero H-Index: {self.hero_h_index}   Villain H-Index: {self.villain_h_index}\n"
        repr_string += "===========================================================\n"
        for i, hero in enumerate(self.sorted_heroes):
            if hero[1].total_plays > 0:
                repr_string += f"{i+1}. " + hero[1].name + "\n"
                repr_string += hero[1].__repr__() + "\n"
                repr_string += "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"
        for j, villain in enumerate(self.sorted_villains):
            if villain[1].total_plays > 0:
                repr_string += f"{j+1}. " + villain[1].name + "\n"
                repr_string += villain[1].__repr__() + "\n"
                repr_string += "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"
        return repr_string




    def analyze_play_data(self, bgg_format=True):
        self.overall_data.analyze_overall_data()
        self.analyze_hero_data()
        self.analyze_villain_data()
        self.generate_team_plays()
        self.calculate_h_indices()
