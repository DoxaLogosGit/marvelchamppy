import gspread
from time import sleep
from datetime import datetime, timedelta

REQUESTS_LIMIT = 60
THROTTLE_VALUE = 10
class UploadData:

    num_requests = 0
    start_time = datetime.now()

    
    def __init__(self, statistics):
        self.statistics = statistics
        self.sheet = None

    #@staticmethod
    def check_request_time(cls):
        cls.num_requests += 1
        if(cls.num_requests == REQUESTS_LIMIT):
            print(cls.num_requests)
            delta_time = datetime.now() - cls.start_time
            wait_time = 61 - delta_time.total_seconds()
            print(f"Hit request limit, waiting {wait_time} seconds")
            sleep(wait_time)
            cls.num_requests = 0
            cls.start_time = datetime.now()
        
    def throttle_update(self, sheet, *args):
        """ Special function to throttle updates requests

        Args:
            data (cell data): _description_
            sheet (worksheet): _description_
        """
            
        self.check_request_time()
        sheet.update(*args)

    def throttle_format(self, sheet, *args):
        """ Special function to throttle format requests

        Args:
            data (cell data): _description_
            sheet (worksheet): _description_
        """
        self.check_request_time()
        sheet.format(*args)
        
    def login(self):
        gc = gspread.service_account()
        self.sheet = gc.open("Marvel Champions Data")

        
    def update_difficulty(self, data, sheet):
        self.throttle_update(sheet,"C1", "Difficulty Data")
        start_row = 2
        increment = 0
        if data.difficulty_data.expert1_plays > 0:
            self.throttle_update(sheet,f"C{start_row + increment}", "S1E1 Plays")
            self.throttle_update(sheet,f"D{start_row + increment}", data.difficulty_data.expert1_plays)
            increment += 1
            self.throttle_update(sheet,f"C{start_row + increment}", "S1E1 Wins")
            self.throttle_update(sheet,f"D{start_row + increment}", data.difficulty_data.expert1_wins)
            increment += 1
            self.throttle_update(sheet,f"C{start_row + increment}", "S1E1 Win %")
            self.throttle_format(sheet, f"D{start_row + increment}", {'numberFormat': {'type':'PERCENT', 'pattern': '0%'}})
            self.throttle_update(sheet,f"D{start_row + increment}", data.difficulty_data.expert1_win_percentage)
            increment += 1

        if data.difficulty_data.expert2_plays > 0:
            self.throttle_update(sheet,f"C{start_row + increment}", "S1E2 Plays")
            self.throttle_update(sheet,f"D{start_row + increment}", data.difficulty_data.expert2_plays)
            increment += 1
            self.throttle_update(sheet,f"C{start_row + increment}", "S1E2 Wins")
            self.throttle_update(sheet,f"D{start_row + increment}", data.difficulty_data.expert2_wins)
            increment += 1
            self.throttle_update(sheet,f"C{start_row + increment}", "S1E2 Win %")
            self.throttle_format(sheet,f"D{start_row + increment}", {'numberFormat': {'type':'PERCENT', 'pattern': '0%'}})
            self.throttle_update(sheet,f"D{start_row + increment}", data.difficulty_data.expert2_win_percentage)
            increment += 1

        if data.difficulty_data.expert3_plays > 0:
            self.throttle_update(sheet,f"C{start_row + increment}", "S2E1 Plays")
            self.throttle_update(sheet,f"D{start_row + increment}", data.difficulty_data.expert3_plays)
            increment += 1
            self.throttle_update(sheet,f"C{start_row + increment}", "S2E1 Wins")
            self.throttle_update(sheet,f"D{start_row + increment}", data.difficulty_data.expert3_wins)
            increment += 1
            self.throttle_update(sheet,f"C{start_row + increment}", "S2E1 Win %")
            self.throttle_format(sheet,f"D{start_row + increment}", {'numberFormat': {'type':'PERCENT', 'pattern': '0%'}})
            self.throttle_update(sheet,f"D{start_row + increment}", data.difficulty_data.expert3_win_percentage)
            increment += 1

        if data.difficulty_data.expert4_plays > 0:
            self.throttle_update(sheet,f"C{start_row + increment}", "S2E2 Plays")
            self.throttle_update(sheet,f"D{start_row + increment}", data.difficulty_data.expert4_plays)
            increment += 1
            self.throttle_update(sheet,f"C{start_row + increment}", "S2E2 Wins")
            self.throttle_update(sheet,f"D{start_row + increment}", data.difficulty_data.expert4_wins)
            increment += 1
            self.throttle_update(sheet,f"C{start_row + increment}", "S2E2 Win %")
            self.throttle_format(sheet,f"D{start_row + increment}", {'numberFormat': {'type':'PERCENT', 'pattern': '0%'}})
            self.throttle_update(sheet,f"D{start_row + increment}", data.difficulty_data.expert4_win_percentage)
            increment += 1

        if data.difficulty_data.standard1_plays > 0:
            self.throttle_update(sheet,f"C{start_row + increment}", "S1 Plays")
            self.throttle_update(sheet,f"D{start_row + increment}", data.difficulty_data.standard1_plays)
            increment += 1
            self.throttle_update(sheet,f"C{start_row + increment}", "S1 Wins")
            self.throttle_update(sheet,f"D{start_row + increment}", data.difficulty_data.standard1_wins)
            increment += 1
            self.throttle_update(sheet,f"C{start_row + increment}", "S1 Win %")
            self.throttle_format(sheet,f"D{start_row + increment}", {'numberFormat': {'type':'PERCENT', 'pattern': '0%'}})
            self.throttle_update(sheet,f"D{start_row + increment}", data.difficulty_data.standard1_win_percentage)
            increment += 1

        if data.difficulty_data.standard2_plays > 0:
            self.throttle_update(sheet,f"C{start_row + increment}", "S2 Plays")
            self.throttle_update(sheet,f"D{start_row + increment}", data.difficulty_data.standard2_plays)
            increment += 1
            self.throttle_update(sheet,f"C{start_row + increment}", "S2 Wins")
            self.throttle_update(sheet,f"D{start_row + increment}", data.difficulty_data.standard2_wins)
            increment += 1
            self.throttle_update(sheet,f"C{start_row + increment}", "S2 Win %")
            self.throttle_format(sheet,f"D{start_row + increment}", {'numberFormat': {'type':'PERCENT', 'pattern': '0%'}})
            self.throttle_update(sheet,f"D{start_row + increment}", data.difficulty_data.standard2_win_percentage)
            increment += 1

        if data.difficulty_data.heroic_plays > 0:
            self.throttle_update(sheet,f"C{start_row + increment}", "Heroic Plays")
            self.throttle_update(sheet,f"D{start_row + increment}", data.difficulty_data.heroic_plays)
            increment += 1
            self.throttle_update(sheet,f"C{start_row + increment}", "Heroic Wins")
            self.throttle_update(sheet,f"D{start_row + increment}", data.difficulty_data.heroic_wins)
            increment += 1
            self.throttle_update(sheet,f"C{start_row + increment}", "Heroic Win %")
            self.throttle_format(sheet,f"D{start_row + increment}", {'numberFormat': {'type':'PERCENT', 'pattern': '0%'}})
            self.throttle_update(sheet,f"D{start_row + increment}", data.difficulty_data.heroic_win_percentage)
            increment += 1


    def update_aspects(self, data, sheet):
        self.throttle_update(sheet,"E1", "Aspect Data")
        start_row = 2
        increment = 0
        if data.aspect_data.leadership_plays > 0:
            self.throttle_update(sheet,f"E{start_row + increment}", "Leadership Plays")
            self.throttle_update(sheet,f"F{start_row + increment}", data.aspect_data.leadership_plays)
            increment += 1
            self.throttle_update(sheet,f"E{start_row + increment}", "Leadership Wins")
            self.throttle_update(sheet,f"F{start_row + increment}", data.aspect_data.leadership_wins)
            increment += 1
            self.throttle_update(sheet,f"E{start_row + increment}", "Leadership Win %")
            self.throttle_format(sheet,f"F{start_row + increment}", {'numberFormat': {'type':'PERCENT', 'pattern': '0%'}})
            self.throttle_update(sheet,f"F{start_row + increment}", data.aspect_data.leadership_win_percentage)
            increment += 1
        if data.aspect_data.aggression_plays > 0:
            self.throttle_update(sheet,f"E{start_row + increment}", "Aggression Plays")
            self.throttle_update(sheet,f"F{start_row + increment}", data.aspect_data.aggression_plays)
            increment += 1
            self.throttle_update(sheet,f"E{start_row + increment}", "Aggression Wins")
            self.throttle_update(sheet,f"F{start_row + increment}", data.aspect_data.aggression_wins)
            increment += 1
            self.throttle_update(sheet,f"E{start_row + increment}", "Aggression Win %")
            self.throttle_format(sheet,f"F{start_row + increment}", {'numberFormat': {'type':'PERCENT', 'pattern': '0%'}})
            self.throttle_update(sheet,f"F{start_row + increment}", data.aspect_data.aggression_win_percentage)
            increment += 1
        if data.aspect_data.justice_plays > 0:
            self.throttle_update(sheet,f"E{start_row + increment}", "Justice Plays")
            self.throttle_update(sheet,f"F{start_row + increment}", data.aspect_data.justice_plays)
            increment += 1
            self.throttle_update(sheet,f"E{start_row + increment}", "Justice Wins")
            self.throttle_update(sheet,f"F{start_row + increment}", data.aspect_data.justice_wins)
            increment += 1
            self.throttle_update(sheet,f"E{start_row + increment}", "Justice Win %")
            self.throttle_format(sheet,f"F{start_row + increment}", {'numberFormat': {'type':'PERCENT', 'pattern': '0%'}})
            self.throttle_update(sheet,f"F{start_row + increment}", data.aspect_data.justice_win_percentage)
            increment += 1

        if data.aspect_data.protection_plays > 0:
            self.throttle_update(sheet,f"E{start_row + increment}", "Protection Plays")
            self.throttle_update(sheet,f"F{start_row + increment}", data.aspect_data.protection_plays)
            increment += 1
            self.throttle_update(sheet,f"E{start_row + increment}", "Protection Wins")
            self.throttle_update(sheet,f"F{start_row + increment}", data.aspect_data.protection_wins)
            increment += 1
            self.throttle_update(sheet,f"E{start_row + increment}", "Protection Win %")
            self.throttle_format(sheet,f"F{start_row + increment}", {'numberFormat': {'type':'PERCENT', 'pattern': '0%'}})
            self.throttle_update(sheet,f"F{start_row + increment}", data.aspect_data.protection_win_percentage)
            increment += 1

        if data.aspect_data.basic_plays > 0:
            self.throttle_update(sheet,f"E{start_row + increment}", "Basic Plays")
            self.throttle_update(sheet,f"D{start_row + increment}", data.aspect_data.basic_plays)
            increment += 1
            self.throttle_update(sheet,f"E{start_row + increment}", "Basic Wins")
            self.throttle_update(sheet,f"D{start_row + increment}", data.aspect_data.basic_wins)
            increment += 1
            self.throttle_update(sheet,f"E{start_row + increment}", "Basic Win %")
            self.throttle_format(sheet,f"D{start_row + increment}", {'numberFormat': {'type':'PERCENT', 'pattern': '0%'}})
            self.throttle_update(sheet,f"D{start_row + increment}", data.aspect_data.basic_win_percentage)
            increment += 1


    

    def update_hero_sheet(self, hero, sheet):
        #overall data
        self.throttle_format(sheet,"A1:Z1", {'textFormat': {'bold':True}, 'horizontalAlignment': "CENTER"})
        self.throttle_update(sheet,"A1", "Overall")
        self.throttle_update(sheet,"A2", "Total Plays")
        self.throttle_update(sheet,"B2", hero.total_plays)
        self.throttle_update(sheet,"A3", "Total Wins")
        self.throttle_update(sheet,"B3", hero.total_wins)
        self.throttle_format(sheet,"B4", {'numberFormat': {'type':'PERCENT', 'pattern': '0%'}})
        self.throttle_update(sheet,"A4", "Win %")
        self.throttle_update(sheet,"B4", hero.win_percentage)
        #sleep(THROTTLE_VALUE)
        #difficulty data (C-D)
        self.update_difficulty(hero, sheet)
        #sleep(THROTTLE_VALUE)
        #aspect data (E-F)
        self.update_aspects(hero, sheet)
        #sleep(THROTTLE_VALUE)
        
        #villain data G,H,I
        self.throttle_update(sheet,"G1", f"Villains Fought - {len(hero.villains_played)}")
        for i, villain in enumerate(hero.villains_played):
            self.throttle_update(sheet,f"G{i+2}", villain)

        #sleep(THROTTLE_VALUE)
        self.throttle_update(sheet,"H1", f"Villains Defeated - {len(hero.villains_defeated)}")
        for i, villain in enumerate(hero.villains_defeated):
            self.throttle_update(sheet,f"H{i+2}", villain)

        #sleep(THROTTLE_VALUE)
        self.throttle_update(sheet,"I1", f"Villains Unplayed - {len(hero.villains_not_played)}")
        for i, villain in enumerate(hero.villains_not_played):
            self.throttle_update(sheet,f"I{i+2}", villain)

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
        