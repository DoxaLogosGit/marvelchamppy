import gspread
from time import sleep
from datetime import datetime, timedelta

class UploadData:

    
    def __init__(self, statistics, skip_found=False):
        self.statistics = statistics
        self.sheet = None
        self.skip_found = skip_found

        
    def login(self):
        gc = gspread.service_account(client_factory=gspread.client.BackoffClient)
        self.sheet = gc.open("Marvel Champions Data")

        
    def update_difficulty(self, data, sheet):
        sheet.update("C1", "Difficulty Data")
        start_row = 2
        increment = 0
        if data.difficulty_data.expert1_plays > 0:
            sheet.update(f"C{start_row + increment}", "S1E1 Plays")
            sheet.update(f"D{start_row + increment}", data.difficulty_data.expert1_plays)
            increment += 1
            sheet.update(f"C{start_row + increment}", "S1E1 Wins")
            sheet.update(f"D{start_row + increment}", data.difficulty_data.expert1_wins)
            increment += 1
            sheet.update(f"C{start_row + increment}", "S1E1 Win %")
            sheet.format( f"D{start_row + increment}", {'numberFormat': {'type':'PERCENT', 'pattern': '0%'}})
            sheet.update(f"D{start_row + increment}", data.difficulty_data.expert1_win_percentage)
            increment += 1

        if data.difficulty_data.expert2_plays > 0:
            sheet.update(f"C{start_row + increment}", "S1E2 Plays")
            sheet.update(f"D{start_row + increment}", data.difficulty_data.expert2_plays)
            increment += 1
            sheet.update(f"C{start_row + increment}", "S1E2 Wins")
            sheet.update(f"D{start_row + increment}", data.difficulty_data.expert2_wins)
            increment += 1
            sheet.update(f"C{start_row + increment}", "S1E2 Win %")
            sheet.format(f"D{start_row + increment}", {'numberFormat': {'type':'PERCENT', 'pattern': '0%'}})
            sheet.update(f"D{start_row + increment}", data.difficulty_data.expert2_win_percentage)
            increment += 1

        if data.difficulty_data.expert3_plays > 0:
            sheet.update(f"C{start_row + increment}", "S2E1 Plays")
            sheet.update(f"D{start_row + increment}", data.difficulty_data.expert3_plays)
            increment += 1
            sheet.update(f"C{start_row + increment}", "S2E1 Wins")
            sheet.update(f"D{start_row + increment}", data.difficulty_data.expert3_wins)
            increment += 1
            sheet.update(f"C{start_row + increment}", "S2E1 Win %")
            sheet.format(f"D{start_row + increment}", {'numberFormat': {'type':'PERCENT', 'pattern': '0%'}})
            sheet.update(f"D{start_row + increment}", data.difficulty_data.expert3_win_percentage)
            increment += 1

        if data.difficulty_data.expert4_plays > 0:
            sheet.update(f"C{start_row + increment}", "S2E2 Plays")
            sheet.update(f"D{start_row + increment}", data.difficulty_data.expert4_plays)
            increment += 1
            sheet.update(f"C{start_row + increment}", "S2E2 Wins")
            sheet.update(f"D{start_row + increment}", data.difficulty_data.expert4_wins)
            increment += 1
            sheet.update(f"C{start_row + increment}", "S2E2 Win %")
            sheet.format(f"D{start_row + increment}", {'numberFormat': {'type':'PERCENT', 'pattern': '0%'}})
            sheet.update(f"D{start_row + increment}", data.difficulty_data.expert4_win_percentage)
            increment += 1

        if data.difficulty_data.standard1_plays > 0:
            sheet.update(f"C{start_row + increment}", "S1 Plays")
            sheet.update(f"D{start_row + increment}", data.difficulty_data.standard1_plays)
            increment += 1
            sheet.update(f"C{start_row + increment}", "S1 Wins")
            sheet.update(f"D{start_row + increment}", data.difficulty_data.standard1_wins)
            increment += 1
            sheet.update(f"C{start_row + increment}", "S1 Win %")
            sheet.format(f"D{start_row + increment}", {'numberFormat': {'type':'PERCENT', 'pattern': '0%'}})
            sheet.update(f"D{start_row + increment}", data.difficulty_data.standard1_win_percentage)
            increment += 1

        if data.difficulty_data.standard2_plays > 0:
            sheet.update(f"C{start_row + increment}", "S2 Plays")
            sheet.update(f"D{start_row + increment}", data.difficulty_data.standard2_plays)
            increment += 1
            sheet.update(f"C{start_row + increment}", "S2 Wins")
            sheet.update(f"D{start_row + increment}", data.difficulty_data.standard2_wins)
            increment += 1
            sheet.update(f"C{start_row + increment}", "S2 Win %")
            sheet.format(f"D{start_row + increment}", {'numberFormat': {'type':'PERCENT', 'pattern': '0%'}})
            sheet.update(f"D{start_row + increment}", data.difficulty_data.standard2_win_percentage)
            increment += 1

        if data.difficulty_data.heroic_plays > 0:
            sheet.update(f"C{start_row + increment}", "Heroic Plays")
            sheet.update(f"D{start_row + increment}", data.difficulty_data.heroic_plays)
            increment += 1
            sheet.update(f"C{start_row + increment}", "Heroic Wins")
            sheet.update(f"D{start_row + increment}", data.difficulty_data.heroic_wins)
            increment += 1
            sheet.update(f"C{start_row + increment}", "Heroic Win %")
            sheet.format(f"D{start_row + increment}", {'numberFormat': {'type':'PERCENT', 'pattern': '0%'}})
            sheet.update(f"D{start_row + increment}", data.difficulty_data.heroic_win_percentage)
            increment += 1


    def update_aspects(self, data, sheet):
        sheet.update("E1", "Aspect Data")
        start_row = 2
        increment = 0
        if data.aspect_data.leadership_plays > 0:
            sheet.update(f"E{start_row + increment}", "Leadership Plays")
            sheet.update(f"F{start_row + increment}", data.aspect_data.leadership_plays)
            increment += 1
            sheet.update(f"E{start_row + increment}", "Leadership Wins")
            sheet.update(f"F{start_row + increment}", data.aspect_data.leadership_wins)
            increment += 1
            sheet.update(f"E{start_row + increment}", "Leadership Win %")
            sheet.format(f"F{start_row + increment}", {'numberFormat': {'type':'PERCENT', 'pattern': '0%'}})
            sheet.update(f"F{start_row + increment}", data.aspect_data.leadership_win_percentage)
            increment += 1
        if data.aspect_data.aggression_plays > 0:
            sheet.update(f"E{start_row + increment}", "Aggression Plays")
            sheet.update(f"F{start_row + increment}", data.aspect_data.aggression_plays)
            increment += 1
            sheet.update(f"E{start_row + increment}", "Aggression Wins")
            sheet.update(f"F{start_row + increment}", data.aspect_data.aggression_wins)
            increment += 1
            sheet.update(f"E{start_row + increment}", "Aggression Win %")
            sheet.format(f"F{start_row + increment}", {'numberFormat': {'type':'PERCENT', 'pattern': '0%'}})
            sheet.update(f"F{start_row + increment}", data.aspect_data.aggression_win_percentage)
            increment += 1
        if data.aspect_data.justice_plays > 0:
            sheet.update(f"E{start_row + increment}", "Justice Plays")
            sheet.update(f"F{start_row + increment}", data.aspect_data.justice_plays)
            increment += 1
            sheet.update(f"E{start_row + increment}", "Justice Wins")
            sheet.update(f"F{start_row + increment}", data.aspect_data.justice_wins)
            increment += 1
            sheet.update(f"E{start_row + increment}", "Justice Win %")
            sheet.format(f"F{start_row + increment}", {'numberFormat': {'type':'PERCENT', 'pattern': '0%'}})
            sheet.update(f"F{start_row + increment}", data.aspect_data.justice_win_percentage)
            increment += 1

        if data.aspect_data.protection_plays > 0:
            sheet.update(f"E{start_row + increment}", "Protection Plays")
            sheet.update(f"F{start_row + increment}", data.aspect_data.protection_plays)
            increment += 1
            sheet.update(f"E{start_row + increment}", "Protection Wins")
            sheet.update(f"F{start_row + increment}", data.aspect_data.protection_wins)
            increment += 1
            sheet.update(f"E{start_row + increment}", "Protection Win %")
            sheet.format(f"F{start_row + increment}", {'numberFormat': {'type':'PERCENT', 'pattern': '0%'}})
            sheet.update(f"F{start_row + increment}", data.aspect_data.protection_win_percentage)
            increment += 1

        if data.aspect_data.basic_plays > 0:
            sheet.update(f"E{start_row + increment}", "Basic Plays")
            sheet.update(f"F{start_row + increment}", data.aspect_data.basic_plays)
            increment += 1
            sheet.update(f"E{start_row + increment}", "Basic Wins")
            sheet.update(f"F{start_row + increment}", data.aspect_data.basic_wins)
            increment += 1
            sheet.update(f"E{start_row + increment}", "Basic Win %")
            sheet.format(f"F{start_row + increment}", {'numberFormat': {'type':'PERCENT', 'pattern': '0%'}})
            sheet.update(f"F{start_row + increment}", data.aspect_data.basic_win_percentage)
            increment += 1


    

    def update_hero_sheet(self, hero, sheet):
        #clear the sheet
        sheet.batch_clear(["A1:Z100"])
        #overall data
        sheet.format("A1:Z1", {'textFormat': {'bold':True}, 'horizontalAlignment': "CENTER"})
        sheet.update("A1", "Overall")
        sheet.update("A2", "Total Plays")
        sheet.update("B2", hero.total_plays)
        sheet.update("A3", "Total Wins")
        sheet.update("B3", hero.total_wins)
        sheet.format("B4", {'numberFormat': {'type':'PERCENT', 'pattern': '0%'}})
        sheet.update("A4", "Win %")
        sheet.update("B4", hero.win_percentage)
        #difficulty data (C-D)
        self.update_difficulty(hero, sheet)
        #aspect data (E-F)
        self.update_aspects(hero, sheet)
        
        #villain data G,H,I
        sheet.update("G1", f"Villains Fought - {len(hero.villains_played)}")
        for i, villain in enumerate(sorted(hero.villains_played)):
            sheet.update(f"G{i+2}", villain)

        sheet.update("H1", f"Villains Defeated - {len(hero.villains_defeated)}")
        for i, villain in enumerate(sorted(hero.villains_defeated)):
            sheet.update(f"H{i+2}", villain)

        sheet.update("I1", f"Villains Unplayed - {len(hero.villains_not_played)}")
        for i, villain in enumerate(sorted(hero.villains_not_played)):
            sheet.update(f"I{i+2}", villain)

    def upload_heroes(self, worksheets):
        print("Uploading Hero statistics...")
        for hero in sorted(self.statistics.hero_data.keys()):
            skip = False
            if hero not in worksheets:
                print(f"creating {hero} worksheet, not found")
                hsheet = self.sheet.add_worksheet(title = hero, rows=100, cols=100)
            else:
                print(f"found {hero} worksheet, -- ")
                hsheet = self.sheet.worksheet(hero)
                skip = self.skip_found

            if not skip:
                self.update_hero_sheet(self.statistics.hero_data[hero], hsheet)
            

    def update_villain_sheet(self, villain, sheet):
        #clear sheet
        sheet.batch_clear(["A1:Z100"])
        #overall data
        sheet.format("A1:Z1", {'textFormat': {'bold':True}, 'horizontalAlignment': "CENTER"})
        sheet.update("A1", "Overall")
        sheet.update("A2", "Total Plays")
        sheet.update("B2", villain.total_plays)
        sheet.update("A3", "Total Wins")
        sheet.update("B3", villain.total_wins)
        sheet.format("B4", {'numberFormat': {'type':'PERCENT', 'pattern': '0%'}})
        sheet.update("A4", "Win %")
        sheet.update("B4", villain.win_percentage)
        #difficulty data (C-D)
        self.update_difficulty(villain, sheet)
        #aspect data (E-F)
        self.update_aspects(villain, sheet)
        
        #villain data G,H
        sheet.update("G1", f"Heroes Fought - {len(villain.heroes_played)}")
        for i, hero in enumerate(sorted(villain.heroes_played)):
            sheet.update(f"G{i+2}", hero)

        #clear the unplayed before publishing unplayed (the list will shrink over time)
        range = f"H1:H{len(villain.heroes_played)+len(villain.heroes_not_played)+3}"
        sheet.batch_clear([range])
        sheet.update("H1", f"Heroes Unplayed - {len(villain.heroes_not_played)}")
        for i, hero in enumerate(sorted(villain.heroes_not_played)):
            sheet.update(f"H{i+2}", hero)

    def upload_villains(self, worksheets):
        print("Uploading Villain statistics...")
        for villain in sorted(self.statistics.villain_data.keys()):
            skip = False
            if villain not in worksheets:
                print(f"creating {villain} worksheet, not found")
                vsheet = self.sheet.add_worksheet(title = villain, rows=100, cols=100)
            else:
                print(f"found {villain} worksheet, -- ")
                vsheet = self.sheet.worksheet(villain)
                skip = self.skip_found

            if not skip:
                self.update_villain_sheet(self.statistics.villain_data[villain], vsheet)


    def upload_overall(self):
        print("Uploading Overall statistics...")
        osheet = self.sheet.worksheet("Overall")
        osheet.format("A1:Z1", {'textFormat': {'bold':True}, 'horizontalAlignment': "CENTER"})
        osheet.update("A1", "Overall")
        osheet.update("A2", "Total Plays")
        osheet.update("B2", self.statistics.overall_data.overall_plays)
        osheet.update("A3", "Total Wins")
        osheet.update("B3", self.statistics.overall_data.overall_wins)
        osheet.format("B4", {'numberFormat': {'type':'PERCENT', 'pattern': '0%'}})
        osheet.update("A4", "Win %")
        osheet.update("B4", self.statistics.overall_data.overall_win_percentage)
        osheet.update("A5", "Total True Solo Plays")
        osheet.update("B5", self.statistics.overall_data.overall_true_solo_plays)
        osheet.update("A6", "Total Multihanded Solo Plays")
        osheet.update("B6", self.statistics.overall_data.overall_solo_plays)
        osheet.update("A7", "Total Multiplayer Plays")
        osheet.update("B7", self.statistics.overall_data.overall_multi_plays)
        #difficulty data (C-D)
        self.update_difficulty(self.statistics.overall_data, osheet)
        #aspect data (E-F)
        self.update_aspects(self.statistics.overall_data, osheet)

        #team data (G-J)
        osheet.update("G1", "Team")
        #osheet.update("H1", "Plays")
        for n, data in enumerate(self.statistics.sorted_team_list):
            osheet.update(f"G{n+2}", data[0])
            osheet.update(f"H{n+2}", data[1])
            

        #hero H-Index (K-L)
        osheet.update("K1", f"Hero H-Index: {self.statistics.hero_h_index}")
        osheet.update("L1", "Plays")
        for n, hero in enumerate(self.statistics.sorted_heroes):
            osheet.update(f"K{n+2}", hero[1].hero_name)
            osheet.update(f"L{n+2}", hero[1].total_plays)
        #villain H-Index (M-N)
        osheet.update("M1", f"Villain H-Index: {self.statistics.villain_h_index}")
        osheet.update("N1", "Plays")
        for n, villain in enumerate(self.statistics.sorted_villains):
            osheet.update(f"M{n+2}", villain[1].villain_name)
            osheet.update(f"N{n+2}", villain[1].total_plays)

    def perform_upload(self):
        self.login()
        self.upload_overall()
        worksheets = [x.title for x in self.sheet.worksheets()]
        sleep(10)
        self.upload_heroes(worksheets)
        sleep(60)
        self.upload_villains(worksheets)
        