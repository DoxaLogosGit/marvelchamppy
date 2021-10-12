class HeroData:
    def __init__(self, hero):
        self.hero_name = hero
        self.total_plays = 0
        self.total_wins = 0
        self.win_percentage = 0
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

    def add_play(self, play):
        """
        Assumes the caller has matched up the hero
        """
        self.total_plays += 1
        this_was_a_win = play["Win"]
        self.total_wins += this_was_a_win
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

    def __repr__(self):
        return ("[b]Overall Data[/b]" +
        "\nTotal Plays: {}".format(self.total_plays) +
        "\nTotal Wins: {}".format(self.total_wins) +
        "\nTotal Win  %: {:.2%}".format(self.win_percentage) +
        "\n\n[b]Aspect Data[/b][b][COLOR=#00CCCC]" +
        "\nLeadership Plays: {}".format(self.leadership_plays) +
        "\nLeadership Wins: {}".format(self.leadership_wins) +
        "\nLeadership Wins %: {:.2%}".format(self.leadership_win_percentage) +
        "\n[/COLOR] [COLOR=#FF0000]" +
        "\nAggression Plays: {}".format(self.aggression_plays) +
        "\nAggression Wins: {}".format(self.aggression_wins) +
        "\nAggression Wins %: {:.2%}".format(self.aggression_win_percentage) +
        "\n[/COLOR] [BGCOLOR=#003399][COLOR=#FFFF00]" +
        "\nJustice Plays: {}".format(self.justice_plays) +
        "\nJustice Wins: {}".format(self.justice_wins) +
        "\nJustice Wins %: {:.2%}".format(self.justice_win_percentage) +
        "\n[/BGCOLOR][/COLOR] [COLOR=#00FF33]" +
        "\nProtection Plays: {}".format(self.protection_plays) +
        "\nProtection Wins: {}".format(self.protection_wins) +
        "\nProtection Wins %: {:.2%}".format(self.protection_win_percentage) +
        "\n[/COLOR] [COLOR=#808080]" +
        "\nBasic Plays: {}".format(self.basic_plays) +
        "\nBasic Wins: {}".format(self.basic_wins) +
        "\nBasic Wins %: {:.2%}".format(self.basic_win_percentage) +
        "\n[/COLOR][/b]")


    def calculate_percentages(self):
        if self.total_plays:
            self.win_percentage = self.total_wins/self.total_plays
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



class VillainData:
    def __init__(self, villain):
        self.villain_name = villain
        self.total_plays = 0
        self.total_wins = 0
        self.win_percentage = 0
        self.expert_plays = 0
        self.expert_wins = 0
        self.expert_win_percentage = 0
        self.standard_plays = 0
        self.standard_wins = 0
        self.standard_win_percentage = 0
        self.heroic_plays = 0
        self.heroic_wins = 0
        self.heroic_win_percentage = 0

    def add_play(self, play):
        self.total_plays += 1
        this_was_a_win = play["Heroes"][0]["Win"]
        self.total_wins += this_was_a_win

        if play["Difficulty"] == "Expert":
            self.expert_plays += 1
            self.expert_wins += this_was_a_win
        elif play["Difficulty"] == "Standard":
            self.standard_plays += 1
            self.standard_wins += this_was_a_win
        elif play["Difficulty"] == "Heroic":
            self.heroic_plays += 1
            self.heroic_wins += this_was_a_win

    def __repr__(self):
        return ("Total Plays: {}".format(self.total_plays) +
        "\nTotal Wins: {}".format(self.total_wins) +
        "\nTotal Win  %: {:.2%}".format(self.win_percentage) +
        "\nExpert Plays: {}".format(self.expert_plays) +
        "\nExpert Wins: {}".format(self.expert_wins) +
        "\nExpert Wins %: {:.2%}".format(self.expert_win_percentage) +
        "\nStandard Plays: {}".format(self.standard_plays) +
        "\nStandard Wins: {}".format(self.standard_wins) +
        "\nStandard Wins %: {:.2%}".format(self.standard_win_percentage) +
        "\nHeroic Plays: {}".format(self.heroic_plays) +
        "\nHeroic Wins: {}".format(self.heroic_wins) +
        "\nHeroic Wins %: {:.2%}".format(self.heroic_win_percentage))

    def calculate_percentages(self):
        if self.total_plays:
            self.win_percentage = self.total_wins/self.total_plays
        if self.expert_plays:
            self.expert_win_percentage = self.expert_wins/self.expert_plays
        if self.standard_plays:
            self.standard_win_percentage = self.standard_wins/self.standard_plays
        if self.heroic_plays:
            self.heroic_win_percentage = self.heroic_wins/self.heroic_plays



