import simplejson as json
from textual.app import App, ComposeResult
from textual.containers import Vertical, Horizontal, Container, Widget
from textual.reactive import reactive
from textual.widgets import Header, Footer, Tree, DataTable, Static, ContentSwitcher
from analyze_data import Statistics, HeroData, VillainData, OverallData, AspectData, DifficultyStats

def read_data():
    marvel_plays = None
    with open("marvel_play_data.json") as play_data:
        marvel_plays = json.loads(play_data.read())

    statistics = Statistics(marvel_plays)
    statistics.analyze_play_data()
    return statistics

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
        yield DataTable(id = "special_play_table")

    def on_mount(self) -> None:
        table = self.query_one("#special_play_table")
        self.c1 = table.add_column("Special Plays:")
        self.ct = table.add_column("   ")
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
        yield DataTable(id = "total_data_table")

    def on_mount(self) -> None:
        table = self.query_one("#total_data_table")
        self.c1 = table.add_column("Total Data:")
        self.ct = table.add_column("   ")
        self.rp = table.add_row("Plays", self.total_plays)
        self.rw = table.add_row("Wins", self.total_wins)
        self.rwp = table.add_row("Win %", round(self.total_win_percentage * 100, 1))

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
            table.update_cell(self.rwp,self.ct, round(self.total_win_percentage * 100, 1))

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
        yield DataTable(id = "aspect_data_table")
    
    def on_mount(self) -> None:
        table = self.query_one("#aspect_data_table")
        self.c1 = table.add_column("Aspect Data:")
        self.cl = table.add_column("Leadership")
        self.cj = table.add_column("Justice")
        self.ca = table.add_column("Agression")
        self.cp = table.add_column("Protection")
        self.cb = table.add_column("Basic")
        self.rp = table.add_row("Plays", self.aspect_data.leadership_plays,
                      self.aspect_data.justice_plays,
                      self.aspect_data.aggression_plays,
                      self.aspect_data.protection_plays,
                      self.aspect_data.basic_plays)
        self.rw = table.add_row("Wins", self.aspect_data.leadership_wins,
                      self.aspect_data.justice_wins,
                      self.aspect_data.aggression_wins,
                      self.aspect_data.protection_wins,
                      self.aspect_data.basic_wins)
        self.rwp = table.add_row("Win %", round(self.aspect_data.leadership_win_percentage * 100, 1),
                      round(self.aspect_data.justice_win_percentage * 100, 1),
                      round(self.aspect_data.aggression_win_percentage * 100, 1),
                      round(self.aspect_data.protection_win_percentage * 100, 1),
                      round(self.aspect_data.basic_win_percentage * 100, 1))

    def watch_aspect_data(self, old_aspect_data: AspectData, new_aspect_data: AspectData):
        self.aspect_data = new_aspect_data
        table = self.query_one("#aspect_data_table", DataTable)
        if self.rp is not None:
            table.update_cell(self.rp,self.cl, self.aspect_data.leadership_plays)
            table.update_cell(self.rp,self.ca, self.aspect_data.aggression_plays)
            table.update_cell(self.rp,self.cb, self.aspect_data.basic_plays)
            table.update_cell(self.rp,self.cj, self.aspect_data.justice_plays)
            table.update_cell(self.rp,self.cp, self.aspect_data.protection_plays)
        if self.rw is not None:
            table.update_cell(self.rw,self.cl, self.aspect_data.leadership_wins)
            table.update_cell(self.rw,self.ca, self.aspect_data.aggression_wins)
            table.update_cell(self.rw,self.cb, self.aspect_data.basic_wins)
            table.update_cell(self.rw,self.cj, self.aspect_data.justice_wins)
            table.update_cell(self.rw,self.cp, self.aspect_data.protection_wins)
        if self.rwp is not None:
            table.update_cell(self.rwp,self.cl, round(self.aspect_data.leadership_win_percentage * 100, 1))
            table.update_cell(self.rwp,self.ca, round(self.aspect_data.aggression_win_percentage * 100, 1))
            table.update_cell(self.rwp,self.cb, round(self.aspect_data.basic_win_percentage * 100, 1))
            table.update_cell(self.rwp,self.cj, round(self.aspect_data.justice_win_percentage * 100, 1))
            table.update_cell(self.rwp,self.cp, round(self.aspect_data.protection_win_percentage * 100, 1))
        
    
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
        yield DataTable(id = "difficulty_table")

    def on_mount(self) -> None:
        table = self.query_one("#difficulty_table")
        self.c1 = table.add_column("Difficulty Data:")
        self.cs1 = table.add_column("S1")
        self.cs1e1 = table.add_column("S1E1")
        self.cs1e2 = table.add_column("S1E2")
        self.cs2 = table.add_column("S2")
        self.cs2e1 = table.add_column("S2E1")
        self.cs2e2 = table.add_column("S2E2")
        self.ch = table.add_column("Heroic")
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
        self.rwp = table.add_row("Win %", round(self.difficulty_data.standard1_win_percentage * 100, 1),
                      round(self.difficulty_data.expert1_win_percentage * 100, 1),
                      round(self.difficulty_data.expert2_win_percentage * 100, 1),
                      round(self.difficulty_data.standard2_win_percentage * 100, 1),
                      round(self.difficulty_data.expert3_win_percentage * 100, 1),
                      round(self.difficulty_data.expert4_win_percentage * 100, 1),
                      round(self.difficulty_data.heroic_win_percentage * 100, 1))

    def watch_difficulty_data(self, old_difficulty_data: DifficultyStats, new_difficulty_data: DifficultyStats):
        self.difficulty_data = new_difficulty_data
        table = self.query_one("#difficulty_table", DataTable)
        if self.rp is not None:
            table.update_cell(self.rp,self.cs1, self.difficulty_data.standard1_plays)
            table.update_cell(self.rp,self.cs1e1, self.difficulty_data.expert1_plays)
            table.update_cell(self.rp,self.cs1e2, self.difficulty_data.expert2_plays)
            table.update_cell(self.rp,self.cs2, self.difficulty_data.standard2_plays)
            table.update_cell(self.rp,self.cs2e1, self.difficulty_data.expert3_plays)
            table.update_cell(self.rp,self.cs2e2, self.difficulty_data.expert4_plays)
            table.update_cell(self.rp,self.ch, self.difficulty_data.heroic_plays)
        if self.rw is not None:
            table.update_cell(self.rw,self.cs1, self.difficulty_data.standard1_wins)
            table.update_cell(self.rw,self.cs1e1, self.difficulty_data.expert1_wins)
            table.update_cell(self.rw,self.cs1e2, self.difficulty_data.expert2_wins)
            table.update_cell(self.rw,self.cs2, self.difficulty_data.standard2_wins)
            table.update_cell(self.rw,self.cs2e1, self.difficulty_data.expert3_wins)
            table.update_cell(self.rw,self.cs2e2, self.difficulty_data.expert4_wins)
            table.update_cell(self.rw,self.ch, self.difficulty_data.heroic_wins)
        if self.rwp is not None:
            table.update_cell(self.rwp,self.cs1, round(self.difficulty_data.standard1_win_percentage * 100, 1))
            table.update_cell(self.rwp,self.cs1e1, round(self.difficulty_data.expert1_win_percentage * 100, 1))
            table.update_cell(self.rwp,self.cs1e2, round(self.difficulty_data.expert2_win_percentage * 100, 1))
            table.update_cell(self.rwp,self.cs2, round(self.difficulty_data.standard2_win_percentage * 100, 1))
            table.update_cell(self.rwp,self.cs2e1, round(self.difficulty_data.expert3_win_percentage * 100, 1))
            table.update_cell(self.rwp,self.cs2e2, round(self.difficulty_data.expert4_win_percentage * 100, 1))
            table.update_cell(self.rwp,self.ch, round(self.difficulty_data.heroic_win_percentage * 100, 1))


