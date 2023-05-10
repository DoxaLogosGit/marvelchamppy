import gspread
from time import sleep

THROTTLE_VALUE = 10
class UploadData:
    
    def __init__(self, statistics):
        self.statistics = statistics
        self.sheet = None

        
        
    def login(self):
        gc = gspread.service_account()
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
            sheet.format(f"D{start_row + increment}", {'numberFormat': {'type':'PERCENT', 'pattern': '0%'}})
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
            sheet.update(f"D{start_row + increment}", data.aspect_data.basic_plays)
            increment += 1
            sheet.update(f"E{start_row + increment}", "Basic Wins")
            sheet.update(f"D{start_row + increment}", data.aspect_data.basic_wins)
            increment += 1
            sheet.update(f"E{start_row + increment}", "Basic Win %")
            sheet.format(f"D{start_row + increment}", {'numberFormat': {'type':'PERCENT', 'pattern': '0%'}})
            sheet.update(f"D{start_row + increment}", data.aspect_data.basic_win_percentage)
            increment += 1



    def update_hero_sheet(self, hero, sheet):
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
        sleep(THROTTLE_VALUE)
        #difficulty data (C-D)
        self.update_difficulty(hero, sheet)
        sleep(THROTTLE_VALUE)
        #aspect data (E-F)
        self.update_aspects(hero, sheet)
        sleep(THROTTLE_VALUE)
        
        #villain data G,H,I
        sheet.update("G1", f"Villains Fought - {len(hero.villains_played)}")
        for i, villain in enumerate(hero.villains_played):
            sheet.update(f"G{i+2}", villain)

        sleep(THROTTLE_VALUE)
        sheet.update("H1", f"Villains Defeated - {len(hero.villains_defeated)}")
        for i, villain in enumerate(hero.villains_defeated):
            sheet.update(f"H{i+2}", villain)

        sleep(THROTTLE_VALUE)
        sheet.update("I1", f"Villains Unplayed - {len(hero.villains_not_played)}")
        for i, villain in enumerate(hero.villains_not_played):
            sheet.update(f"I{i+2}", villain)

    def upload_heroes(self, worksheets):
        print(worksheets)
        if "Wolverine" not in worksheets:
            print("creating worksheet, not found")
            hsheet = self.sheet.add_worksheet(title = "Wolverine", rows=100, cols=100)
        else:
            print("found worksheet, -- ")
            hsheet = self.sheet.worksheet("Wolverine")
        
        print(hsheet)
        self.update_hero_sheet(self.statistics.hero_data["Wolverine"], hsheet)
            

    def upload_villains(self, worksheets):
        pass

    def upload_teams(self, worksheets):
        pass

    def perform_upload(self):
        self.login()
        worksheets = [x.title for x in self.sheet.worksheets()]
        self.upload_heroes(worksheets)
        