class OverallData:

    def __init__(self, all_plays):
        self.all_plays = all_plays
        self.overall_plays = len(all_plays)
        self.overall_wins = 0
        self.overall_win_percentage = 0
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
        self.expert_plays = 0
        self.expert_wins = 0
        self.expert_win_percentage = 0
        self.standard_plays = 0
        self.standard_wins = 0
        self.standard_win_percentage = 0
        self.heroic_plays = 0
        self.heroic_wins = 0
        self.heroic_win_percentage = 0

    def calculate_percentages(self):
        if self.overall_plays:
            self.overall_win_percentage = self.overall_wins/self.overall_plays
        if self.expert_plays:
            self.expert_win_percentage = self.expert_wins/self.expert_plays
        if self.standard_plays:
            self.standard_win_percentage = self.standard_wins/self.standard_plays
        if self.heroic_plays:
            self.heroic_win_percentage = self.heroic_wins/self.heroic_plays
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
        return None

    def __repr__(self):
        return ("[b]Overall Data[/b][b]" +
        "\nTotal Plays: {}".format(self.overall_plays) +
        "\nTotal Wins: {}".format(self.overall_wins) +
        "\nTotal Win  %: {:.2%}".format(self.overall_win_percentage) +
        "\n[b]Difficulty Data:[/b]" +
        "\nExpert Plays: {}".format(self.expert_plays) +
        "\nExpert Wins: {}".format(self.expert_wins) +
        "\nExpert Wins %: {:.2%}".format(self.expert_win_percentage) +
        "\nStandard Plays: {}".format(self.standard_plays) +
        "\nStandard Wins: {}".format(self.standard_wins) +
        "\nStandard Wins %: {:.2%}".format(self.standard_win_percentage) +
        "\nHeroic Plays: {}".format(self.heroic_plays) +
        "\nHeroic Wins: {}".format(self.heroic_wins) +
        "\nHeroic Wins %: {:.2%}".format(self.heroic_win_percentage) +
        "\n[b]Aspect Data:[/b]" +
        "\n[b][COLOR=#00CCCC]" +
        "\nLeadership Plays: {}".format(self.leadership_plays) +
        "\nLeadership Wins: {}".format(self.leadership_wins) +
        "\nLeadership Wins %: {:.2%}".format(self.leadership_win_percentage) +
        "\n[/COLOR] [COLOR=#FF0000]" +
        "\nAggression Plays: {}".format(self.aggression_plays) +
        "\nAggression Wins: {}".format(self.aggression_wins) +
        "\nAggression Wins %: {:.2%}".format(self.aggression_win_percentage) +
        "\n[/COLOR] [BGCOLOR=#003399][COLOR=#FFFF00]" +
        "\nJustice Plays: {}".format(self.justice_plays) +
        "\nJustice Wins: {}".format(self.justice_wins) +
        "\nJustice Wins %: {:.2%}".format(self.justice_win_percentage) +
        "\n[/BGCOLOR][/COLOR] [COLOR=#00FF33]" +
        "\nProtection Plays: {}".format(self.protection_plays) +
        "\nProtection Wins: {}".format(self.protection_wins) +
        "\nProtection Wins %: {:.2%}".format(self.protection_win_percentage) +
        "\n[/COLOR] [COLOR=#808080]" +
        "\nBasic Plays: {}".format(self.basic_plays) +
        "\nBasic Wins: {}".format(self.basic_wins) +
        "\nBasic Wins %: {:.2%}".format(self.basic_win_percentage)+
        "\n[/COLOR][/b]")


    def analyze_overall_data(self):
        """
        Main function to analyze the overall data
        """
        for play in self.all_plays:
            this_was_a_win = play["Heroes"][0]["Win"]
            self.overall_wins += this_was_a_win


            if play["Difficulty"] == "Expert":
                self.expert_plays += 1
                self.expert_wins += this_was_a_win
            elif play["Difficulty"] == "Standard":
                self.standard_plays += 1
                self.standard_wins += this_was_a_win
            elif play["Difficulty"] == "Heroic":
                self.heroic_plays += 1
                self.heroic_wins += this_was_a_win

            for hero in play["Heroes"]:
                if "justice" in hero["Aspect"].lower():
                    self.justice_plays += 1
                    self.justice_wins += this_was_a_win
                if "protection" in hero["Aspect"].lower():
                    self.protection_plays += 1
                    self.protection_wins += this_was_a_win
                if "aggression" in hero["Aspect"].lower():
                    self.aggression_plays += 1
                    self.aggression_wins += this_was_a_win
                if "leadership" in hero["Aspect"].lower():
                    self.leadership_plays += 1
                    self.leadership_wins += this_was_a_win
                if "basic" in hero["Aspect"].lower():
                    self.basic_plays += 1
                    self.basic_wins += this_was_a_win

        self.calculate_percentages()


