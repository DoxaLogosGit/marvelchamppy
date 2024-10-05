import gspread
from time import sleep
from datetime import datetime, timedelta
from config import COLUMNS
import math
from rich.progress import track

class UploadData:


    def __init__(self, statistics, skip_found=False, diff_data=None):
        self.statistics = statistics
        self.sheet = None
        self.skip_found = skip_found
        self.diff_data = diff_data


    def login(self):
        gc = gspread.service_account(http_client=gspread.BackOffHTTPClient)
        self.sheet = gc.open("Marvel Champions Personal Play Data")


    def update_difficulty(self, data, sheet):
        sheet.update([["Difficulty Data"]],"C1")
        start_row = 2
        increment = 0
        if data.difficulty_data.expert1_plays > 0:
            sheet.update([["S1E1 Plays"]],f"C{start_row + increment}")
            sheet.update([[data.difficulty_data.expert1_plays]],f"D{start_row + increment}")
            increment += 1
            sheet.update([["S1E1 Wins"]],f"C{start_row + increment}")
            sheet.update([[data.difficulty_data.expert1_wins]],f"D{start_row + increment}")
            increment += 1
            sheet.update([["S1E1 Win %"]],f"C{start_row + increment}")
            sheet.format( f"D{start_row + increment}", {'numberFormat': {'type':'PERCENT', 'pattern': '0%'}})
            sheet.update([[data.difficulty_data.expert1_win_percentage]],f"D{start_row + increment}")
            increment += 1

        if data.difficulty_data.expert2_plays > 0:
            sheet.update([["S1E2 Plays"]],f"C{start_row + increment}")
            sheet.update([[data.difficulty_data.expert2_plays]],f"D{start_row + increment}")
            increment += 1
            sheet.update([["S1E2 Wins"]],f"C{start_row + increment}")
            sheet.update([[data.difficulty_data.expert2_wins]],f"D{start_row + increment}")
            increment += 1
            sheet.update([["S1E2 Win %"]],f"C{start_row + increment}")
            sheet.format(f"D{start_row + increment}", {'numberFormat': {'type':'PERCENT', 'pattern': '0%'}})
            sheet.update([[data.difficulty_data.expert2_win_percentage]],f"D{start_row + increment}")
            increment += 1

        if data.difficulty_data.expert3_plays > 0:
            sheet.update([["S2E1 Plays"]],f"C{start_row + increment}")
            sheet.update([[data.difficulty_data.expert3_plays]],f"D{start_row + increment}")
            increment += 1
            sheet.update([["S2E1 Wins"]],f"C{start_row + increment}")
            sheet.update([[data.difficulty_data.expert3_wins]],f"D{start_row + increment}")
            increment += 1
            sheet.update([["S2E1 Win %"]],f"C{start_row + increment}")
            sheet.format(f"D{start_row + increment}", {'numberFormat': {'type':'PERCENT', 'pattern': '0%'}})
            sheet.update([[data.difficulty_data.expert3_win_percentage]],f"D{start_row + increment}")
            increment += 1

        if data.difficulty_data.expert4_plays > 0:
            sheet.update([["S2E2 Plays"]],f"C{start_row + increment}")
            sheet.update([[data.difficulty_data.expert4_plays]],f"D{start_row + increment}")
            increment += 1
            sheet.update([["S2E2 Wins"]],f"C{start_row + increment}")
            sheet.update([[data.difficulty_data.expert4_wins]],f"D{start_row + increment}")
            increment += 1
            sheet.update([["S2E2 Win %"]],f"C{start_row + increment}")
            sheet.format(f"D{start_row + increment}", {'numberFormat': {'type':'PERCENT', 'pattern': '0%'}})
            sheet.update([[data.difficulty_data.expert4_win_percentage]],f"D{start_row + increment}")
            increment += 1

        if data.difficulty_data.expert5_plays > 0:
            sheet.update([["S3E1 Plays"]],f"C{start_row + increment}")
            sheet.update([[data.difficulty_data.expert5_plays]],f"D{start_row + increment}")
            increment += 1
            sheet.update([["S3E1 Wins"]],f"C{start_row + increment}")
            sheet.update([[data.difficulty_data.expert5_wins]],f"D{start_row + increment}")
            increment += 1
            sheet.update([["S3E1 Win %"]],f"C{start_row + increment}")
            sheet.format(f"D{start_row + increment}", {'numberFormat': {'type':'PERCENT', 'pattern': '0%'}})
            sheet.update([[data.difficulty_data.expert5_win_percentage]],f"D{start_row + increment}")
            increment += 1

        if data.difficulty_data.expert6_plays > 0:
            sheet.update([["S3E2 Plays"]],f"C{start_row + increment}")
            sheet.update([[data.difficulty_data.expert6_plays]],f"D{start_row + increment}")
            increment += 1
            sheet.update([["S3E2 Wins"]],f"C{start_row + increment}")
            sheet.update([[data.difficulty_data.expert6_wins]],f"D{start_row + increment}")
            increment += 1
            sheet.update([["S3E2 Win %"]],f"C{start_row + increment}")
            sheet.format(f"D{start_row + increment}", {'numberFormat': {'type':'PERCENT', 'pattern': '0%'}})
            sheet.update([[data.difficulty_data.expert6_win_percentage]],f"D{start_row + increment}")
            increment += 1

        if data.difficulty_data.standard1_plays > 0:
            sheet.update([["S1 Plays"]],f"C{start_row + increment}")
            sheet.update([[data.difficulty_data.standard1_plays]],f"D{start_row + increment}")
            increment += 1
            sheet.update([["S1 Wins"]],f"C{start_row + increment}")
            sheet.update([[data.difficulty_data.standard1_wins]],f"D{start_row + increment}")
            increment += 1
            sheet.update([["S1 Win %"]],f"C{start_row + increment}")
            sheet.format(f"D{start_row + increment}", {'numberFormat': {'type':'PERCENT', 'pattern': '0%'}})
            sheet.update([[data.difficulty_data.standard1_win_percentage]],f"D{start_row + increment}")
            increment += 1

        if data.difficulty_data.standard2_plays > 0:
            sheet.update([["S2 Plays"]],f"C{start_row + increment}")
            sheet.update([[data.difficulty_data.standard2_plays]],f"D{start_row + increment}")
            increment += 1
            sheet.update([["S2 Wins"]],f"C{start_row + increment}")
            sheet.update([[data.difficulty_data.standard2_wins]],f"D{start_row + increment}")
            increment += 1
            sheet.update([["S2 Win %"]],f"C{start_row + increment}")
            sheet.format(f"D{start_row + increment}", {'numberFormat': {'type':'PERCENT', 'pattern': '0%'}})
            sheet.update([[data.difficulty_data.standard2_win_percentage]],f"D{start_row + increment}")
            increment += 1

        if data.difficulty_data.standard3_plays > 0:
            sheet.update([["S3 Plays"]],f"C{start_row + increment}")
            sheet.update([[data.difficulty_data.standard3_plays]],f"D{start_row + increment}")
            increment += 1
            sheet.update([[ "S3 Wins"]],f"C{start_row + increment}")
            sheet.update([[data.difficulty_data.standard3_wins]],f"D{start_row + increment}")
            increment += 1
            sheet.update([["S3 Win %"]],f"C{start_row + increment}")
            sheet.format(f"D{start_row + increment}", {'numberFormat': {'type':'PERCENT', 'pattern': '0%'}})
            sheet.update([[data.difficulty_data.standard3_win_percentage]],f"D{start_row + increment}")
            increment += 1

        if data.difficulty_data.heroic_plays > 0:
            sheet.update([["Heroic Plays"]],f"C{start_row + increment}")
            sheet.update([[data.difficulty_data.heroic_plays]],f"D{start_row + increment}")
            increment += 1
            sheet.update([["Heroic Wins"]],f"C{start_row + increment}")
            sheet.update([[data.difficulty_data.heroic_wins]],f"D{start_row + increment}")
            increment += 1
            sheet.update([["Heroic Win %"]],f"C{start_row + increment}")
            sheet.format(f"D{start_row + increment}", {'numberFormat': {'type':'PERCENT', 'pattern': '0%'}})
            sheet.update([[data.difficulty_data.heroic_win_percentage]],f"D{start_row + increment}")
            increment += 1


    def update_aspects(self, data, sheet):
        sheet.update([["Aspect Data"]],"E1")
        start_row = 2
        increment = 0
        for aspect in data.aspect_data.aspect_plays.keys():
            if data.aspect_data.aspect_plays[aspect].plays > 0:
                sheet.update([[f"{aspect} Plays"]],f"E{start_row + increment}")
                sheet.update([[data.aspect_data.aspect_plays[aspect].plays]],f"F{start_row + increment}")
                increment += 1
                sheet.update([[f"{aspect} Wins"]],f"E{start_row + increment}")
                sheet.update([[data.aspect_data.aspect_plays[aspect].wins]],f"F{start_row + increment}")
                increment += 1
                sheet.update([[f"{aspect} Win %"]],f"E{start_row + increment}")
                sheet.format(f"F{start_row + increment}", {'numberFormat': {'type':'PERCENT', 'pattern': '0%'}})
                sheet.update([[data.aspect_data.aspect_plays[aspect].win_percentage]],f"F{start_row + increment}")
                increment += 1


    

    def update_hero_sheet(self, hero, sheet):
        my_progress_track = track(range(7), f"Uploading {hero.name} statistics: ")
        #clear the sheet
        sheet.batch_clear(["A1:Z100"])
        next(my_progress_track)
        #overall data
        sheet.format("A1:Z1", {'textFormat': {'bold':True}, 'horizontalAlignment': "CENTER"})
        sheet.update([["Overall"]],"A1")
        sheet.update([["Total Plays"]],"A2")
        sheet.update([[hero.total_plays]],"B2")
        sheet.update([["Total Wins"]],"A3")
        sheet.update([[ hero.total_wins]],"B3")
        sheet.format("B4", {'numberFormat': {'type':'PERCENT', 'pattern': '0%'}})
        sheet.update([["Win %"]],"A4")
        sheet.update([[hero.win_percentage]],"B4")
        next(my_progress_track)
        #difficulty data (C-D)
        self.update_difficulty(hero, sheet)
        next(my_progress_track)
        #aspect data (E-F)
        self.update_aspects(hero, sheet)
        next(my_progress_track)
        
        #villain data G,H,I
        sheet.update([[f"Villains Fought - {len(hero.villains_played)}"]],"G1")
        for i, villain in enumerate(sorted(hero.villains_played)):
            sheet.update([[villain]],f"G{i+2}")
        next(my_progress_track)

        sheet.update([[f"Villains Not Defeated - {len(hero.villains_not_defeated)}"]],"H1")
        for i, villain in enumerate(sorted(hero.villains_not_defeated)):
            sheet.update([[villain]],f"H{i+2}")
        next(my_progress_track)

        sheet.update([[f"Villains Unplayed - {len(hero.villains_not_played)}"]],"I1")
        for i, villain in enumerate(sorted(hero.villains_not_played)):
            sheet.update([[villain]],f"I{i+2}")
        next(my_progress_track)
        next(my_progress_track, 0)

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
        my_progress_track = track(range(7), f"Uploading {villain.name} statistics: ")
        #clear sheet
        sheet.batch_clear(["A1:Z100"])
        next(my_progress_track)
        #overall data
        sheet.format("A1:Z1", {'textFormat': {'bold':True}, 'horizontalAlignment': "CENTER"})
        sheet.update([["Overall"]],"A1")
        sheet.update([["Total Plays"]],"A2")
        sheet.update([[villain.total_plays]],"B2")
        sheet.update([["Total Wins"]],"A3")
        sheet.update([[villain.total_wins]],"B3")
        sheet.format("B4", {'numberFormat': {'type':'PERCENT', 'pattern': '0%'}})
        sheet.update([[ "Win %"]],"A4")
        sheet.update([[villain.win_percentage]],"B4")
        next(my_progress_track)
        #difficulty data (C-D)
        self.update_difficulty(villain, sheet)
        next(my_progress_track)
        #aspect data (E-F)
        self.update_aspects(villain, sheet)
        next(my_progress_track)
        
        #villain data G,H
        sheet.update([[f"Heroes Fought - {len(villain.heroes_played)}"]],"G1")
        for i, hero in enumerate(sorted(villain.heroes_played)):
            sheet.update([[hero]],f"G{i+2}")
        next(my_progress_track)

        #clear the unplayed before publishing unplayed (the list will shrink over time)
        vrange = f"H1:H{len(villain.heroes_played)+len(villain.heroes_not_played)+3}"
        sheet.batch_clear([vrange])
        sheet.update([[f"Heroes Unplayed - {len(villain.heroes_not_played)}"]],"H1")
        next(my_progress_track)
        for i, hero in enumerate(sorted(villain.heroes_not_played)):
            sheet.update([[hero]],f"H{i+2}")
        next(my_progress_track)
        next(my_progress_track, 0)

    def upload_villains(self, worksheets):
        if(self.diff_data is None):
            villain_list = self.statistics.villain_data.keys()
        else:
            villain_list = list(self.diff_data[0])

        print("Uploading Villain statistics: ")
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
                
        print("Uploading Big Box statistics: ")
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
                vsheet = self.sheet.add_worksheet(title = scenario_pack, rows=100, cols=100)
            else:
                print(f"found {scenario_pack} worksheet, -- ")
                vsheet = self.sheet.worksheet(scenario_pack)
                skip = self.skip_found

            if not skip:
                self.update_villain_sheet(self.statistics.scenario_pack_data[scenario_pack], vsheet)

    def upload_play_matrix(self):

        #determine maximum amount of entries
        total = 0
        for villain in self.statistics.villain_data.values():
            total += len(villain.heroes_played)

        my_progress_track = track(range(total), "Uploading Play Matrix statistics: ")
        psheet = self.sheet.worksheet("Play Matrix")
        #clear sheet
        psheet.batch_clear(["A1:ZZ200"])
        psheet.format("B2:ZZ200", {'textFormat': {'bold':True}, 'horizontalAlignment': "CENTER"})
        #print the hero names
        heroes = sorted(self.statistics.hero_data.keys())
        for n, hero in enumerate(heroes):
            psheet.update([[f"{hero}"]],f"A{n+2}")

        #walk the villains
        villains = sorted(self.statistics.villain_data.keys())
        for column, villain in enumerate(villains):
            #print the name on first row
            psheet.update([[f"{villain}"]],f"{COLUMNS[column]}1")
            #walk heroes played
            for hero_played in self.statistics.villain_data[villain].heroes_played:
                #see where in the list the hero played is in there
                for index, hero in enumerate(heroes):
                    if hero_played == hero:
                       #found here, print x
                        psheet.format(f"{COLUMNS[column]}{index+2}", {"backgroundColor": {
                                                                       "red": 0.0,
                                                                       "green": 0.0,
                                                                       "blue": 0.0
                        }})
                        next(my_progress_track)
        next(my_progress_track, 0)
                    
                            
                        



    def upload_overall(self):
        my_progress_track = track(range(10), "Uploading Overall statistics...", show_speed=False)
        osheet = self.sheet.worksheet("Overall")
        #clear sheet
        osheet.batch_clear(["A1:Z100"])
        next(my_progress_track)
        osheet.format("A1:Z1", {'textFormat': {'bold':True}, 'horizontalAlignment': "CENTER"})
        osheet.update([["Overall"]], "A1")
        osheet.update([["Total Plays"]], "A2")
        osheet.update([[self.statistics.overall_data.overall.plays]], "B2")
        osheet.update([["Total Wins"]], "A3")
        osheet.update([[self.statistics.overall_data.overall.wins]], "B3")
        osheet.format("B4", {'numberFormat': {'type':'PERCENT', 'pattern': '0%'}})
        osheet.update([["Win %"]], "A4")
        osheet.update([[self.statistics.overall_data.overall.win_percentage]], "B4")
        osheet.update([["Total True Solo Plays"]],"A5")
        osheet.update([[self.statistics.overall_data.overall_true_solo_plays]],"B5")
        osheet.update([["Total Multihanded Solo Plays"]],"A6")
        osheet.update([[self.statistics.overall_data.overall_solo_plays]],"B6")
        osheet.update([["Total Multiplayer Plays"]],"A7")
        osheet.update([[self.statistics.overall_data.overall_multi_plays]],"B7")
        next(my_progress_track)
        #difficulty data (C-D)
        self.update_difficulty(self.statistics.overall_data, osheet)
        next(my_progress_track)
        #aspect data (E-F)
        self.update_aspects(self.statistics.overall_data, osheet)
        next(my_progress_track)

        #team data (G-J)
        osheet.update([["Team"]],"G1")
        osheet.update([["Plays"]],"H1")
        osheet.update([["Wins"]],"I1")
        osheet.update([["Percentage"]],"J1")
        next(my_progress_track)
        for n, data in enumerate(self.statistics.sorted_team_list):
            osheet.update([[data[0]]],f"G{n+2}")
            osheet.update([[data[1]]],f"H{n+2}")
            osheet.update([[self.statistics.team_data[data[0]].total_wins]],f"I{n+2}")
            osheet.format(f"J{n+2}", {'numberFormat': {'type':'PERCENT', 'pattern': '0%'}})
            osheet.update([[self.statistics.team_data[data[0]].win_percentage]],f"J{n+2}")
        next(my_progress_track)

        #hero H-Index (K-L)
        osheet.update([[f"Hero H-Index: {self.statistics.hero_h_index}"]],"K1")
        osheet.update([["Plays"]],"L1")
        for n, hero in enumerate(self.statistics.sorted_heroes):
            osheet.update([[f"{n+1}. {hero[1].name}"]],f"K{n+2}")
            osheet.update([[hero[1].total_plays]],f"L{n+2}")
        next(my_progress_track)
        #villain H-Index (M-N)
        osheet.update([[f"Villain H-Index: {self.statistics.villain_h_index}"]],"M1")
        osheet.update([["Plays"]],"N1")
        for n, villain in enumerate(self.statistics.sorted_villains):
            osheet.update([[ f"{n+1}. {villain[1].name}"]],f"M{n+2}")
            osheet.update([[villain[1].total_plays]],f"N{n+2}")

        next(my_progress_track)
        #hero win percentage (O-P)
        osheet.update([["Best Heroes"]],"O1")
        osheet.update([[" Winning Percent"]],"P1")
        printed_row = 2 #start row
        for hero in self.statistics.sorted_percent_heroes:
            #only upload those with minimum number of plays and opponents
            if(hero[1].total_plays >= 10 and len(hero[1].villains_played) >= math.floor(len(self.statistics.sorted_villains)*.19)):
                osheet.update([[f"{printed_row-1}. {hero[1].name}"]],f"O{printed_row}")
                osheet.format(f"P{printed_row}", {'numberFormat': {'type':'PERCENT', 'pattern': '0%'}})
                osheet.update([[hero[1].win_percentage]],f"P{printed_row}")
                printed_row += 1
        next(my_progress_track)

        #villain win percentage (Q-R)
        osheet.update([["Easiest Villains"]],"Q1")
        osheet.update([["Losing Percent"]],"R1")
        printed_row = 2 #start row
        for villain in self.statistics.sorted_percent_villains:
            #only upload those with minimum number of plays and opponents
            if(villain[1].total_plays >= 10 and len(villain[1].heroes_played) >= math.floor(len(self.statistics.sorted_heroes)*.19)):
                osheet.update([[f"{printed_row-1}. {villain[1].name}"]],f"Q{printed_row}")
                osheet.format(f"R{printed_row}", {'numberFormat': {'type':'PERCENT', 'pattern': '0%'}})
                osheet.update([[villain[1].win_percentage]],f"R{printed_row}")
                printed_row += 1

        next(my_progress_track)
        next(my_progress_track, 0)

    def perform_upload(self):
        self.login()
        self.upload_overall()
        worksheets = [x.title for x in self.sheet.worksheets()]
        sleep(5)
        self.upload_heroes(worksheets)
        sleep(30)
        self.upload_villains(worksheets)
        sleep(30)
        self.upload_teams(worksheets)
        sleep(30)
        self.upload_big_box_expansions(worksheets)
        sleep(30)
        self.upload_scenario_packs(worksheets)
        sleep(30)
        self.upload_play_matrix()
        
