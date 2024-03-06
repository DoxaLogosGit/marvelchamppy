import simplejson as json
from textual.app import App, ComposeResult
from textual.containers import Horizontal, Container, Widget
from textual.reactive import reactive
from textual.widgets import Header, Footer, Tree, DataTable, Static
from analyze_data import Statistics, HeroData, VillainData, OverallData, AspectData

def read_data():
    marvel_plays = None
    with open("marvel_play_data.json") as play_data:
        marvel_plays = json.loads(play_data.read())

    statistics = Statistics(marvel_plays)
    statistics.analyze_play_data()
    return statistics

    
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
        self.rwp = table.add_row("Win %", self.aspect_data.leadership_win_percentage,
                      self.aspect_data.justice_win_percentage,
                      self.aspect_data.aggression_win_percentage,
                      self.aspect_data.protection_win_percentage,
                      self.aspect_data.basic_win_percentage)

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
            table.update_cell(self.rwp,self.cl, self.aspect_data.leadership_win_percentage)
            table.update_cell(self.rwp,self.ca, self.aspect_data.aggression_win_percentage)
            table.update_cell(self.rwp,self.cb, self.aspect_data.basic_win_percentage)
            table.update_cell(self.rwp,self.cj, self.aspect_data.justice_win_percentage)
            table.update_cell(self.rwp,self.cp, self.aspect_data.protection_win_percentage)
        


        
    
class DifficultyStats(Static):
    def compose(self) -> ComposeResult:
        yield DataTable(id = "difficulty_data")


class HeroResults(Widget):
    current_hero : reactive[HeroData] = reactive(HeroData("Bob", "none"))
    aspect_data : reactive[AspectData] = reactive(AspectData())

    def compose(self) -> ComposeResult:
        with Horizontal(id="hero_results"):
            yield AspectStats(id="hero_aspect").data_bind(aspect_data=HeroResults.aspect_data)

    def watch_current_hero(self, old_hero: HeroData, new_hero: HeroData):
        self.query_one("#hero_results").current_hero = new_hero
        self.query_one("#hero_aspect").aspect_data = new_hero.aspect_data
        self.query_one("#hero_aspect", Static).refresh()
        
    def on_mount(self) -> None:
        self.aspect_data = self.current_hero.aspect_data
        self.query_one("#aspect_data_table").refresh()
        

class OverallResults(Widget):

    overall_data: reactive[OverallData] = reactive(OverallData(""))
    aspect_data : reactive[AspectData] = reactive(AspectData())

    def compose(self) -> ComposeResult:
        with Horizontal(id="overall_results"):
            yield AspectStats().data_bind(OverallResults.aspect_data)
            
    def on_mount(self) -> None:
        self.aspect_data = self.overall_data.aspect_data

class MCStatApp(App):
    """ A Textual app for my Marvel Champions stat tracking"""

    BINDINGS = [("d", "toggle_dark", "Toggle Dark Mode")]
    CSS_PATH = "mc_stat_gui.tcss"

    statistics: reactive[Statistics] = reactive(read_data())
    current_hero : reactive[HeroData] = reactive(HeroData("Drax", "Guardian"))
    current_villain: reactive[VillainData] = reactive(VillainData("Rhino", "core"))
    overall_data : reactive[OverallData] = reactive(OverallData(""))

    def compose(self) -> ComposeResult:
        yield Header()
        with Horizontal(id="menu"):
            self.current_hero =self.statistics.hero_data["Drax"]
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
            with Container(id="data"):
                #yield OverallResults().data_bind(MCStatApp.overall_data)
                yield HeroResults(id="hresults").data_bind(current_hero=MCStatApp.current_hero)
        yield Footer()

    def on_mount(self) -> None:
        self.statistics = read_data()
        self.current_hero = self.statistics.hero_data["Drax"]

    def on_tree_node_selected(self, event: Tree.NodeSelected) -> None:
        #event.stop()
        #test if hero or villain or none
        if(event.node.label.plain in self.statistics.hero_data.keys()):
            #context switch to hero data
            self.current_hero = self.statistics.hero_data[event.node.label.plain]
            hero_results = self.query_one("#hresults", Widget)
            hero_results.refresh()
        elif(event.node.label.plain in self.statistics.villain_data.keys()):
            #context switch to villain data
            self.current_villain = self.statistics.villain_data[event.node.label.plain]
        elif(event.node.label.plain == "Overall"):
            #context switch to overall data
            pass

    def action_toggle_dark(self) -> None:
        self.dark = not self.dark
        
if __name__ == "__main__":
    app = MCStatApp()
    app.run()