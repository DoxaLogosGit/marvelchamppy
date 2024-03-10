import simplejson as json
from textual.app import App, ComposeResult
from widgets.stats import SpecialPlays, AspectStats, DifficultyStatistics, TotalStats, Name
from textual.containers import Vertical, Horizontal, Container, Widget
from textual.reactive import reactive
from textual.widgets import Header, Footer, Tree, DataTable, Static, ContentSwitcher, Label, OptionList
from analyze_data import Statistics, HeroData, VillainData, OverallData, AspectData, TeamData, DifficultyStats, ExpansionData
from rich.text import Text


def read_data():
    marvel_plays = None
    with open("marvel_play_data.json") as play_data:
        marvel_plays = json.loads(play_data.read())

    statistics = Statistics(marvel_plays)
    statistics.analyze_play_data()
    return statistics


class HeroResults(Static):
    current_hero : reactive[HeroData] = reactive(HeroData("Bob", "none"))
    aspect_data : reactive[AspectData] = reactive(AspectData())
    difficulty_data : reactive[DifficultyStats] = reactive(DifficultyStats())
    total_plays : reactive[int] = reactive(0)
    total_wins : reactive[int] = reactive(0)
    total_win_percentage : reactive[float] = reactive(0)
    name : reactive[str] = reactive("bob")

    def compose(self) -> ComposeResult:
        with Vertical(id="hero_results"):
            with Horizontal(id="hero_banner"):
                yield Label("Hero Statistics - ")
                yield Name(id="hero_name").data_bind(who=HeroResults.name)
            yield TotalStats(id="total_stats").data_bind(total_plays=HeroResults.total_plays,
                                                           total_wins=HeroResults.total_wins,
                                                           total_win_percentage=HeroResults.total_win_percentage)
            yield AspectStats(id="hero_aspect").data_bind(aspect_data=HeroResults.aspect_data)
            yield DifficultyStatistics(id="diff_stats").data_bind(difficulty_data=HeroResults.difficulty_data)
            with Horizontal(id="hero_lists_labels"):
                yield Label("Villains Defeated",markup=True, classes="listlabels")
                yield Label("Villains Played", markup=True, classes="listlabels")
                yield Label("Villains Not Played",markup=True, classes="listlabels")
            with Horizontal(id="hero_lists"):
                yield OptionList("Bad", "Good",id="villains_defeat")
                yield OptionList("Bad", "Good",id="villains_played")
                yield OptionList("Bad", "Good",id="villains_unplayed")

    def watch_current_hero(self, old_hero: HeroData, new_hero: HeroData):
        self.current_hero = new_hero
        self.name = new_hero.name
        self.aspect_data = new_hero.aspect_data
        self.difficulty_data = new_hero.difficulty_data
        self.total_plays = new_hero.total_plays
        self.total_wins = new_hero.total_wins
        self.total_win_percentage = new_hero.win_percentage
        dlist = self.query_one("#villains_defeat", OptionList)
        dlist.clear_options()
        dlist.add_options(self.current_hero.villains_defeated)
        dlist.highlighted = None

        ulist = self.query_one("#villains_unplayed", OptionList)
        ulist.clear_options()
        ulist.add_options(self.current_hero.villains_not_played)
        ulist.highlighted = None

        plist = self.query_one("#villains_played", OptionList)
        plist.clear_options()
        plist.add_options(self.current_hero.villains_played)
        plist.highlighted = None
       
