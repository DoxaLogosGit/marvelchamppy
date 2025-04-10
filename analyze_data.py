from config import hero_config_data, villain_config_data, Traits, expansions, aspects
import sys
import json
from sortedcontainers import SortedSet

#load up traits from config file
HeroTraits = Traits["Hero_Traits"]
TeamTraits = Traits["Team_Traits"]
BigBoxes = expansions["bigbox"]
ScenarioPacks = expansions["scenario_packs"]
CoreSet = ["Core Set"]

HERO_DATA_SET = SortedSet(hero_config_data.keys())
VILLAIN_DATA_SET = SortedSet(villain_config_data.keys())

def find_diff_data(play_data_new, play_data_old):


    new_size = len(play_data_new)
    old_size = len(play_data_old)

    print(f"New games: {new_size - old_size}")
    if(new_size == old_size):
        return ([],[])
    elif(new_size < old_size):
        return (-1, -1)
    else:
        delta_data = play_data_new[(new_size-old_size)*-1 :]
    #get villains
    villains = [x["Villain"] for x in delta_data]

    #get heroes
    heroes = []
    for play in delta_data:
        for hero in play["Heroes"]:
            heroes.append(hero["Hero"])

    return (set(villains), set(heroes))

class PlayData:
    
    def __init__(self):
        self.plays = 0
        self.wins = 0
        self.win_percentage = 0

class PlaySpecificStats:

    def __init__(self, name):
        self.name = name
        self.total_plays = 0
        #this is used to filter out characters who only had 1 or 2 plays
        self.minimum_play_percentage = 0.02
        self.heroes = []
        self.villains = []
        self.teams = []

    def set_total_plays(self, plays):
        self.total_plays = plays
        
    def set_percent(self, percent):
        self.minimum_play_percentage = percent
        
    def add_villain(self, name, plays, win_percentage):
        if(plays >= round(self.total_plays * self.minimum_play_percentage)):
           #minimum criteria met so add them
           self.villains.append({"name":name, "plays":plays, "percent":win_percentage})

    def add_hero(self, name, plays, win_percentage):
        if(plays >= round(self.total_plays * self.minimum_play_percentage)):
           #minimum criteria met so add them
           self.heroes.append({"name":name, "plays":plays, "percent":win_percentage})

    def add_team(self, name, plays, win_percentage):
        if(plays >= round(self.total_plays * self.minimum_play_percentage)):
           #minimum criteria met so add them
           self.teams.append({"name":name, "plays":plays, "percent":win_percentage})

    def check_percent(self, entry):
           return entry["percent"]
           
    def check_plays(self, entry):
           return entry["plays"]

    def get_best_x_heroes(self, num):
           self.heroes.sort(reverse=True, key=self.check_percent)
           return self.heroes[:num]

    def get_worst_x_heroes(self, num):
           self.heroes.sort(key=self.check_percent)
           return self.heroes[:num]

    def get_best_x_villains(self, num):
           self.villains.sort(key=self.check_percent)
           return self.villains[:num]

    def get_worst_x_villains(self, num):
           self.villains.sort(reverse=True, key=self.check_percent)
           return self.villains[:num]

    def get_best_x_teams(self, num):
           self.teams.sort(reverse=True, key=self.check_percent)
           return self.teams[:num]

    def get_worst_x_teams(self, num):
           self.teams.sort(key=self.check_percent)
           return self.teams[:num]

    def get_most_x_teams(self, num):
           self.teams.sort(reverse=True, key=self.check_plays)
           return self.teams[:num]

    def get_most_x_heroes(self, num):
           self.heroes.sort(reverse=True, key=self.check_plays)
           return self.heroes[:num]

    def get_most_x_villains(self, num):
           self.villains.sort(reverse=True, key=self.check_plays)
           return self.villains[:num]