class HeroResults(Static):
    current_hero : reactive[HeroData] = reactive(HeroData("Bob", "none"))
    aspect_data : reactive[AspectData] = reactive(AspectData())
    difficulty_data : reactive[DifficultyStats] = reactive(DifficultyStats())
    total_plays : reactive[int] = reactive(0)
    total_wins : reactive[int] = reactive(0)
    total_win_percentage : reactive[float] = reactive(0)

    def compose(self) -> ComposeResult:
        with Vertical(id="hero_results"):
            yield TotalStats(id="total_stats").data_bind(total_plays=HeroResults.total_plays,
                                                           total_wins=HeroResults.total_wins,
                                                           total_win_percentage=HeroResults.total_win_percentage)
            yield AspectStats(id="hero_aspect").data_bind(aspect_data=HeroResults.aspect_data)
            yield DifficultyStatistics(id="diff_stats").data_bind(difficulty_data=HeroResults.difficulty_data)

    def watch_current_hero(self, old_hero: HeroData, new_hero: HeroData):
        self.current_hero = new_hero
        self.query_one("#hero_aspect").aspect_data = new_hero.aspect_data
        self.query_one("#diff_stats").difficulty_data = new_hero.difficulty_data
        self.query_one("#total_stats").total_plays = new_hero.total_plays
        self.query_one("#total_stats").total_wins = new_hero.total_wins
        self.query_one("#total_stats").total_win_percentage = new_hero.win_percentage
        
    def on_mount(self) -> None:
        self.aspect_data = self.current_hero.aspect_data
        self.difficulty_data = self.current_hero.difficulty_data
        self.total_plays = self.current_hero.total_plays
        self.total_wins = self.current_hero.win_percentage
        self.total_wins = self.current_hero.win_percentage
        