class TeamResults(Static):
    current_team : reactive[TeamData] = reactive(TeamData("Junkers"))
    aspect_data : reactive[AspectData] = reactive(AspectData())
    difficulty_data : reactive[DifficultyStats] = reactive(DifficultyStats())
    total_plays : reactive[int] = reactive(0)
    total_wins : reactive[int] = reactive(0)
    total_win_percentage : reactive[float] = reactive(0)
    name : reactive[str] = reactive("Junkers")

    def compose(self) -> ComposeResult:
        with Vertical(id="team_results"):
            with Horizontal(id="team_banner"):
                yield Label("Team Statistics - ")
                yield Name(id="team_name").data_bind(who=TeamResults.name)
            yield TotalStats(id="total_stats").data_bind(total_plays=TeamResults.total_plays,
                                                           total_wins=TeamResults.total_wins,
                                                           total_win_percentage=TeamResults.total_win_percentage)
            yield AspectStats(id="team_aspect").data_bind(aspect_data=TeamResults.aspect_data)
            yield DifficultyStatistics(id="team_diff_stats").data_bind(difficulty_data=TeamResults.difficulty_data)
            with Horizontal(id="hero_lists_labels"):
                yield Label("Villains Defeated",markup=True, classes="listlabels")
                yield Label("Villains Played", markup=True, classes="listlabels")
                yield Label("Villains Not Played",markup=True, classes="listlabels")
            with Horizontal(id="team_lists"):
                yield OptionList("Bad", "Good",id="villains_defeat")
                yield OptionList("Bad", "Good",id="villains_played")
                yield OptionList("Bad", "Good",id="villains_unplayed")

    def watch_current_team(self, old_team: TeamData, new_team: TeamData):
        self.current_team = new_team
        self.name = new_team.name
        self.aspect_data = new_team.aspect_data
        self.difficulty_data = new_team.difficulty_data
        self.total_plays = new_team.total_plays
        self.total_wins = new_team.total_wins
        self.total_win_percentage = new_team.win_percentage
        dlist = self.query_one("#villains_defeat", OptionList)
        dlist.clear_options()
        dlist.add_options(self.current_team.villains_defeated)
        dlist.highlighted = None

        ulist = self.query_one("#villains_unplayed", OptionList)
        ulist.clear_options()
        ulist.add_options(self.current_team.villains_not_played)
        ulist.highlighted = None

        plist = self.query_one("#villains_played", OptionList)
        plist.clear_options()
        plist.add_options(self.current_team.villains_played)
        plist.highlighted = None

        
class VillainResults(Static):
    current_villain : reactive[VillainData] = reactive(VillainData("Evil Bob", "none"))
    aspect_data : reactive[AspectData] = reactive(AspectData())
    difficulty_data : reactive[DifficultyStats] = reactive(DifficultyStats())
    total_plays : reactive[int] = reactive(0)
    total_wins : reactive[int] = reactive(0)
    total_win_percentage : reactive[float] = reactive(0)
    name : reactive[str] = reactive("Evil Bob")

    def compose(self) -> ComposeResult:
        with Vertical(id="villain_results"):
            with Horizontal(id="villain_banner"):
                yield Label("Villain Statistics - ")
                yield Name(id="villain_name").data_bind(who=VillainResults.name)
            yield TotalStats(id="total_stats").data_bind(total_plays=VillainResults.total_plays,
                                                           total_wins=VillainResults.total_wins,
                                                           total_win_percentage=VillainResults.total_win_percentage)
            yield AspectStats(id="villain_aspect").data_bind(aspect_data=VillainResults.aspect_data)
            yield DifficultyStatistics(id="villain_diff_stats").data_bind(difficulty_data=VillainResults.difficulty_data)
            with Horizontal(id="villains_lists_labels"):
                yield Label("Heroes Played", markup=True, classes="vlistlabels")
                yield Label("Heroes Not Played",markup=True, classes="vlistlabels")
            with Horizontal(id="villain_lists"):
                yield OptionList("Bad", "Good",id="heroes_played")
                yield OptionList("Bad", "Good",id="heroes_unplayed")

    def watch_current_villain(self, old_villain: VillainData, new_villain: VillainData):
        self.current_villain = new_villain
        self.name = new_villain.name
        self.aspect_data = new_villain.aspect_data
        self.difficulty_data = new_villain.difficulty_data
        self.total_plays = new_villain.total_plays
        self.total_wins = new_villain.total_wins
        self.total_win_percentage = new_villain.win_percentage


        ulist = self.query_one("#heroes_unplayed", OptionList)
        ulist.clear_options()
        ulist.add_options(self.current_villain.heroes_not_played)
        ulist.highlighted = None

        plist = self.query_one("#heroes_played", OptionList)
        plist.clear_options()
        plist.add_options(self.current_villain.heroes_played)
        plist.highlighted = None

