import xlsxwriter
from datetime import datetime, timedelta
from config import COLUMNS
import math
from rich.progress import track

class ExcelData:

    def __init__(self, statistics, skip_found=False, diff_data=None):
        self.statistics = statistics
        self.sheet = None
        self.skip_found = skip_found
        self.diff_data = diff_data
        try:
            self.sheet = xlsxwriter.Workbook("statistics.xlsx")
        except IOError:
            print("Error openign file")
            raise Exception
        except xlsxwriter:
            print("Error opening file")
            raise Exception

        self.bg_format = self.sheet.add_format({'bg_color': 'black'})
        self.bold_format = self.sheet.add_format({'bold':True, 'align': 'center'})
        self.win_format = self.sheet.add_format({'num_format': '0%'})
        self.invalid_excel = r"[]/\?:*"
        self.max_worksheet_name_length = 31


    def update_difficulty(self, data, sheet):
        sheet.write_string("C1", "Difficulty Data")
        start_row = 2
        increment = 0
        if data.difficulty_data.expert1_plays > 0:
            sheet.write_string(f"C{start_row + increment}", "S1E1 Plays")
            sheet.write(f"D{start_row + increment}", data.difficulty_data.expert1_plays)
            increment += 1
            sheet.write_string(f"C{start_row + increment}", "S1E1 Wins")
            sheet.write(f"D{start_row + increment}", data.difficulty_data.expert1_wins)
            increment += 1
            sheet.write_string(f"C{start_row + increment}", "S1E1 Win %")
            sheet.write(f"D{start_row + increment}", data.difficulty_data.expert1_win_percentage, self.win_format)
            increment += 1

        if data.difficulty_data.expert2_plays > 0:
            sheet.write_string(f"C{start_row + increment}", "S1E2 Plays")
            sheet.write(f"D{start_row + increment}", data.difficulty_data.expert2_plays)
            increment += 1
            sheet.write_string(f"C{start_row + increment}", "S1E2 Wins")
            sheet.write(f"D{start_row + increment}", data.difficulty_data.expert2_wins)
            increment += 1
            sheet.write_string(f"C{start_row + increment}", "S1E2 Win %")
            sheet.write(f"D{start_row + increment}", data.difficulty_data.expert2_win_percentage, self.win_format)
            increment += 1

        if data.difficulty_data.expert3_plays > 0:
            sheet.write_string(f"C{start_row + increment}", "S2E1 Plays")
            sheet.write(f"D{start_row + increment}", data.difficulty_data.expert3_plays)
            increment += 1
            sheet.write_string(f"C{start_row + increment}", "S2E1 Wins")
            sheet.write(f"D{start_row + increment}", data.difficulty_data.expert3_wins)
            increment += 1
            sheet.write_string(f"C{start_row + increment}", "S2E1 Win %")
            sheet.write(f"D{start_row + increment}", data.difficulty_data.expert3_win_percentage, self.win_format)
            increment += 1

        if data.difficulty_data.expert4_plays > 0:
            sheet.write_string(f"C{start_row + increment}", "S2E2 Plays")
            sheet.write(f"D{start_row + increment}", data.difficulty_data.expert4_plays)
            increment += 1
            sheet.write_string(f"C{start_row + increment}", "S2E2 Wins")
            sheet.write(f"D{start_row + increment}", data.difficulty_data.expert4_wins)
            increment += 1
            sheet.write_string(f"C{start_row + increment}", "S2E2 Win %")
            sheet.write(f"D{start_row + increment}", data.difficulty_data.expert4_win_percentage, self.win_format)
            increment += 1

        if data.difficulty_data.expert5_plays > 0:
            sheet.write_string(f"C{start_row + increment}", "S3E1 Plays")
            sheet.write(f"D{start_row + increment}", data.difficulty_data.expert5_plays)
            increment += 1
            sheet.write_string(f"C{start_row + increment}", "S3E1 Wins")
            sheet.write(f"D{start_row + increment}", data.difficulty_data.expert5_wins)
            increment += 1
            sheet.write_string(f"C{start_row + increment}", "S3E1 Win %")
            sheet.write(f"D{start_row + increment}", data.difficulty_data.expert5_win_percentage, self.win_format)
            increment += 1

        if data.difficulty_data.expert6_plays > 0:
            sheet.write_string(f"C{start_row + increment}", "S3E2 Plays")
            sheet.write(f"D{start_row + increment}", data.difficulty_data.expert6_plays)
            increment += 1
            sheet.write_string(f"C{start_row + increment}", "S3E2 Wins")
            sheet.write(f"D{start_row + increment}", data.difficulty_data.expert6_wins)
            increment += 1
            sheet.write_string(f"C{start_row + increment}", "S3E2 Win %")
            sheet.write(f"D{start_row + increment}", data.difficulty_data.expert6_win_percentage, self.win_format)
            increment += 1

        if data.difficulty_data.standard1_plays > 0:
            sheet.write_string(f"C{start_row + increment}", "S1 Plays")
            sheet.write(f"D{start_row + increment}", data.difficulty_data.standard1_plays)
            increment += 1
            sheet.write_string(f"C{start_row + increment}", "S1 Wins")
            sheet.write(f"D{start_row + increment}", data.difficulty_data.standard1_wins)
            increment += 1
            sheet.write_string(f"C{start_row + increment}", "S1 Win %")
            sheet.write(f"D{start_row + increment}", data.difficulty_data.standard1_win_percentage, self.win_format)
            increment += 1

        if data.difficulty_data.standard2_plays > 0:
            sheet.write_string(f"C{start_row + increment}", "S2 Plays")
            sheet.write(f"D{start_row + increment}", data.difficulty_data.standard2_plays)
            increment += 1
            sheet.write_string(f"C{start_row + increment}", "S2 Wins")
            sheet.write(f"D{start_row + increment}", data.difficulty_data.standard2_wins)
            increment += 1
            sheet.write_string(f"C{start_row + increment}", "S2 Win %")
            sheet.write(f"D{start_row + increment}", data.difficulty_data.standard2_win_percentage, self.win_format)
            increment += 1

        if data.difficulty_data.standard3_plays > 0:
            sheet.write_string(f"C{start_row + increment}", "S3 Plays")
            sheet.write(f"D{start_row + increment}", data.difficulty_data.standard3_plays)
            increment += 1
            sheet.write_string(f"C{start_row + increment}",  "S3 Wins")
            sheet.write(f"D{start_row + increment}", data.difficulty_data.standard3_wins)
            increment += 1
            sheet.write_string(f"C{start_row + increment}", "S3 Win %")
            sheet.write(f"D{start_row + increment}", data.difficulty_data.standard3_win_percentage, self.win_format)
            increment += 1

        if data.difficulty_data.heroic_plays > 0:
            sheet.write_string(f"C{start_row + increment}", "Heroic Plays")
            sheet.write(f"D{start_row + increment}", data.difficulty_data.heroic_plays)
            increment += 1
            sheet.write_string(f"C{start_row + increment}", "Heroic Wins")
            sheet.write(f"D{start_row + increment}", data.difficulty_data.heroic_wins)
            increment += 1
            sheet.write_string(f"C{start_row + increment}", "Heroic Win %")
            sheet.write(f"D{start_row + increment}", data.difficulty_data.heroic_win_percentage, self.win_format)
            increment += 1


    def update_aspects(self, data, sheet):
        sheet.write_string("E1", "Aspect Data")
        start_row = 2
        increment = 0
        for aspect in data.aspect_data.aspect_plays.keys():
            if data.aspect_data.aspect_plays[aspect].plays > 0:
                sheet.write_string(f"E{start_row + increment}", f"{aspect} Plays")
                sheet.write(f"F{start_row + increment}", data.aspect_data.aspect_plays[aspect].plays)
                increment += 1
                sheet.write_string(f"E{start_row + increment}", f"{aspect} Wins")
                sheet.write(f"F{start_row + increment}", data.aspect_data.aspect_plays[aspect].wins)
                increment += 1
                sheet.write_string(f"E{start_row + increment}", f"{aspect} Win %")
                sheet.write(f"F{start_row + increment}", data.aspect_data.aspect_plays[aspect].win_percentage, self.win_format)
                increment += 1


    

    def update_hero_sheet(self, hero, sheet):
        my_progress_track = track(range(7), f"Uploading {hero.name} statistics: ")
        next(my_progress_track)
        #overall data
        sheet.set_row(0,26, self.bold_format)
        sheet.write_string("A1", "Overall")
        sheet.write_string("A2", "Total Plays")
        sheet.write("B2", hero.total_plays)
        sheet.write_string("A3", "Total Wins")
        sheet.write("B3",  hero.total_wins)
        sheet.write_string("A4", "Win %")
        sheet.write("B4", hero.win_percentage, self.win_format)
        next(my_progress_track)
        #difficulty data (C-D)
        self.update_difficulty(hero, sheet)
        next(my_progress_track)
        #aspect data (E-F)
        self.update_aspects(hero, sheet)
        next(my_progress_track)
        
        #villain data G,H,I
        sheet.write_string("G1", f"Villains Fought - {len(hero.villains_played)}")
        for i, villain in enumerate(sorted(hero.villains_played)):
            sheet.write_string(f"G{i+2}", villain)
        next(my_progress_track)

        sheet.write_string("H1", f"Villains Not Defeated - {len(hero.villains_not_defeated)}")
        for i, villain in enumerate(sorted(hero.villains_not_defeated)):
            sheet.write_string(f"H{i+2}", villain)
        next(my_progress_track)

        sheet.write_string("I1", f"Villains Unplayed - {len(hero.villains_not_played)}")
        for i, villain in enumerate(sorted(hero.villains_not_played)):
            sheet.write_string(f"I{i+2}", villain)
        next(my_progress_track)
        next(my_progress_track, 0)

    def upload_heroes(self, worksheets):
        if(self.diff_data is None):
            hero_list = self.statistics.hero_data.keys()
        else:
            hero_list = list(self.diff_data[1])

        print("Uploading Hero statistics...")
        for hero in sorted(hero_list):
            if any(char in hero for char in self.invalid_excel):
                print(f"skipping {hero} due to invalid characters")
                continue
            skip = False
            if hero not in worksheets:
                print(f"creating {hero} worksheet, not found")
                hsheet = self.sheet.add_worksheet(hero)
            else:
                print(f"found {hero} worksheet, -- ")
                hsheet = self.sheet.get_worksheet_by_name(hero)
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
                hsheet = self.sheet.add_worksheet(team)
            else:
                print(f"found {team} worksheet, -- ")
                hsheet = self.sheet.get_worksheet_by_name(team)
                skip = self.skip_found

            if not skip:
                self.update_hero_sheet(self.statistics.team_data[team], hsheet)
            

    def update_villain_sheet(self, villain, sheet):
        my_progress_track = track(range(7), f"Uploading {villain.name} statistics: ")
        next(my_progress_track)
        #overall data
        sheet.set_row(0,26, self.bold_format)
        sheet.write_string("A1", "Overall")
        sheet.write_string("A2", "Total Plays")
        sheet.write("B2", villain.total_plays)
        sheet.write_string("A3", "Total Wins")
        sheet.write("B3", villain.total_wins)
        sheet.write_string("A4", "Win %")
        sheet.write("B4", villain.win_percentage, self.win_format)
        next(my_progress_track)
        #difficulty data (C-D)
        self.update_difficulty(villain, sheet)
        next(my_progress_track)
        #aspect data (E-F)
        self.update_aspects(villain, sheet)
        next(my_progress_track)
        
        #villain data G,H
        sheet.write_string("G1", f"Heroes Fought - {len(villain.heroes_played)}")
        for i, hero in enumerate(sorted(villain.heroes_played)):
            sheet.write_string(f"G{i+2}", hero)
        next(my_progress_track)

        sheet.write_string("H1", f"Heroes Unplayed - {len(villain.heroes_not_played)}")
        next(my_progress_track)
        for i, hero in enumerate(sorted(villain.heroes_not_played)):
            sheet.write_string(f"H{i+2}", hero)
        next(my_progress_track)
        next(my_progress_track, 0)

    def upload_villains(self, worksheets):
        if(self.diff_data is None):
            villain_list = self.statistics.villain_data.keys()
        else:
            villain_list = list(self.diff_data[0])

        print("Uploading Villain statistics: ")
        for villain in sorted(villain_list):
            if len(villain) > self.max_worksheet_name_length:
                print(f"skipping {villain} due to name too long for worksheet name")
                continue
            skip = False
            if villain not in worksheets:
                print(f"creating {villain} worksheet, not found")
                vsheet = self.sheet.add_worksheet(villain)
            else:
                print(f"found {villain} worksheet, -- ")
                vsheet = self.sheet.get_worksheet_by_name(villain)
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
                
        print("Uploading Big Box statistics: ")
        for big_box in sorted(big_box_list):
            skip = False
            if big_box not in worksheets:
                print(f"creating {big_box} worksheet, not found")
                vsheet = self.sheet.add_worksheet(big_box)
            else:
                print(f"found {big_box} worksheet, -- ")
                vsheet = self.sheet.get_worksheet_by_name(big_box)
                skip = self.skip_found

            if not skip:
                self.update_villain_sheet(self.statistics.big_box_data[big_box], vsheet)

    def upload_scenario_packs(self, worksheets):
        if(self.diff_data is None):
            scenario_pack_list = list(self.statistics.scenario_pack_data.keys())
        else:
            #grab expansion data out of villain
            scenario_pack_list = []
            for villain in list(self.diff_data[0]):
                if self.statistics.villain_data[villain].expansion in self.statistics.scenario_pack_data.keys():
                    scenario_pack_list.append(self.statistics.villain_data[villain].expansion)


        #remove the repeat scenarios that only include one villain (already uploaded when villains uploaded)
        if "Wrecking Crew" in scenario_pack_list:
            scenario_pack_list.remove("Wrecking Crew")
        if "The Hood" in scenario_pack_list:
            scenario_pack_list.remove("The Hood")
        if "Once and Future Kang" in scenario_pack_list:
            scenario_pack_list.remove("Once and Future Kang")
                
        print("Uploading Scenario Pack statistics: ")
        for scenario_pack in sorted(scenario_pack_list):
            skip = False
            if scenario_pack not in worksheets:
                print(f"creating {scenario_pack} worksheet, not found")
                vsheet = self.sheet.add_worksheet(scenario_pack)
            else:
                print(f"found {scenario_pack} worksheet, -- ")
                vsheet = self.sheet.get_worksheet_by_name(scenario_pack)
                skip = self.skip_found

            if not skip:
                self.update_villain_sheet(self.statistics.scenario_pack_data[scenario_pack], vsheet)

    def upload_play_matrix(self):

        #determine maximum amount of entries
        total = 0
        for villain in self.statistics.villain_data.values():
            total += len(villain.heroes_played)

        my_progress_track = track(range(total), "Uploading Play Matrix statistics: ")
        if self.sheet.get_worksheet_by_name("Play Matrix") is None:
            psheet = self.sheet.add_worksheet("Play Matrix")
        else:
            psheet = self.sheet.get_worksheet_by_name("Play Matrix")
        #print the hero names
        heroes = sorted(self.statistics.hero_data.keys())
        for n, hero in enumerate(heroes):
            psheet.write_string(f"A{n+2}", hero, self.bold_format)

        #walk the villains
        villains = sorted(self.statistics.villain_data.keys())
        for column, villain in enumerate(villains):
            #print the name on first row
            psheet.write_string(f"A1", villain, self.bold_format)
            #walk heroes played
            for hero_played in self.statistics.villain_data[villain].heroes_played:
                #see where in the list the hero played is in there
                for index, hero in enumerate(heroes):
                    if hero_played == hero:
                       #found here, print x
                        psheet.write_string(f"{COLUMNS[column]}{index+2}","", self.bg_format)
                        next(my_progress_track)
        next(my_progress_track, 0)
                    

    def upload_overall(self):
        my_progress_track = track(range(10), "Uploading Overall statistics...", show_speed=False)
        osheet = self.sheet.get_worksheet_by_name("Overall")
        if osheet is None:
            osheet = self.sheet.add_worksheet("Overall")
        next(my_progress_track)
        osheet.set_row(0,26, self.bold_format)
        osheet.write_string("A1", "Overall")
        osheet.write_string("A2", "Total Plays")
        osheet.write("B2", self.statistics.overall_data.overall.plays)
        osheet.write_string("A3","Total Wins")
        osheet.write("B3", self.statistics.overall_data.overall.wins)
        osheet.write_string("A4", "Win %")
        osheet.write("B4", self.statistics.overall_data.overall.win_percentage, self.win_format)
        osheet.write_string("A5", "Total True Solo Plays")
        osheet.write("B5", self.statistics.overall_data.overall_true_solo_plays)
        osheet.write_string("A6","Total Multihanded Solo Plays")
        osheet.write("B6", self.statistics.overall_data.overall_solo_plays)
        osheet.write_string("A7","Total Multiplayer Plays")
        osheet.write("B7", self.statistics.overall_data.overall_multi_plays)
        next(my_progress_track)
        #difficulty data (C-D)
        self.update_difficulty(self.statistics.overall_data, osheet)
        next(my_progress_track)
        #aspect data (E-F)
        self.update_aspects(self.statistics.overall_data, osheet)
        next(my_progress_track)

        #team data (G-J)
        osheet.write_string("G1","Team")
        osheet.write_string("H1", "Plays")
        osheet.write_string("I1", "Wins")
        osheet.write_string("J1", "Percentage")
        next(my_progress_track)
        for n, data in enumerate(self.statistics.sorted_team_list):
            osheet.write_string(f"G{n+2}",data[0])
            osheet.write(f"H{n+2}",data[1])
            osheet.write(f"I{n+2}", self.statistics.team_data[data[0]].total_wins)
            osheet.write(f"J{n+2}", self.statistics.team_data[data[0]].win_percentage, self.win_format)
        next(my_progress_track)

        #hero H-Index (K-L)
        osheet.write_string("K1", f"Hero H-Index: {self.statistics.hero_h_index}")
        osheet.write_string("L1", "Plays")
        for n, hero in enumerate(self.statistics.sorted_heroes):
            osheet.write_string(f"K{n+2}", f"{n+1}. {hero[1].name}")
            osheet.write(f"L{n+2}",hero[1].total_plays)
        next(my_progress_track)
        #villain H-Index (M-N)
        osheet.write_string("M1", f"Villain H-Index: {self.statistics.villain_h_index}")
        osheet.write_string("N1", "Plays")
        for n, villain in enumerate(self.statistics.sorted_villains):
            osheet.write_string(f"M{n+2}", f"{n+1}. {villain[1].name}")
            osheet.write(f"N{n+2}", villain[1].total_plays)

        next(my_progress_track)
        #hero win percentage (O-P)
        osheet.write_string("O1","Best Heroes")
        osheet.write_string("P1", " Winning Percent")
        printed_row = 2 #start row
        for hero in self.statistics.sorted_percent_heroes:
            #only upload those with minimum number of plays and opponents
            if(hero[1].total_plays >= 10 and len(hero[1].villains_played) >= math.floor(len(self.statistics.sorted_villains)*.19)):
                osheet.write_string(f"O{printed_row}", f"{printed_row-1}. {hero[1].name}")
                osheet.write(f"P{printed_row}", hero[1].win_percentage, self.win_format)
                printed_row += 1
        next(my_progress_track)

        #villain win percentage (Q-R)
        osheet.write_string("Q1", "Easiest Villains")
        osheet.write_string("R1", "Losing Percent")
        printed_row = 2 #start row
        for villain in self.statistics.sorted_percent_villains:
            #only upload those with minimum number of plays and opponents
            if(villain[1].total_plays >= 10 and len(villain[1].heroes_played) >= math.floor(len(self.statistics.sorted_heroes)*.19)):
                osheet.write_string(f"Q{printed_row}", f"{printed_row-1}. {villain[1].name}")
                osheet.write(f"R{printed_row}", villain[1].win_percentage, self.win_format)
                printed_row += 1

        next(my_progress_track)
        next(my_progress_track, 0)

    def perform_write(self):
        worksheets = [x.title for x in self.sheet.worksheets()]
        self.upload_heroes(worksheets)
        self.upload_villains(worksheets)
        self.upload_teams(worksheets)
        self.upload_big_box_expansions(worksheets)
        self.upload_scenario_packs(worksheets)
        self.upload_overall()
        self.upload_play_matrix()
        self.sheet.close()
        
