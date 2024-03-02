import simplejson as json
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Tree
from analyze_data import Statistics

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

    def compose(self) -> ComposeResult:
        self.statistics = read_data()
        yield Header()
        #create the tree

        tree: Tree[dict] = Tree("Marvel Champions Data")
        tree.root.expand()
        overall_root = tree.root.add_leaf("Overall")
        heroes_root = tree.root.add("Heroes")
        for hero in self.statistics.sorted_heroes:
            heroes_root.add_leaf(hero[0])
        villains_root = tree.root.add("Villains")
        for villain in self.statistics.sorted_villains:
            villains_root.add_leaf(villain[0])
        yield tree
        yield Footer()

    def action_toggle_dark(self) -> None:
        self.dark = not self.dark
        
if __name__ == "__main__":
    app = MCStatApp()
    app.run()