import gspread

class UploadData:
    
    def __init__(self, statistics):
        self.statistics = statistics
        self.sheet = None

        
        
    def login(self):
        gc = gspread.service_account()
        self.sheet = gc.open("Marvel Champions Data")

    def update_hero_sheet(self, hero, sheet):
        #overall data
        sheet.format("A1:Z1", {'textFormat': {'bold':True}, 'horizontalAlignment': "CENTER"})
        sheet.update("A1", "Overall")
        sheet.update("A2", "Total Plays")
        sheet.update("B2", hero.total_plays)
        sheet.update("A3", "Total Wins")
        sheet.update("B3", hero.total_wins)
        sheet.format("B4", {'numberFormat': {'type':'PERCENT'}})
        sheet.update("A4", "Win %")
        sheet.update("B4", hero.win_percentage)
        #difficulty data (C-D)
        
        #aspect data (E-F)
        
        #villain data G,H,I
        sheet.update("G1", f"Villains Fought - {len(hero.villains_played)}")
        for i, villain in enumerate(hero.villains_played):
            sheet.update(f"G{i+2}", villain)

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
        