class BigBoxResults(Static):
    current_bigbox : reactive[ExpansionData] = reactive(ExpansionData("Evil Bob"))
    aspect_data : reactive[AspectData] = reactive(AspectData())
    difficulty_data : reactive[DifficultyStats] = reactive(DifficultyStats())
    total_plays : reactive[int] = reactive(0)
    total_wins : reactive[int] = reactive(0)
    total_win_percentage : reactive[float] = reactive(0)
    name : reactive[str] = reactive("Evil Bob")

    def compose(self) -> ComposeResult:
        with Vertical(id="bigbox_results"):
            with Horizontal(id="bigbox_banner"):
                yield Label("Big Box Statistics - ")
                yield Name(id="bigbox_name").data_bind(who=BigBoxResults.name)
            yield TotalStats(id="total_stats").data_bind(total_plays=BigBoxResults.total_plays,
                                                           total_wins=BigBoxResults.total_wins,
                                                           total_win_percentage=BigBoxResults.total_win_percentage)
            yield AspectStats(id="bigbox_aspect").data_bind(aspect_data=BigBoxResults.aspect_data)
            yield DifficultyStatistics(id="bigbox_diff_stats").data_bind(difficulty_data=BigBoxResults.difficulty_data)
            with Horizontal(id="villains_lists_labels"):
                yield Label("Heroes Played", markup=True, classes="vlistlabels")
                yield Label("Heroes Not Played",markup=True, classes="vlistlabels")
            with Horizontal(id="bigbox_lists"):
                yield OptionList("Bad", "Good",id="heroes_played")
                yield OptionList("Bad", "Good",id="heroes_unplayed")

    def watch_current_bigbox(self, old_bigbox: ExpansionData, new_bigbox: ExpansionData):
        self.current_bigbox = new_bigbox
        self.name = new_bigbox.name
        self.aspect_data = new_bigbox.aspect_data
        self.difficulty_data = new_bigbox.difficulty_data
        self.total_plays = new_bigbox.total_plays
        self.total_wins = new_bigbox.total_wins
        self.total_win_percentage = new_bigbox.win_percentage


        ulist = self.query_one("#heroes_unplayed", OptionList)
        ulist.clear_options()
        ulist.add_options(self.current_bigbox.heroes_not_played)
        ulist.highlighted = None

        plist = self.query_one("#heroes_played", OptionList)
        plist.clear_options()
        plist.add_options(self.current_bigbox.heroes_played)
        plist.highlighted = None