HERO_INIT_DATA  = {
    "Spider Man" : HeroData("Spider Man"),
    "Spider Woman" : HeroData("Spider Woman"),
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
    "Thanos": VillainData("Thanos"),
    "Loki": VillainData("Loki"),
    "Hood": VillainData("Hood"),
    "The Collector - Infiltrate the Museum": VillainData("The Collector - Infiltrate the Museum"),
    "The Collector - Escape the Museum": VillainData("The Collector - Escape the Museum"),

}

class Statistics:
    def __init__(self, all_plays):
        self.all_plays = all_plays
        self.overall_data = OverallData(all_plays)
        self.hero_data = HERO_INIT_DATA
        self.villain_data = VILLAIN_INIT_DATA
        self.villain_h_index = 0
        self.hero_h_index = 0

    def analyze_hero_data(self):
        for play in self.all_plays:
            for hero in play["Heroes"]:
                self.hero_data[hero["Hero"]].add_play(hero)

        for hero in self.hero_data:
            self.hero_data[hero].calculate_percentages()


    def analyze_villain_data(self):
        for play in self.all_plays:
            self.villain_data[play["Villain"]].add_play(play)

        for villain in self.villain_data:
            self.villain_data[villain].calculate_percentages()


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
        repr_string += "Hero-H Index: {0}   Villain H-Index: {1}\n".format(self.hero_h_index, self.villain_h_index)
        repr_string += "===========================================================\n"
        sorted_heroes = sorted(self.hero_data.items(), key=lambda x: x[1].total_plays, reverse=True)
        for hero in sorted_heroes:
            if hero[1].total_plays > 0:
                repr_string += hero[1].hero_name + "\n"
                repr_string += hero[1].__repr__() + "\n"
                repr_string += "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"
        sorted_villains = sorted(self.villain_data.items(), key=lambda x: x[1].total_plays, reverse=True)
        for villain in sorted_villains:
            if villain[1].total_plays > 0:
                repr_string += villain[1].villain_name + "\n"
                repr_string += villain[1].__repr__() + "\n"
                repr_string += "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"
        return repr_string




    def analyze_play_data(self):
        self.overall_data.analyze_overall_data()
        self.analyze_hero_data()
        self.analyze_villain_data()
        self.calculate_h_indices()
