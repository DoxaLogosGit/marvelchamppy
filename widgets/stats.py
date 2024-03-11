from textual.app import ComposeResult
from textual.containers import Widget
from textual.reactive import reactive
from textual.widgets import DataTable, Static
from analyze_data import AspectData, DifficultyStats
from rich.text import Text


class SpecialPlays(Static):
    solo_plays: reactive[int] = reactive(0)
    multiplayer_plays: reactive[int] = reactive(0)
    multihanded_solo_plays: reactive[int] = reactive(0)
    c1 = None
    ct = None
    rs = None
    rmp = None
    rmsp = None

    def compose(self) -> ComposeResult:
        yield DataTable(id = "special_play_table", show_cursor=False)

    def on_mount(self) -> None:
        table = self.query_one("#special_play_table")
        self.c1 = table.add_column("Special Plays:")
        self.ct = table.add_column("      ")
        self.rmp = table.add_row("Mutiplayer  Plays", self.multiplayer_plays)
        self.rmsp = table.add_row("Multi-Handed Solo Plays", self.multihanded_solo_plays)
        self.rs = table.add_row("True Solo Plays", self.solo_plays)

    def watch_solo_plays(self, old_solo_plays, new_solo_plays):
        self.solo_plays = new_solo_plays
        table = self.query_one("#special_play_table", DataTable)
        if self.rs is not None:
            table.update_cell(self.rs,self.ct, self.solo_plays)

    def watch_multiplayer_plays(self, old_multiplayer_plays, new_multiplayer_plays):
        self.multiplayer_plays = new_multiplayer_plays
        table = self.query_one("#special_play_table", DataTable)
        if self.rmp is not None:
            table.update_cell(self.rmp,self.ct, self.multiplayer_plays)

    def watch_multihanded_solo_plays(self, old_multihanded_solo_plays, new_multihanded_solo_plays):
        self.multihanded_solo_plays = new_multihanded_solo_plays
        table = self.query_one("#special_play_table", DataTable)
        if self.rmsp is not None:
            table.update_cell(self.rmsp,self.ct, self.multihanded_solo_plays)


class TotalStats(Static):
    total_plays: reactive[int] = reactive(0)
    total_wins: reactive[int] = reactive(0)
    total_win_percentage: reactive[float] = reactive(0)
    c1 = None
    ct = None
    rp = None
    rw = None
    rwp = None

    def compose(self) -> ComposeResult:
        yield DataTable(id = "total_data_table", show_cursor=False)

    def on_mount(self) -> None:
        table = self.query_one("#total_data_table")
        self.c1 = table.add_column("Total Data:")
        self.ct = table.add_column("      ")
        self.rp = table.add_row("Plays", self.total_plays)
        self.rw = table.add_row("Wins", self.total_wins)
        self.rwp = table.add_row("Win %", round(self.total_win_percentage * 100))

    def watch_total_plays(self, old_total_plays, new_total_plays):
        self.total_plays = new_total_plays
        table = self.query_one("#total_data_table", DataTable)
        if self.rp is not None:
            table.update_cell(self.rp,self.ct, self.total_plays)

    def watch_total_wins(self, old_total_wins, new_total_wins):
        self.total_wins = new_total_wins
        table = self.query_one("#total_data_table", DataTable)
        if self.rw is not None:
            table.update_cell(self.rw,self.ct, self.total_wins)

    def watch_total_win_percentage(self, old_total_win_percentage, new_total_win_percentage):
        self.total_win_percentage = new_total_win_percentage
        table = self.query_one("#total_data_table", DataTable)
        if self.rwp is not None:
            table.update_cell(self.rwp,self.ct, round(self.total_win_percentage * 100))

