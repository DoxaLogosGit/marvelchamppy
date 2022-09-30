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
                smart_string += f"\n[b]Leadership Plays: {self.leadership_plays}"
            smart_string += f"\nLeadership Wins: {self.leadership_wins}"
            smart_string += f"\nLeadership Win %: {self.leadership_win_percentage:.1%}"
            if self.bgg_format:
                smart_string += f"[/COLOR][/b]"
            else:
                smart_string += f"[/b]"

        if(self.aggression_plays > 0):
            if self.bgg_format:
                smart_string += f"\n[b][COLOR=#FF0000]Aggression Plays: {self.aggression_plays}"
            else:
                smart_string += f"\n[b]Aggression Plays: {self.aggression_plays}"
            smart_string += f"\nAggression Wins: {self.aggression_wins}"
            smart_string += f"\nAggression Win %: {self.aggression_win_percentage:.1%}"
            if self.bgg_format:
                smart_string += f"[/COLOR][/b]"
            else:
                smart_string += f"[/b]"
        if(self.justice_plays > 0):
            if self.bgg_format:
                smart_string += f"\n[b][BGCOLOR=#003399][COLOR=#FFFF00]Justice Plays: {self.justice_plays}"
            else:
                smart_string += f"\n[b]Justice Plays: {self.justice_plays}"
            smart_string += f"\nJustice Wins: {self.justice_wins}"
            smart_string += f"\nJustice Win %: {self.justice_win_percentage:.1%}"
            if self.bgg_format:
                smart_string += f"[/COLOR][/BGCOLOR][/b]"
            else:
                smart_string += f"[/b]"
        if(self.protection_plays > 0):
            if self.bgg_format:
                smart_string += f"\n[b][COLOR=#00FF33]Protection Plays: {self.protection_plays}"
            else:
                smart_string += f"\n[b]Protection Plays: {self.protection_plays}"
            smart_string += f"\n[b][COLOR=#00FF33]Protection Plays: {self.protection_plays}"
            smart_string += f"\nProtection Wins: {self.protection_wins}"
            smart_string += f"\nProtection Win %: {self.protection_win_percentage:.1%}"
            if self.bgg_format:
                smart_string += f"[/COLOR][/b]"
            else:
                smart_string += f"[/b]"
        if(self.basic_plays > 0):
            if self.bgg_format:
                smart_string += f"\n[b][COLOR=#808080]All Basic Plays: {self.basic_plays}"
            else:
                smart_string += f"\n[b]All Basic Plays: {self.basic_plays}"
            smart_string += f"\nAll Basic Wins: {self.basic_wins}"
            smart_string += f"\nAll Basic Win %: {self.basic_win_percentage:.1%}"
            if self.bgg_format:
                smart_string += f"[/COLOR][/b]"
            else:
                smart_string += f"[/b]"
        return smart_string

    def __repr__(self):
        return (self.smarter_string())

class HeroData:
    def __init__(self, hero):
        self.hero_name = hero
        self.total_plays = 0
        self.total_wins = 0
        self.aspect_data = AspectData()
        self.difficulty_data = DifficultyStats()

    def add_play(self, play):
        """
        Assumes the caller has matched up the hero
        """
        self.total_plays += 1
        this_was_a_win = play["Win"]
        self.total_wins += this_was_a_win
        self.aspect_data.add_play(play, this_was_a_win, self.hero_name)
        #self.difficulty_data.add_play(play, this_was_a_win)


    def smarter_string(self):
        smart_string = ("[b]Overall Data[/b]" +
                        f"\nTotal Plays: {self.total_plays}" +
                        f"\nTotal Wins: {self.total_wins}" +
                        f"\nTotal Win  %: {self.win_percentage:.1%}")
        smart_string += self.aspect_data.smarter_string()
        return smart_string

    def __repr__(self):
        return (self.smarter_string())


    def calculate_percentages(self, bgg_format=True):
        if self.total_plays:
            self.win_percentage = self.total_wins/self.total_plays
        self.aspect_data.calculate_percentages(bgg_format)

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

