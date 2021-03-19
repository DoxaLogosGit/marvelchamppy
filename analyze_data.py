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
        return ("Total Plays: {}".format(self.total_plays) +
        "\nTotal Wins: {}".format(self.total_wins) +
        "\nTotal Win  %: {}%".format(self.win_percentage) +
        "\nLeadership Plays: {}".format(self.leadership_plays) +
        "\nLeadership Wins: {}".format(self.leadership_wins) +
        "\nLeadership Wins %: {}%".format(self.leadership_win_percentage) +
        "\nAggression Plays: {}".format(self.aggression_plays) +
        "\nAggression Wins: {}".format(self.aggression_wins) +
        "\nAggression Wins %: {}%".format(self.aggression_win_percentage) +
        "\nJustice Plays: {}".format(self.justice_plays) +
        "\nJustice Wins: {}".format(self.justice_wins) +
        "\nJustice Wins %: {}%".format(self.justice_win_percentage) +
        "\nProtection Plays: {}".format(self.protection_plays) +
        "\nProtection Wins: {}".format(self.protection_wins) +
        "\nProtection Wins %: {}%".format(self.protection_win_percentage) +
        "\nBasic Plays: {}".format(self.basic_plays) +
        "\nBasic Wins: {}".format(self.basic_wins) +
        "\nBasic Wins %: {}%".format(self.basic_win_percentage))


    def calculate_percentages(self):
        if self.total_plays:
            self.win_percentage = self.total_wins/self.total_plays * 100
        if self.leadership_plays:
            self.leadership_win_percentage = self.leadership_wins/self.leadership_plays * 100
        if self.justice_plays:
            self.justice_win_percentage = self.justice_wins/self.justice_plays * 100
        if self.protection_plays:
            self.protection_win_percentage = self.protection_wins/self.protection_plays * 100
        if self.basic_plays:
            self.basic_win_percentage = self.basic_wins/self.basic_plays * 100
        if self.aggression_plays:
            self.aggression_win_percentage = self.aggression_wins/self.aggression_plays * 100



class VillainData:
    def __init__(self, villain):
        self.villain = villain
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
        "\nTotal Win  %: {}%".format(self.win_percentage) +
        "\nExpert Plays: {}".format(self.expert_plays) +
        "\nExpert Wins: {}".format(self.expert_wins) +
        "\nExpert Wins %: {}%".format(self.expert_win_percentage) +
        "\nStandard Plays: {}".format(self.standard_plays) +
        "\nStandard Wins: {}".format(self.standard_wins) +
        "\nStandard Wins %: {}%".format(self.standard_win_percentage) +
        "\nHeroic Plays: {}".format(self.heroic_plays) +
        "\nHeroic Wins: {}".format(self.heroic_wins) +
        "\nHeroic Wins %: {}%".format(self.heroic_win_percentage))

    def calculate_percentages(self):
        if self.total_plays:
            self.win_percentage = self.total_wins/self.total_plays * 100
        if self.expert_plays:
            self.expert_win_percentage = self.expert_wins/self.expert_plays * 100
        if self.standard_plays:
            self.standard_win_percentage = self.standard_wins/self.standard_plays * 100
        if self.heroic_plays:
            self.heroic_win_percentage = self.heroic_wins/self.heroic_plays * 100



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
            self.overall_win_percentage = self.overall_wins/self.overall_plays * 100
        if self.expert_plays:
            self.expert_win_percentage = self.expert_wins/self.expert_plays * 100
        if self.standard_plays:
            self.standard_win_percentage = self.standard_wins/self.standard_plays * 100
        if self.heroic_plays:
            self.heroic_win_percentage = self.heroic_wins/self.heroic_plays * 100
        if self.leadership_plays:
            self.leadership_win_percentage = self.leadership_wins/self.leadership_plays * 100
        if self.justice_plays:
            self.justice_win_percentage = self.justice_wins/self.justice_plays * 100
        if self.protection_plays:
            self.protection_win_percentage = self.protection_wins/self.protection_plays * 100
        if self.basic_plays:
            self.basic_win_percentage = self.basic_wins/self.basic_plays * 100
        if self.aggression_plays:
            self.aggression_win_percentage = self.aggression_wins/self.aggression_plays * 100
        return None

    def __repr__(self):
        return ("Total Plays: {}".format(self.overall_plays) +
        "\nTotal Wins: {}".format(self.overall_wins) +
        "\nTotal Win  %: {}%".format(self.overall_win_percentage) +
        "\nExpert Plays: {}".format(self.expert_plays) +
        "\nExpert Wins: {}".format(self.expert_wins) +
        "\nExpert Wins %: {}%".format(self.expert_win_percentage) +
        "\nStandard Plays: {}".format(self.standard_plays) +
        "\nStandard Wins: {}".format(self.standard_wins) +
        "\nStandard Wins %: {}%".format(self.standard_win_percentage) +
        "\nHeroic Plays: {}".format(self.heroic_plays) +
        "\nHeroic Wins: {}".format(self.heroic_wins) +
        "\nHeroic Wins %: {}%".format(self.heroic_win_percentage) +
        "\nLeadership Plays: {}".format(self.leadership_plays) +
        "\nLeadership Wins: {}".format(self.leadership_wins) +
        "\nLeadership Wins %: {}%".format(self.leadership_win_percentage) +
        "\nAggression Plays: {}".format(self.aggression_plays) +
        "\nAggression Wins: {}".format(self.aggression_wins) +
        "\nAggression Wins %: {}%".format(self.aggression_win_percentage) +
        "\nJustice Plays: {}".format(self.justice_plays) +
        "\nJustice Wins: {}".format(self.justice_wins) +
        "\nJustice Wins %: {}%".format(self.justice_win_percentage) +
        "\nProtection Plays: {}".format(self.protection_plays) +
        "\nProtection Wins: {}".format(self.protection_wins) +
        "\nProtection Wins %: {}%".format(self.protection_win_percentage) +
        "\nBasic Plays: {}".format(self.basic_plays) +
        "\nBasic Wins: {}".format(self.basic_wins) +
        "\nBasic Wins %: {}%".format(self.basic_win_percentage))


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
}
VILLAIN_INIT_DATA = {
    "Ultron": VillainData("Ultron"),
    "Klaw": VillainData("Klaw"),
    "Rhino": VillainData("Rhino"),
    "Green Goblin": VillainData("Green Goblin"),
    "Wrecking Crew": VillainData("Wrecking Crew"),
    "Crossbones": VillainData("Crossbones"),
    "Absorbing Man": VillainData("Absorbing Man"),
    "Taskmaster": VillainData("Taskmaster"),
    "Amin Zola": VillainData("Amin Zola"),
    "Red Skull": VillainData("Red Skull"),
    "Kang": VillainData("Kang"),

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
        repr_string = self.overall_data.__repr__() + "\n"
        repr_string += "Hero-H Index: {0}   Villain H-Index: {1}\n".format(self.hero_h_index, self.villain_h_index)
        for hero in self.hero_data:
            repr_string += hero + "\n"
            repr_string += self.hero_data[hero].__repr__() + "\n"
        for villain in self.villain_data:
            repr_string += villain + "\n"
            repr_string += self.villain_data[villain].__repr__() + "\n"
        return repr_string




    def analyze_play_data(self):
        self.overall_data.analyze_overall_data()
        self.analyze_hero_data()
        self.analyze_villain_data()
        self.calculate_h_indices()