class AspectStats(Static):
    aspect_data: reactive[AspectData] = reactive(AspectData())
    c1 = None 
    cl  = None
    cj  = None
    ca  = None
    cp  = None
    cb  = None
    rp = None
    rw = None
    rwp = None

    def compose(self) -> ComposeResult:
        yield DataTable(id = "aspect_data_table", show_cursor=False)
    
    def on_mount(self) -> None:
        table = self.query_one("#aspect_data_table")
        self.c1 = table.add_column("Aspect Data:")
        self.cl = table.add_column(Text("Leadership", style="bold navy_blue", justify='right'))
        #self.cj = table.add_column("Justice")
        self.cj = table.add_column(Text("Justice",style="bold yellow1", justify='right'))
        self.ca = table.add_column(Text("Agression", style="bold bright_red", justify='right'))
        self.cp = table.add_column(Text("Protection", style="bold green3", justify='right'))
        self.cb = table.add_column(Text("Basic", style="bold grey54", justify='right'))
        self.rp = table.add_row("Plays", self.aspect_data.aspect_plays["Leadership"].plays,
                      self.aspect_data.aspect_plays["Justice"].plays,
                      self.aspect_data.aspect_plays["Aggression"].plays,
                      self.aspect_data.aspect_plays["Protection"].plays,
                      self.aspect_data.aspect_plays["Basic"].plays)
        self.rw = table.add_row("Wins", self.aspect_data.aspect_plays["Leadership"].wins,
                      self.aspect_data.aspect_plays["Justice"].wins,
                      self.aspect_data.aspect_plays["Aggression"].wins,
                      self.aspect_data.aspect_plays["Protection"].wins,
                      self.aspect_data.aspect_plays["Basic"].wins)
        self.rwp = table.add_row("Win %", round(self.aspect_data.aspect_plays["Leadership"].win_percentage * 100),
                      round(self.aspect_data.aspect_plays["Justice"].win_percentage * 100),
                      round(self.aspect_data.aspect_plays["Aggression"].win_percentage * 100),
                      round(self.aspect_data.aspect_plays["Protection"].win_percentage * 100),
                      round(self.aspect_data.aspect_plays["Basic"].win_percentage * 100))

    def watch_aspect_data(self, old_aspect_data: AspectData, new_aspect_data: AspectData):
        self.aspect_data = new_aspect_data
        table = self.query_one("#aspect_data_table", DataTable)
        if self.rp is not None:
            table.update_cell(self.rp,self.cl, Text(str(self.aspect_data.aspect_plays["Leadership"].plays), style="bold bright_blue", justify='right'))
            table.update_cell(self.rp,self.ca, Text(str(self.aspect_data.aspect_plays["Aggression"].plays), style="bold bright_red", justify='right'))
            table.update_cell(self.rp,self.cb, Text(str(self.aspect_data.aspect_plays["Basic"].plays), style="bold grey50", justify='right'))
            table.update_cell(self.rp,self.cj, Text(str(self.aspect_data.aspect_plays["Justice"].plays),style="bold yellow1", justify='right'))
            table.update_cell(self.rp,self.cp, Text(str(self.aspect_data.aspect_plays["Protection"].plays), style="bold green3", justify='right'))
        if self.rw is not None:
            table.update_cell(self.rw,self.cl, Text(str(self.aspect_data.aspect_plays["Leadership"].wins), style="bold bright_blue", justify='right'))
            table.update_cell(self.rw,self.ca, Text(str(self.aspect_data.aspect_plays["Aggression"].wins),  style="bold bright_red",justify='right'))
            table.update_cell(self.rw,self.cb, Text(str(self.aspect_data.aspect_plays["Basic"].wins), style="bold grey50", justify='right'))
            table.update_cell(self.rw,self.cj, Text(str(self.aspect_data.aspect_plays["Justice"].wins), style="bold yellow1", justify='right'))
            table.update_cell(self.rw,self.cp, Text(str(self.aspect_data.aspect_plays["Protection"].wins), style="bold green3", justify='right'))
        if self.rwp is not None:
            table.update_cell(self.rwp,self.cl, Text(str(round(self.aspect_data.aspect_plays["Leadership"].win_percentage * 100)), style="bold bright_blue", justify='right'))
            table.update_cell(self.rwp,self.ca, Text(str(round(self.aspect_data.aspect_plays["Aggression"].win_percentage * 100)), style="bold bright_red", justify='right'))
            table.update_cell(self.rwp,self.cb, Text(str(round(self.aspect_data.aspect_plays["Basic"].win_percentage * 100)), style="bold grey50", justify='right'))
            table.update_cell(self.rwp,self.cj, Text(str(round(self.aspect_data.aspect_plays["Justice"].win_percentage * 100)), style="bold yellow1", justify='right'))
            table.update_cell(self.rwp,self.cp, Text(str(round(self.aspect_data.aspect_plays["Protection"].win_percentage * 100)), style="bold green3", justify='right'))
        
    