class AspectData:
    def __init__(self):
        self.aspect_plays = { x:PlayData() for x in aspects}

    def add_play(self, play, this_was_a_win):
        if play["Hero"] == "Adam Warlock":
            if "basic" in play["Aspect"].lower():
                self.aspect_plays["Basic"].plays +=1
                self.aspect_plays["Basic"].wins += this_was_a_win
            else:
                self.aspect_plays["Justice"].plays +=1
                self.aspect_plays["Justice"].wins += this_was_a_win
                self.aspect_plays["Leadership"].plays +=1
                self.aspect_plays["Leadership"].wins += this_was_a_win
                self.aspect_plays["Protection"].plays +=1
                self.aspect_plays["Protection"].wins += this_was_a_win
                self.aspect_plays["Aggression"].plays +=1
                self.aspect_plays["Aggression"].wins += this_was_a_win
        elif play["Hero"] == "Spider Woman":
            if "justice" in play["Aspect"].lower():
                self.aspect_plays["Justice"].plays +=1
                self.aspect_plays["Justice"].wins += this_was_a_win
            if "aggression" in play["Aspect"].lower():
                self.aspect_plays["Aggression"].plays +=1
                self.aspect_plays["Aggression"].wins += this_was_a_win
            if "leadership" in play["Aspect"].lower():
                self.aspect_plays["Leadership"].plays +=1
                self.aspect_plays["Leadership"].wins += this_was_a_win
            if "protection" in play["Aspect"].lower():
                self.aspect_plays["Protection"].plays +=1
                self.aspect_plays["Protection"].wins += this_was_a_win
            if "basic" in play["Aspect"].lower():
                self.aspect_plays["Basic"].plays +=1
                self.aspect_plays["Basic"].wins += this_was_a_win
        else:
            self.aspect_plays[play["Aspect"].strip()].plays +=1
            self.aspect_plays[play["Aspect"].strip()].wins += this_was_a_win

    def calculate_percentages(self):
        for aspect in self.aspect_plays.keys():
            if(self.aspect_plays[aspect].plays > 0):
                self.aspect_plays[aspect].win_percentage = self.aspect_plays[aspect].wins / self.aspect_plays[aspect].plays




class HeroBase:
    def __init__(self, name):
        self.name = name
        self.total_plays = 0
        self.total_wins = 0
        self.aspect_data = AspectData()
        self.difficulty_data = DifficultyStats()
        self.win_percentage = 0
        self.villains_played = SortedSet()
        self.villains_defeated = SortedSet()
        self.villains_not_defeated = SortedSet()
        self.villains_not_played = VILLAIN_DATA_SET

    def add_play(self, hero, full_play):
        """
        Assumes the caller has matched up the hero
        """
        self.total_plays += 1
        this_was_a_win = hero["Win"]
        self.total_wins += this_was_a_win
        self.aspect_data.add_play(hero, this_was_a_win)
        self.difficulty_data.add_play(full_play, this_was_a_win)
        self.villains_played.add(full_play["Villain"])
        if this_was_a_win:
            self.villains_defeated.add(full_play["Villain"])
        self.villains_not_played = VILLAIN_DATA_SET.difference(self.villains_played)
        self.villains_not_defeated = self.villains_played.difference(self.villains_defeated)

    def calculate_percentages(self):
        if self.total_plays:
            self.win_percentage = self.total_wins/self.total_plays
        self.aspect_data.calculate_percentages()
        self.difficulty_data.calculate_percentages()
        