class ScenarioPackResults(Static):
    current_pack : reactive[ExpansionData] = reactive(ExpansionData("Evil Bob"))
    aspect_data : reactive[AspectData] = reactive(AspectData())
    difficulty_data : reactive[DifficultyStats] = reactive(DifficultyStats())
    total_plays : reactive[int] = reactive(0)
    total_wins : reactive[int] = reactive(0)
    total_win_percentage : reactive[float] = reactive(0)
    name : reactive[str] = reactive("Evil Bob")

    def compose(self) -> ComposeResult:
        with Vertical(id="pack_results"):
            with Horizontal(id="pack_banner"):
                yield Label("Scenario Pack Statistics - ")
                yield Name(id="pack_name").data_bind(who=ScenarioPackResults.name)
            yield TotalStats(id="total_stats").data_bind(total_plays=ScenarioPackResults.total_plays,
                                                           total_wins=ScenarioPackResults.total_wins,
                                                           total_win_percentage=ScenarioPackResults.total_win_percentage)
            yield AspectStats(id="pack_aspect").data_bind(aspect_data=ScenarioPackResults.aspect_data)
            yield DifficultyStatistics(id="pack_diff_stats").data_bind(difficulty_data=ScenarioPackResults.difficulty_data)
            with Horizontal(id="villains_lists_labels"):
                yield Label("Heroes Played", markup=True, classes="vlistlabels")
                yield Label("Heroes Not Played",markup=True, classes="vlistlabels")
            with Horizontal(id="pack_lists"):
                yield OptionList("Bad", "Good",id="heroes_played")
                yield OptionList("Bad", "Good",id="heroes_unplayed")

    def watch_current_pack(self, old_pack: ExpansionData, new_pack: ExpansionData):
        self.current_villain = new_pack
        self.name = new_pack.name
        self.aspect_data = new_pack.aspect_data
        self.difficulty_data = new_pack.difficulty_data
        self.total_plays = new_pack.total_plays
        self.total_wins = new_pack.total_wins
        self.total_win_percentage = new_pack.win_percentage


        ulist = self.query_one("#heroes_unplayed", OptionList)
        ulist.clear_options()
        ulist.add_options(self.current_pack.heroes_not_played)
        ulist.highlighted = None

        plist = self.query_one("#heroes_played", OptionList)
        plist.clear_options()
        plist.add_options(self.current_pack.heroes_played)
        plist.highlighted = None
        
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
            yield Label("Overall Statistics")
            with Horizontal(id="play_data"):
                yield TotalStats(id="overall_totals").data_bind(total_plays=OverallResults.total_plays,
                                                            total_wins=OverallResults.total_wins,
                                                            total_win_percentage=OverallResults.total_win_percentage)
                yield SpecialPlays(id="special_plays").data_bind(solo_plays=OverallResults.solo_plays,
                                                                 multiplayer_plays=OverallResults.multiplayer_plays,
                                                                 multihanded_solo_plays=OverallResults.multihanded_solo_plays)
            yield AspectStats(id='overall_aspect').data_bind(aspect_data=OverallResults.aspect_data)
            yield DifficultyStatistics(id='overall_diff').data_bind(difficulty_data=OverallResults.difficulty_data)
            
    
    def watch_overall_data(self, old_overall_data : OverallData, new_overall_data : OverallData):
        self.overall_data = new_overall_data
        self.solo_plays = new_overall_data.overall_true_solo_plays
        self.multiplayer_plays = new_overall_data.overall_multi_plays
        self.multihanded_solo_plays = new_overall_data.overall_solo_plays
        self.aspect_data = self.overall_data.aspect_data
        self.difficulty_data = self.overall_data.difficulty_data
        self.total_plays = new_overall_data.overall_plays
        self.total_wins = new_overall_data.overall_wins
        self.total_win_percentage = new_overall_data.overall_win_percentage
        self.solo_plays = new_overall_data.overall_true_solo_plays
        self.multihanded_solo_plays = new_overall_data.overall_solo_plays
        self.multiplayer_plays = new_overall_data.overall_multi_plays