class DifficultyStatistics(Static):
    difficulty_data: reactive[DifficultyStats] = reactive(DifficultyStats())
    c1 = None
    cs1 = None
    cs1e1 = None
    cs1e2 = None
    cs2 = None
    cs2e1 = None
    cs2e2 = None
    ch = None
    rp = None
    rw = None
    rwp = None

    def compose(self) -> ComposeResult:
        yield DataTable(id = "difficulty_table", show_cursor=False)

    def on_mount(self) -> None:
        table = self.query_one("#difficulty_table")
        self.c1 = table.add_column("Difficulty Data:")
        self.cs1 = table.add_column(Text("  S1", justify='right'))
        self.cs1e1 = table.add_column(Text("S1E1", justify='right'))
        self.cs1e2 = table.add_column(Text("S1E2", justify='right'))
        self.cs2 = table.add_column(Text("  S2", justify='right'))
        self.cs2e1 = table.add_column(Text("S2E1", justify='right'))
        self.cs2e2 = table.add_column(Text("S2E2", justify='right'))
        self.ch = table.add_column(Text("Heroic", justify='right'))
        self.rp = table.add_row("Plays", self.difficulty_data.standard1_plays,
                      self.difficulty_data.expert1_plays,
                      self.difficulty_data.expert2_plays,
                      self.difficulty_data.standard2_plays,
                      self.difficulty_data.expert3_plays,
                      self.difficulty_data.expert4_plays,
                      self.difficulty_data.heroic_plays)
        self.rw = table.add_row("Wins", self.difficulty_data.standard1_wins,
                      self.difficulty_data.expert1_wins,
                      self.difficulty_data.expert2_wins,
                      self.difficulty_data.standard2_wins,
                      self.difficulty_data.expert3_wins,
                      self.difficulty_data.expert4_wins,
                      self.difficulty_data.heroic_wins)
        self.rwp = table.add_row("Win %", round(self.difficulty_data.standard1_win_percentage * 100),
                      round(self.difficulty_data.expert1_win_percentage * 100),
                      round(self.difficulty_data.expert2_win_percentage * 100),
                      round(self.difficulty_data.standard2_win_percentage * 100),
                      round(self.difficulty_data.expert3_win_percentage * 100),
                      round(self.difficulty_data.expert4_win_percentage * 100),
                      round(self.difficulty_data.heroic_win_percentage * 100))

    def watch_difficulty_data(self, old_difficulty_data: DifficultyStats, new_difficulty_data: DifficultyStats):
        self.difficulty_data = new_difficulty_data
        table = self.query_one("#difficulty_table", DataTable)
        if self.rp is not None:
            table.update_cell(self.rp,self.cs1, Text(str(self.difficulty_data.standard1_plays), justify='right'))
            table.update_cell(self.rp,self.cs1e1, Text(str(self.difficulty_data.expert1_plays), justify='right'))
            table.update_cell(self.rp,self.cs1e2, Text(str(self.difficulty_data.expert2_plays), justify='right'))
            table.update_cell(self.rp,self.cs2, Text(str(self.difficulty_data.standard2_plays), justify='right'))
            table.update_cell(self.rp,self.cs2e1, Text(str(self.difficulty_data.expert3_plays), justify='right'))
            table.update_cell(self.rp,self.cs2e2, Text(str(self.difficulty_data.expert4_plays), justify='right'))
            table.update_cell(self.rp,self.ch, Text(str(self.difficulty_data.heroic_plays), justify='right'))
        if self.rw is not None:
            table.update_cell(self.rw,self.cs1, Text(str(self.difficulty_data.standard1_wins), justify='right'))
            table.update_cell(self.rw,self.cs1e1, Text(str(self.difficulty_data.expert1_wins), justify='right'))
            table.update_cell(self.rw,self.cs1e2, Text(str(self.difficulty_data.expert2_wins), justify='right'))
            table.update_cell(self.rw,self.cs2, Text(str(self.difficulty_data.standard2_wins), justify='right'))
            table.update_cell(self.rw,self.cs2e1, Text(str(self.difficulty_data.expert3_wins), justify='right'))
            table.update_cell(self.rw,self.cs2e2, Text(str(self.difficulty_data.expert4_wins), justify='right'))
            table.update_cell(self.rw,self.ch, Text(str(self.difficulty_data.heroic_wins), justify='right'))
        if self.rwp is not None:
            table.update_cell(self.rwp,self.cs1, Text(str(round(self.difficulty_data.standard1_win_percentage * 100)), justify='right'))
            table.update_cell(self.rwp,self.cs1e1, Text(str(round(self.difficulty_data.expert1_win_percentage * 100)), justify='right'))
            table.update_cell(self.rwp,self.cs1e2, Text(str(round(self.difficulty_data.expert2_win_percentage * 100)), justify='right'))
            table.update_cell(self.rwp,self.cs2, Text(str(round(self.difficulty_data.standard2_win_percentage * 100)), justify='right'))
            table.update_cell(self.rwp,self.cs2e1, Text(str(round(self.difficulty_data.expert3_win_percentage * 100)), justify='right'))
            table.update_cell(self.rwp,self.cs2e2, Text(str(round(self.difficulty_data.expert4_win_percentage * 100)), justify='right'))
            table.update_cell(self.rwp,self.ch, Text(str(round(self.difficulty_data.heroic_win_percentage * 100)), justify='right'))