class VillainData:
    def __init__(self, villain):
        self.villain_name = villain
        self.total_plays = 0
        self.total_wins = 0
        self.win_percentage = 0
        self.difficulty_data = DifficultyStats()
        self.aspect_data = AspectData()

    def add_play(self, play):
        self.total_plays += 1
        this_was_a_win = play["Heroes"][0]["Win"]
        self.total_wins += this_was_a_win
        self.difficulty_data.add_play(play, this_was_a_win)
        #self.aspect_data.add_play(play, this_was_a_win)


    def __repr__(self):
        return (f"Total Plays: {self.total_plays}" +
        f"\nTotal Wins: {self.total_wins}" +
        f"\nTotal Win  %: {self.win_percentage:.1%}" +
        self.difficulty_data.__repr__())

    def calculate_percentages(self, bgg_format=True):
        if self.total_plays:
            self.win_percentage = self.total_wins/self.total_plays
        self.difficulty_data.calculate_percentages(bgg_format)



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


HERO_INIT_DATA  = {
    "Spider Man" : HeroData("Spider Man"),
    "Spider Ham" : HeroData("Spider Ham"),
    "Miles Morales" : HeroData("Miles Morales"),
    "Spider Woman" : HeroData("Spider Woman"),
    "Spider Gwen" : HeroData("Spider Gwen"),
    "Ms. Marvel" : HeroData("Ms. Marvel"),
    "Iron Man" : HeroData("Iron Man"),
    "Captain Marvel" : HeroData("Captain Marvel"),
    "She-Hulk" : HeroData("She-Hulk"),
    "Black Panther" : HeroData("Black Panther"),
    "Ant Man" : HeroData("Ant Man"),
    "Wasp" : HeroData("Wasp"),
    "Quicksilver" : HeroData("Quicksilver"),
    "Scarlet Witch" : HeroData("Scarlet Witch"),
    "Captain America" : HeroData("Captain America"),
    "Doctor Strange" : HeroData("Doctor Strange"),
    "Hulk" : HeroData("Hulk"),
    "Thor" : HeroData("Thor"),
    "Black Widow" : HeroData("Black Widow"),
    "Hawkeye" : HeroData("Hawkeye"),
    "Rocket Raccoon" : HeroData("Rocket Raccoon"),
    "Groot" : HeroData("Groot"),
    "Gamora" : HeroData("Gamora"),
    "Star Lord" : HeroData("Star Lord"),
    "Drax" : HeroData("Drax"),
    "Venom" : HeroData("Venom"),
    "Adam Warlock" : HeroData("Adam Warlock"),
    "Spectrum" : HeroData("Spectrum"),
    "Nebula" : HeroData("Nebula"),
    "War Machine" : HeroData("War Machine"),
    "Vision" : HeroData("Vision"),
    "Valkyrie" : HeroData("Valkyrie"),
    "Miles Morales" : HeroData("Miles Morales"),
    "Ghost Spider" : HeroData("Ghost Spider"),
    "Iron Heart" : HeroData("Iron Heart"),
    "Nova" : HeroData("Nova"),
    "Cyclops" : HeroData("Cyclops"),
    "Shadowcat" : HeroData("Shadowcat"),
    "Colossus" : HeroData("Colossus"),
    "Phoenix" : HeroData("Phoenix"),
    "Sp//der" : HeroData("Sp//der"),
}
VILLAIN_INIT_DATA = {
    "Ultron": VillainData("Ultron"),
    "Klaw": VillainData("Klaw"),
    "Rhino": VillainData("Rhino"),
    "Green Goblin - Risky Business": VillainData("Green Goblin - Risky Business"),
    "Green Goblin - Mutagen Formula": VillainData("Green Goblin - Mutagen Formula"),
    "Wrecking Crew": VillainData("Wrecking Crew"),
    "Crossbones": VillainData("Crossbones"),
    "Absorbing Man": VillainData("Absorbing Man"),
    "Taskmaster": VillainData("Taskmaster"),
    "Amin Zola": VillainData("Amin Zola"),
    "Red Skull": VillainData("Red Skull"),
    "Kang": VillainData("Kang"),
    "Drang": VillainData("Drang"),
    "Nebula": VillainData("Nebula"),
    "Ronan": VillainData("Ronan"),
    "Ebony Maw": VillainData("Ebony Maw"),
    "Thanos": VillainData("Thanos"),
    "Loki": VillainData("Loki"),
    "Venom": VillainData("Venom"),
    "Sandman": VillainData("Sandman"),
    "Mysterio": VillainData("Mysterio"),
    "Sinister Six": VillainData("Sinister Six"),
    "Venom Goblin": VillainData("Venom Goblin"),
    "Tower Defense": VillainData("Tower Defense"),
    "Hela": VillainData("Hela"),
    "Hood": VillainData("Hood"),
    "Magneto": VillainData("Magneto"),
    "Sabretooth": VillainData("Sabretooth"),
    "Master Mold": VillainData("Master Mold"),
    "Mansion Attack": VillainData("Mansion Attack"),
    "Project Wideawake": VillainData("Project Wideawake"),
    "The Collector - Infiltrate the Museum": VillainData("The Collector - Infiltrate the Museum"),
    "The Collector - Escape the Museum": VillainData("The Collector - Escape the Museum"),

}

