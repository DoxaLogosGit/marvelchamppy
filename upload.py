import gspread
from time import sleep
from datetime import datetime, timedelta
from config import COLUMNS

class UploadData:


    def __init__(self, statistics, skip_found=False, diff_data=None):
        self.statistics = statistics
        self.sheet = None
        self.skip_found = skip_found
        self.diff_data = diff_data


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
        if(self.diff_data is None):
            hero_list = self.statistics.hero_data.keys()
        else:
            hero_list = list(self.diff_data[1])

        print("Uploading Hero statistics...")
        for hero in sorted(hero_list):
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
            
    def upload_teams(self, worksheets):
        if(self.diff_data is None):
            team_list = self.statistics.team_data.keys()
        else:
            team_list = []
            for hero in list(self.diff_data[1]):
                for trait in self.statistics.hero_data[hero].traits:
                    if trait in self.statistics.team_data.keys():
                        team_list.append(trait)
                

        print("Uploading Team statistics...")
        for team in sorted(team_list):
            skip = False
            if team not in worksheets:
                print(f"creating {team} worksheet, not found")
                hsheet = self.sheet.add_worksheet(title = team, rows=100, cols=100)
            else:
                print(f"found {team} worksheet, -- ")
                hsheet = self.sheet.worksheet(team)
                skip = self.skip_found

            if not skip:
                self.update_hero_sheet(self.statistics.team_data[team], hsheet)
            

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
        if(self.diff_data is None):
            villain_list = self.statistics.villain_data.keys()
        else:
            villain_list = list(self.diff_data[0])

        print("Uploading Villain statistics...")
        for villain in sorted(villain_list):
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


    def upload_big_box_expansions(self, worksheets):
        if(self.diff_data is None):
            big_box_list = self.statistics.big_box_data.keys()
        else:
            #grab expansion data out of villain
            big_box_list = []
            for villain in list(self.diff_data[0]):
                if self.statistics.villain_data[villain].expansion in self.statistics.big_box_data.keys():
                    big_box_list.append(self.statistics.villain_data[villain].expansion)
                
        print("Uploading Big Box statistics...")
        for big_box in sorted(big_box_list):
            skip = False
            if big_box not in worksheets:
                print(f"creating {big_box} worksheet, not found")
                vsheet = self.sheet.add_worksheet(title = big_box, rows=100, cols=100)
            else:
                print(f"found {big_box} worksheet, -- ")
                vsheet = self.sheet.worksheet(big_box)
                skip = self.skip_found

            if not skip:
                self.update_villain_sheet(self.statistics.big_box_data[big_box], vsheet)

    def upload_scenario_packs(self, worksheets):
        if(self.diff_data is None):
            scenario_pack_list = self.statistics.scenario_pack_data.keys()
        else:
            #grab expansion data out of villain
            scenario_pack_list = []
            for villain in list(self.diff_data[0]):
                if self.statistics.villain_data[villain].expansion in self.statistics.scenario_pack_data.keys():
                    scenario_pack_list.append(self.statistics.villain_data[villain].expansion)
                
        print("Uploading Scenario Pack statistics...")
        for scenario_pack in sorted(scenario_pack_list):
            skip = False
            if scenario_pack not in worksheets:
                print(f"creating {scenario_pack} worksheet, not found")
                vsheet = self.sheet.add_worksheet(title = scenario_pack, rows=100, cols=100)
            else:
                print(f"found {scenario_pack} worksheet, -- ")
                vsheet = self.sheet.worksheet(scenario_pack)
                skip = self.skip_found

            if not skip:
                self.update_villain_sheet(self.statistics.scenario_pack_data[scenario_pack], vsheet)

    def upload_play_matrix(self):
        print("Uploading Play Matrix statistics...")
        psheet = self.sheet.worksheet("Play Matrix")
        #clear sheet
        psheet.batch_clear(["A1:ZZ200"])
        psheet.add_cols(100)
        psheet.format("B2:ZZ200", {'textFormat': {'bold':True}, 'horizontalAlignment': "CENTER"})
        #print the hero names
        heroes = sorted(self.statistics.hero_data.keys())
        for n, hero in enumerate(heroes):
            psheet.update(f"A{n+2}", f"{hero}")

        #walk the villains
        villains = sorted(self.statistics.villain_data.keys())
        for column, villain in enumerate(villains):
            #walk heroes played
            for hero_played in self.statistics.villain_data[villain].heroes_played:
                #see where in the list the hero played is in there
                for index, hero in enumerate(heroes):
                    if index == 0:
                        #print the name on first row
                        psheet.update(f"{COLUMNS[column]}1", f"{villain}")
                    if hero_played == hero:
                        #found here, print x
                        psheet.update(f"{COLUMNS[column]}{index+2}", "X")
                            
                        



    def upload_overall(self):
        print("Uploading Overall statistics...")
        osheet = self.sheet.worksheet("Overall")
        #clear sheet
        osheet.batch_clear(["A1:Z100"])
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
        osheet.update("H1", "Plays")
        osheet.update("I1", "Wins")
        osheet.update("J1", "Percentage")
        for n, data in enumerate(self.statistics.sorted_team_list):
            osheet.update(f"G{n+2}", data[0])
            osheet.update(f"H{n+2}", data[1])
            osheet.update(f"I{n+2}", self.statistics.team_data[data[0]].total_wins)
            osheet.format(f"J{n+2}", {'numberFormat': {'type':'PERCENT', 'pattern': '0%'}})
            osheet.update(f"J{n+2}", self.statistics.team_data[data[0]].win_percentage)

        #hero H-Index (K-L)
        osheet.update("K1", f"Hero H-Index: {self.statistics.hero_h_index}")
        osheet.update("L1", "Plays")
        for n, hero in enumerate(self.statistics.sorted_heroes):
            osheet.update(f"K{n+2}", f"{n+1}. {hero[1].name}")
            osheet.update(f"L{n+2}", hero[1].total_plays)
        #villain H-Index (M-N)
        osheet.update("M1", f"Villain H-Index: {self.statistics.villain_h_index}")
        osheet.update("N1", "Plays")
        for n, villain in enumerate(self.statistics.sorted_villains):
            osheet.update(f"M{n+2}", f"{n+1}. {villain[1].name}")
            osheet.update(f"N{n+2}", villain[1].total_plays)

        #hero win percentage (O-P)
        osheet.update("O1", f"Hero")
        osheet.update("P1", " Winning Percent")
        printed_row = 2 #start row
        for hero in self.statistics.sorted_percent_heroes:
            #only upload those with minimum number of plays and opponents
            if(hero[1].total_plays >= 10 and len(hero[1].villains_played) >=8):
                osheet.update(f"O{printed_row}", f"{printed_row-1}. {hero[1].name}")
                osheet.format(f"P{printed_row}", {'numberFormat': {'type':'PERCENT', 'pattern': '0%'}})
                osheet.update(f"P{printed_row}", hero[1].win_percentage)
                printed_row += 1

        #villain win percentage (Q-R)
        osheet.update("Q1", f"Villain")
        osheet.update("R1", "Losing Percent")
        printed_row = 2 #start row
        for villain in self.statistics.sorted_percent_villains:
            #only upload those with minimum number of plays and opponents
            if(villain[1].total_plays >= 10 and len(villain[1].heroes_played) >= 8):
                osheet.update(f"Q{printed_row}", f"{printed_row-1}. {villain[1].name}")
                osheet.format(f"R{printed_row}", {'numberFormat': {'type':'PERCENT', 'pattern': '0%'}})
                osheet.update(f"R{printed_row}", villain[1].win_percentage)
                printed_row += 1

    def perform_upload(self):
        self.login()
#        self.upload_overall()
        self.upload_play_matrix()
#        worksheets = [x.title for x in self.sheet.worksheets()]
#        sleep(5)
#        self.upload_heroes(worksheets)
#        sleep(20)
#        self.upload_teams(worksheets)
#        sleep(5)
#        self.upload_villains(worksheets)
#        sleep(5)
#        self.upload_big_box_expansions(worksheets)
#        sleep(5)
#        self.upload_scenario_packs(worksheets)
        