class HeroData(HeroBase):
    def __init__(self, hero, traits="Avenger"):
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
        self.expert5_plays = 0
        self.expert5_wins = 0
        self.expert5_win_percentage = 0
        self.expert6_plays = 0
        self.expert6_wins = 0
        self.expert6_win_percentage = 0
        self.standard1_plays = 0
        self.standard1_wins = 0
        self.standard1_win_percentage = 0
        self.standard2_plays = 0
        self.standard2_wins = 0
        self.standard2_win_percentage = 0
        self.standard3_plays = 0
        self.standard3_wins = 0
        self.standard3_win_percentage = 0
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
        elif play["Difficulty"] == "S3E1":
            self.expert5_plays += 1
            self.expert5_wins += this_was_a_win
        elif play["Difficulty"] == "S3E2":
            self.expert6_plays += 1
            self.expert6_wins += this_was_a_win
        elif play["Difficulty"] == "S1E2":
            self.expert2_plays += 1
            self.expert2_wins += this_was_a_win
        elif play["Difficulty"] == "S1E1":
            self.expert1_plays += 1
            self.expert1_wins += this_was_a_win
        elif play["Difficulty"] == "S3":
            self.standard3_plays += 1
            self.standard3_wins += this_was_a_win
        elif play["Difficulty"] == "S2":
            self.standard2_plays += 1
            self.standard2_wins += this_was_a_win
        elif play["Difficulty"] == "S1":
            self.standard1_plays += 1
            self.standard1_wins += this_was_a_win
        elif play["Difficulty"] == "Heroic":
            self.heroic_plays += 1
            self.heroic_wins += this_was_a_win

    def calculate_percentages(self):
        if self.expert1_plays:
            self.expert1_win_percentage = self.expert1_wins/self.expert1_plays
        if self.expert2_plays:
            self.expert2_win_percentage = self.expert2_wins/self.expert2_plays
        if self.expert3_plays:
            self.expert3_win_percentage = self.expert3_wins/self.expert3_plays
        if self.expert4_plays:
            self.expert4_win_percentage = self.expert4_wins/self.expert4_plays
        if self.expert5_plays:
            self.expert5_win_percentage = self.expert5_wins/self.expert5_plays
        if self.expert6_plays:
            self.expert6_win_percentage = self.expert6_wins/self.expert6_plays
        if self.standard1_plays:
            self.standard1_win_percentage = self.standard1_wins/self.standard1_plays
        if self.standard2_plays:
            self.standard2_win_percentage = self.standard2_wins/self.standard2_plays
        if self.standard3_plays:
            self.standard3_win_percentage = self.standard3_wins/self.standard3_plays
        if self.heroic_plays:
            self.heroic_win_percentage = self.heroic_wins/self.heroic_plays


class VillainBase:
    def __init__(self, name):
        self.name = name
        self.total_plays = 0
        self.total_wins = 0
        self.win_percentage = 0
        self.difficulty_data = DifficultyStats()
        self.aspect_data = AspectData()
        self.heroes_played = SortedSet()
        self.heroes_not_played = HERO_DATA_SET

    def add_play(self, play):
        self.total_plays += 1
        this_was_a_win = play["Heroes"][0]["Win"]
        self.total_wins += this_was_a_win
        self.difficulty_data.add_play(play, this_was_a_win)
        for hero_play in play["Heroes"]:
            self.aspect_data.add_play(hero_play, this_was_a_win)
            self.heroes_played.add(hero_play["Hero"])
            self.heroes_not_played = HERO_DATA_SET.difference(self.heroes_played)


    def calculate_percentages(self):
        if self.total_plays:
            self.win_percentage = self.total_wins/self.total_plays
        self.difficulty_data.calculate_percentages()
        self.aspect_data.calculate_percentages()

class VillainData(VillainBase):
    def __init__(self, name, expansion="Core Set"):
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
        self.overall = PlayData()
        self.overall.plays = len(all_plays)
        self.overall_solo_plays = 0
        self.overall_true_solo_plays = 0
        self.overall_multi_plays = 0
        self.aspect_data = AspectData()
        self.difficulty_data = DifficultyStats()
        self.overall_specific_stats = PlaySpecificStats("Overall")
        self.hero_h_index = 0
        self.villain_h_index = 0

    def calculate_percentages(self):
        if self.overall.plays:
            self.overall.win_percentage = self.overall.wins/self.overall.plays
        self.difficulty_data.calculate_percentages()
        self.aspect_data.calculate_percentages()
        return None



    def analyze_overall_data(self):
        """
        Main function to analyze the overall data
        """
        self.overall_specific_stats.set_total_plays(self.overall.plays)
        self.overall_specific_stats.set_percent(0.01)
        for play in self.all_plays:
            this_was_a_win = play["Heroes"][0]["Win"]
            self.overall.wins += this_was_a_win

            if play["Multiplayer"] == True:
                self.overall_multi_plays += 1
            elif play["True_Solo"] == True:
                self.overall_true_solo_plays += 1
            else:
                self.overall_solo_plays += 1

            self.difficulty_data.add_play(play, this_was_a_win)
            for hero in play["Heroes"]:
                self.aspect_data.add_play(hero, this_was_a_win)


        self.calculate_percentages()


