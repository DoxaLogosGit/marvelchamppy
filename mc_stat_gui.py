import simplejson as json
from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.reactive import reactive
from textual.widgets import Header, Footer, Tree, ContentSwitcher
from analyze_data import Statistics, HeroData, VillainData, OverallData, TeamData, ExpansionData
from widgets.results import HeroResults, VillainResults, OverallResults, TeamResults, BigBoxResults, ScenarioPackResults


def read_data():
    marvel_plays = None
    with open("marvel_play_data.json") as play_data:
        marvel_plays = json.loads(play_data.read())

    statistics = Statistics(marvel_plays)
    statistics.analyze_play_data()
    return statistics


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
            self.current_hero = self.statistics.hero_data[event.node.label.plain]
            self.query_one(ContentSwitcher).current = "hresults"
        elif(event.node.label.plain in self.statistics.villain_data.keys()):
            self.current_villain = self.statistics.villain_data[event.node.label.plain]
            self.query_one(ContentSwitcher).current = "vresults"
        #checking for X-force & X-men (not ending in s)
        elif(event.node.label.plain in self.statistics.team_data.keys()):
            self.current_team = self.statistics.team_data[event.node.label.plain]
            self.query_one(ContentSwitcher).current = "tresults"
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