class VillainResults(Static):
    current_villain : reactive[VillainData] = reactive(VillainData("Evil Bob", "none"))
    aspect_data : reactive[AspectData] = reactive(AspectData())
    difficulty_data : reactive[DifficultyStats] = reactive(DifficultyStats())
    total_plays : reactive[int] = reactive(0)
    total_wins : reactive[int] = reactive(0)
    total_win_percentage : reactive[float] = reactive(0)

    def compose(self) -> ComposeResult:
        with Vertical(id="villain_results"):
            yield TotalStats(id="total_stats").data_bind(total_plays=VillainResults.total_plays,
                                                           total_wins=VillainResults.total_wins,
                                                           total_win_percentage=VillainResults.total_win_percentage)
            yield AspectStats(id="villain_aspect").data_bind(aspect_data=VillainResults.aspect_data)
            yield DifficultyStatistics(id="villain_diff_stats").data_bind(difficulty_data=VillainResults.difficulty_data)

    def watch_current_villain(self, old_villain: HeroData, new_villain: HeroData):
        self.current_villain = new_villain
        self.query_one("#villain_aspect").aspect_data = new_villain.aspect_data
        self.query_one("#villain_diff_stats").difficulty_data = new_villain.difficulty_data
        self.query_one("#total_stats").total_plays = new_villain.total_plays
        self.query_one("#total_stats").total_wins = new_villain.total_wins
        self.query_one("#total_stats").total_win_percentage = new_villain.win_percentage
        
    def on_mount(self) -> None:
        self.aspect_data = self.current_villain.aspect_data
        self.difficulty_data = self.current_villain.difficulty_data
        self.total_plays = self.current_villain.total_plays
        self.total_wins = self.current_villain.win_percentage
        self.total_wins = self.current_villain.win_percentage
        

class OverallResults(Static):

    overall_data: reactive[OverallData] = reactive(OverallData(""))
    aspect_data : reactive[AspectData] = reactive(AspectData())
    difficulty_data : reactive[DifficultyStats] = reactive(DifficultyStats())
    total_plays : reactive[int] = reactive(0)
    total_wins : reactive[int] = reactive(0)
    total_win_percentage : reactive[float] = reactive(0)
    solo_plays : reactive[int] = reactive(0)
    multiplayer_plays : reactive[int] = reactive(0)
    multihanded_solo_plays : reactive[int] = reactive(0)

    def compose(self) -> ComposeResult:
        with Vertical(id="overall_results"):
            with Horizontal(id="play_data"):
                yield TotalStats(id="overall_totals").data_bind(total_plays=OverallResults.total_plays,
                                                            total_wins=OverallResults.total_wins,
                                                            total_win_percentage=OverallResults.total_win_percentage)
                yield SpecialPlays(id="special_plays").data_bind(solo_plays=OverallResults.solo_plays,
                                                                 multiplayer_plays=OverallResults.multiplayer_plays,
                                                                 multihanded_solo_plays=OverallResults.multihanded_solo_plays)
            yield AspectStats(id='overall_aspect').data_bind(aspect_data=OverallResults.aspect_data)
            yield DifficultyStatistics(id='overall_diff').data_bind(difficulty_data=OverallResults.difficulty_data)
            
    def on_mount(self) -> None:
        self.aspect_data = self.overall_data.aspect_data
        self.query_one('#overall_aspect').aspect_data = self.aspect_data
        self.query_one('#overall_diff').difficulty_data = self.difficulty_data
        self.total_plays = self.overall_data.overall_plays
        self.total_wins = self.overall_data.overall_wins
        self.total_win_percentage = self.overall_data.overall_win_percentage
        self.solo_plays = self.overall_data.overall_true_solo_plays
        self.multiplayer_plays = self.overall_data.overall_multi_plays
        self.multihanded_solo_plays = self.overall_data.overall_solo_plays

    
    def watch_overall_data(self, old_overall_data : OverallData, new_overall_data : OverallData):
        self.overall_data = new_overall_data
        self.solo_plays = new_overall_data.overall_true_solo_plays
        self.multiplayer_plays = new_overall_data.overall_multi_plays
        self.multihanded_solo_plays = new_overall_data.overall_solo_plays
        self.query_one("#overall_aspect").aspect_data = self.overall_data.aspect_data
        self.query_one('#overall_diff').difficulty_data = self.overall_data.difficulty_data
        self.query_one("#overall_totals").total_plays = new_overall_data.overall_plays
        self.query_one("#overall_totals").total_wins = new_overall_data.overall_wins
        self.query_one("#overall_totals").total_win_percentage = new_overall_data.overall_win_percentage
        self.query_one("#special_plays").solo_plays = new_overall_data.overall_true_solo_plays
        self.query_one("#special_plays").multihanded_solo_plays = new_overall_data.overall_solo_plays
        self.query_one("#special_plays").multiplayer_plays = new_overall_data.overall_multi_plays