class Statistics:
    def __init__(self, all_plays=None, bgg_format=True):
        if all_plays is None:
            all_plays = self.load_play_data()
        self.all_plays = all_plays
        self.overall_data = OverallData(all_plays)
        self.hero_data = {x:HeroData(x, hero_config_data[x]["traits"]) for x in hero_config_data.keys()}
        self.villain_data = {x:VillainData(x, villain_config_data[x]['expansion']) for x in villain_config_data.keys()}
        self.villain_h_index = 0
        self.hero_h_index = 0
        self.aspect_specific_data = {x:PlaySpecificStats(x) for x in aspects}
        self.bgg_format=bgg_format
        self.sorted_team_list = []
        self.sorted_heroes = None
        self.sorted_percent_heroes = None
        self.sorted_villains = None
        self.sorted_percent_villains = None
        self.team_data = {x:TeamData(x) for  x in TeamTraits}
        self.big_box_data = {x:ExpansionData(x) for  x in BigBoxes}
        self.core_set_data = {x:ExpansionData(x) for  x in CoreSet}
        self.scenario_pack_data = {x:ExpansionData(x) for  x in ScenarioPacks}
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

    def load_play_data(self):
        with open('marvel_play_data.json', 'r') as file:
            return json.load(file)

    def analyze_hero_data(self):
        for play in self.all_plays:
            for hero in play["Heroes"]:
                self.hero_data[hero["Hero"]].add_play(hero, play)

        for hero in self.hero_data:
            self.hero_data[hero].calculate_percentages()
            self.overall_data.overall_specific_stats.add_hero(hero,
                                                        self.hero_data[hero].total_plays,
                                                        self.hero_data[hero].win_percentage)
            for aspect in self.aspect_specific_data:
                self.aspect_specific_data[aspect].add_hero(hero,
                                                            self.hero_data[hero].aspect_data.aspect_plays[aspect].plays,
                                                            self.hero_data[hero].aspect_data.aspect_plays[aspect].win_percentage)

        for team in self.team_data:
            self.team_data[team].calculate_percentages()
            self.overall_data.overall_specific_stats.add_team(team,
                                                        self.team_data[team].total_plays,
                                                        self.team_data[team].win_percentage)
            for aspect in self.aspect_specific_data:
                self.aspect_specific_data[aspect].add_team(team,
                                                            self.team_data[team].aspect_data.aspect_plays[aspect].plays,
                                                            self.team_data[team].aspect_data.aspect_plays[aspect].win_percentage)
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
            self.villain_data[villain].calculate_percentages()
            self.overall_data.overall_specific_stats.add_villain(villain,
                                                        self.villain_data[villain].total_plays,
                                                        self.villain_data[villain].win_percentage)
            for aspect in self.aspect_specific_data:
                self.aspect_specific_data[aspect].add_villain(villain,
                                                            self.villain_data[villain].aspect_data.aspect_plays[aspect].plays,
                                                            self.villain_data[villain].aspect_data.aspect_plays[aspect].win_percentage)

        for big_box in self.big_box_data:
            self.big_box_data[big_box].calculate_percentages()

        for scenario_pack in self.scenario_pack_data:
            self.scenario_pack_data[scenario_pack].calculate_percentages()


    def calculate_h_indices(self):
        self.sorted_heroes = sorted(self.hero_data.items(), key=lambda x: x[1].total_plays, reverse=True)
        self.sorted_percent_heroes = sorted(self.hero_data.items(), key=lambda x: x[1].win_percentage, reverse=True)
        for i, h in enumerate(self.sorted_heroes):
            if self.hero_h_index < h[1].total_plays :
                self.hero_h_index += 1
        self.overall_data.hero_h_index = self.hero_h_index

        self.sorted_villains = sorted(self.villain_data.items(), key=lambda x: x[1].total_plays, reverse=True)
        self.sorted_percent_villains = sorted(self.villain_data.items(), key=lambda x: x[1].win_percentage, reverse=True)
        for i, h in enumerate(self.sorted_villains):
            if self.villain_h_index < h[1].total_plays :
                self.villain_h_index += 1

        self.overall_data.villain_h_index = self.villain_h_index
        return None





    def analyze_play_data(self):
        self.overall_data.analyze_overall_data()

        #get the total plays for each aspect
        for aspect in self.aspect_specific_data.keys():
            self.aspect_specific_data[aspect].set_total_plays(self.overall_data.aspect_data.aspect_plays[aspect].plays)

        self.analyze_hero_data()
        self.analyze_villain_data()
        self.generate_team_plays()
        self.calculate_h_indices()