class Statistics:
    def __init__(self, all_plays, bgg_format=True):
        self.all_plays = all_plays
        self.overall_data = OverallData(all_plays)
        self.hero_data = HERO_INIT_DATA
        self.villain_data = VILLAIN_INIT_DATA
        self.villain_h_index = 0
        self.hero_h_index = 0
        self.bgg_format=bgg_format

    def analyze_hero_data(self):
        for play in self.all_plays:
            for hero in play["Heroes"]:
                self.hero_data[hero["Hero"]].add_play(hero)

        for hero in self.hero_data:
            self.hero_data[hero].calculate_percentages(self.bgg_format)


    def analyze_villain_data(self):
        for play in self.all_plays:
            self.villain_data[play["Villain"]].add_play(play)

        for villain in self.villain_data:
            self.villain_data[villain].calculate_percentages(self.bgg_format)


    def calculate_h_indices(self):
        sorted_heroes = sorted(self.hero_data.items(), key=lambda x: x[1].total_plays, reverse=True)
        for i, h in enumerate(sorted_heroes):
            if self.hero_h_index < h[1].total_plays :
                self.hero_h_index += 1

        sorted_villains = sorted(self.villain_data.items(), key=lambda x: x[1].total_plays, reverse=True)
        for i, h in enumerate(sorted_villains):
            if self.villain_h_index < h[1].total_plays :
                self.villain_h_index += 1

        return None

    def __repr__(self):
        repr_string = "===========================================================\n"
        repr_string += self.overall_data.__repr__() + "\n"
        repr_string += "===========================================================\n"
        repr_string += f"Hero-H Index: {self.hero_h_index}   Villain H-Index: {self.villain_h_index}\n"
        repr_string += "===========================================================\n"
        sorted_heroes = sorted(self.hero_data.items(), key=lambda x: x[1].total_plays, reverse=True)
        for i, hero in enumerate(sorted_heroes):
            if hero[1].total_plays > 0:
                repr_string += f"{i+1}. " + hero[1].hero_name + "\n"
                repr_string += hero[1].__repr__() + "\n"
                repr_string += "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"
        sorted_villains = sorted(self.villain_data.items(), key=lambda x: x[1].total_plays, reverse=True)
        for j, villain in enumerate(sorted_villains):
            if villain[1].total_plays > 0:
                repr_string += f"{j+1}. " + villain[1].villain_name + "\n"
                repr_string += villain[1].__repr__() + "\n"
                repr_string += "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"
        return repr_string




    def analyze_play_data(self, bgg_format=True):
        self.overall_data.analyze_overall_data()
        self.analyze_hero_data()
        self.analyze_villain_data()
        self.calculate_h_indices()