class MCStatApp(App):
    """ A Textual app for my Marvel Champions stat tracking"""

    BINDINGS = [("d", "toggle_dark", "Toggle Dark Mode")]
    CSS_PATH = "mc_stat_gui.tcss"

    statistics: reactive[Statistics] = reactive(read_data())
    #statistics: reactive[Statistics] = reactive(STATISTICS)
    #current_hero : reactive[HeroData] = reactive(STATISTICS.hero_data["Gamora"])
    current_hero : reactive[HeroData] = reactive(HeroData("Gamora", "Guardian"))
    current_villain: reactive[VillainData] = reactive(VillainData("Rhino", "core"))
    overall_data : reactive[OverallData] = reactive(OverallData(""))

    def compose(self) -> ComposeResult:
        yield Header()
        with Horizontal(id="menu"):
            #create the tree
            tree: Tree[dict] = Tree("Marvel Champions Data", id="mctree")
            tree.root.expand()
            overall_root = tree.root.add_leaf("Overall")
            heroes_root = tree.root.add("Heroes")
            for hero in self.statistics.sorted_heroes:
                heroes_root.add_leaf(hero[0])
            villains_root = tree.root.add("Villains")
            for villain in self.statistics.sorted_villains:
                villains_root.add_leaf(villain[0])
            yield tree
            with ContentSwitcher(initial="oresults"):
                yield OverallResults(id="oresults").data_bind(overall_data=MCStatApp.overall_data)
                yield HeroResults(id="hresults").data_bind(current_hero=MCStatApp.current_hero)
                yield VillainResults(id="vresults").data_bind(current_villain=MCStatApp.current_villain)
        yield Footer()

    def on_mount(self) -> None:
        self.current_hero = self.statistics.hero_data["Gamora"]
        self.current_villain = self.statistics.villain_data["Klaw"]
        self.overall_data = self.statistics.overall_data
        self.query_one("#oresults").overall_data = self.overall_data
        self.query_one("#hresults").current_hero = self.current_hero
        self.query_one("#vresults").current_villain = self.current_villain

    def on_tree_node_selected(self, event: Tree.NodeSelected) -> None:
        #test if hero or villain or none
        if(event.node.label.plain in self.statistics.hero_data.keys()):
            self.query_one(ContentSwitcher).current = "hresults"
            self.current_hero = self.statistics.hero_data[event.node.label.plain]
        elif(event.node.label.plain in self.statistics.villain_data.keys()):
            self.query_one(ContentSwitcher).current = "vresults"
            self.current_villain = self.statistics.villain_data[event.node.label.plain]
        elif(event.node.label.plain == "Overall"):
            self.query_one(ContentSwitcher).current = "oresults"
            self.overall_data = self.statistics.overall_data

    def action_toggle_dark(self) -> None:
        self.dark = not self.dark
        
if __name__ == "__main__":
    app = MCStatApp()
    app.run()