class MCStatApp(App):
    """ A Textual app for my Marvel Champions stat tracking"""

    BINDINGS = [("d", "toggle_dark", "Toggle Dark Mode")]
    CSS_PATH = "mc_stat_gui.tcss"

    statistics: reactive[Statistics] = reactive(read_data())
    current_hero : reactive[HeroData] = reactive(HeroData("Gamora", "Guardian"))
    current_villain: reactive[VillainData] = reactive(VillainData("Rhino", "core"))
    overall_data : reactive[OverallData] = reactive(OverallData(""))
    current_team : reactive[TeamData] = reactive(TeamData("Junker"))
    current_bigbox : reactive[ExpansionData] = reactive(ExpansionData("Junker"))
    current_pack : reactive[ExpansionData] = reactive(ExpansionData("Junker"))

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
            team_root = tree.root.add("Teams")
            for team_name in self.statistics.team_data.keys():
                if team_name != "X-Force" and team_name != "X-Men":
                    team_root.add_leaf(team_name+"s")
                else:
                    team_root.add_leaf(team_name)
            aspect_root = tree.root.add("Aspects")
            aspect_root.add_leaf("Aggression")
            aspect_root.add_leaf("Justice")
            aspect_root.add_leaf("Leadership")
            aspect_root.add_leaf("Protection")
            aspect_root.add_leaf("Basic")
            big_box_root = tree.root.add("Big Box Expansions")
            for bb_name in self.statistics.big_box_data.keys():
                big_box_root.add_leaf(bb_name)
            scenario_pack_root = tree.root.add("Scenario Packs")
            for sp_name in self.statistics.scenario_pack_data.keys():
                scenario_pack_root.add_leaf(sp_name)
            yield tree
            with ContentSwitcher(initial="oresults"):
                yield OverallResults(id="oresults").data_bind(overall_data=MCStatApp.overall_data)
                yield HeroResults(id="hresults").data_bind(current_hero=MCStatApp.current_hero)
                yield VillainResults(id="vresults").data_bind(current_villain=MCStatApp.current_villain)
                yield TeamResults(id="tresults").data_bind(current_team=MCStatApp.current_team)
                yield ScenarioPackResults(id="presults").data_bind(current_pack=MCStatApp.current_pack)
                yield BigBoxResults(id="bresults").data_bind(current_bigbox=MCStatApp.current_bigbox)
        yield Footer()

    def on_mount(self) -> None:
        self.current_hero = self.statistics.hero_data["Gamora"]
        self.current_villain = self.statistics.villain_data["Klaw"]
        self.current_team = self.statistics.team_data["Avenger"]
        self.current_bigbox = self.statistics.big_box_data["Sinister Motives"]
        self.current_pack = self.statistics.scenario_pack_data["The Hood"]
        self.overall_data = self.statistics.overall_data
        self.query_one("#oresults").overall_data = self.overall_data
        self.query_one("#hresults").current_hero = self.current_hero
        self.query_one("#vresults").current_villain = self.current_villain
        self.query_one("#tresults").current_team = self.current_team
        self.query_one("#bresults").current_bigbox = self.current_bigbox
        self.query_one("#presults").current_pack = self.current_pack

    def on_tree_node_selected(self, event: Tree.NodeSelected) -> None:
        #test if hero or villain or none
        if(event.node.label.plain in self.statistics.hero_data.keys()):
            self.query_one(ContentSwitcher).current = "hresults"
            self.current_hero = self.statistics.hero_data[event.node.label.plain]
        elif(event.node.label.plain in self.statistics.villain_data.keys()):
            self.query_one(ContentSwitcher).current = "vresults"
            self.current_villain = self.statistics.villain_data[event.node.label.plain]
        #checking for X-force & X-men (not ending in s)
        elif(event.node.label.plain in self.statistics.team_data.keys()):
            self.query_one(ContentSwitcher).current = "tresults"
            self.current_team = self.statistics.team_data[event.node.label.plain]
        #checking for other teams ending with s
        elif(event.node.label.plain[:-1] in self.statistics.team_data.keys()):
            self.query_one(ContentSwitcher).current = "tresults"
            self.current_team = self.statistics.team_data[event.node.label.plain[:-1]]
        elif(event.node.label.plain == "Overall"):
            self.query_one(ContentSwitcher).current = "oresults"
            self.overall_data = self.statistics.overall_data
        elif(event.node.label.plain in self.statistics.big_box_data.keys()):
            self.query_one(ContentSwitcher).current = "bresults"
            self.current_bigbox = self.statistics.big_box_data[event.node.label.plain]
        elif(event.node.label.plain in self.statistics.scenario_pack_data.keys()):
            self.query_one(ContentSwitcher).current = "presults"
            self.current_pack = self.statistics.scenario_pack_data[event.node.label.plain]

    def action_toggle_dark(self) -> None:
        self.dark = not self.dark
        
if __name__ == "__main__":
    app = MCStatApp()
    app.run()