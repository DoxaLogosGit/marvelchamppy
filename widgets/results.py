from textual.app import ComposeResult
from textual.reactive import reactive
from textual.containers import Vertical, Horizontal
from textual.widgets import Label, OptionList, Static
from analyze_data import OverallData, AspectData, DifficultyStats, HeroBase, VillainBase, PlaySpecificStats
from widgets.stats import SpecialPlays, AspectStats, DifficultyStatistics, TotalStats

class Name(Static):
     who = reactive("Name")

     def render(self) -> str:
         return f"{self.who}"

class HeroBaseResults(Static):
    current_base : reactive[HeroBase] = reactive(HeroBase("Bob"))
    aspect_data : reactive[AspectData] = reactive(AspectData())
    difficulty_data : reactive[DifficultyStats] = reactive(DifficultyStats())
    total_plays : reactive[int] = reactive(0)
    total_wins : reactive[int] = reactive(0)
    total_win_percentage : reactive[float] = reactive(0)
    name : reactive[str] = reactive("bob")

    def compose(self) -> ComposeResult:
        with Vertical(id="hero_results"):
            with Horizontal(id="hero_banner"):
                yield Label("Statistics for ")
                yield Name(id="hero_name").data_bind(who=HeroBaseResults.name)
            yield TotalStats(id="total_stats").data_bind(total_plays=HeroBaseResults.total_plays,
                                                           total_wins=HeroBaseResults.total_wins,
                                                           total_win_percentage=HeroBaseResults.total_win_percentage)
            yield AspectStats(id="hero_aspect").data_bind(aspect_data=HeroBaseResults.aspect_data)
            yield DifficultyStatistics(id="diff_stats").data_bind(difficulty_data=HeroBaseResults.difficulty_data)
            with Horizontal(id="hero_lists_labels"):
                yield Label("Villains Not Defeated",markup=True, classes="listlabels")
                yield Label("Villains Played", markup=True, classes="listlabels")
                yield Label("Villains Not Played",markup=True, classes="listlabels")
            with Horizontal(id="hero_lists"):
                yield OptionList("Bad", "Good",id="villains_defeat")
                yield OptionList("Bad", "Good",id="villains_played")
                yield OptionList("Bad", "Good",id="villains_unplayed")

    def watch_current_base(self, old_hero: HeroBase, new_hero: HeroBase):
        self.current_base = new_hero
        self.name = new_hero.name
        self.aspect_data = new_hero.aspect_data
        self.difficulty_data = new_hero.difficulty_data
        self.total_plays = new_hero.total_plays
        self.total_wins = new_hero.total_wins
        self.total_win_percentage = new_hero.win_percentage
        dlist = self.query_one("#villains_defeat", OptionList)
        dlist.clear_options()
        dlist.add_options(self.current_base.villains_not_defeated)
        dlist.highlighted = None

        ulist = self.query_one("#villains_unplayed", OptionList)
        ulist.clear_options()
        ulist.add_options(self.current_base.villains_not_played)
        ulist.highlighted = None

        plist = self.query_one("#villains_played", OptionList)
        plist.clear_options()
        plist.add_options(self.current_base.villains_played)
        plist.highlighted = None
       
class VillainBaseResults(Static):
    current_base : reactive[VillainBase] = reactive(VillainBase("Evil Bob"))
    aspect_data : reactive[AspectData] = reactive(AspectData())
    difficulty_data : reactive[DifficultyStats] = reactive(DifficultyStats())
    total_plays : reactive[int] = reactive(0)
    total_wins : reactive[int] = reactive(0)
    total_win_percentage : reactive[float] = reactive(0)
    name : reactive[str] = reactive("Evil Bob")


    def compose(self) -> ComposeResult:
        with Vertical(id="villain_results"):
            with Horizontal(id="villain_banner"):
                yield Label("Statistics for ")
                yield Name(id="villain_name").data_bind(who=VillainBaseResults.name)
            yield TotalStats(id="total_stats").data_bind(total_plays=VillainBaseResults.total_plays,
                                                           total_wins=VillainBaseResults.total_wins,
                                                           total_win_percentage=VillainBaseResults.total_win_percentage)
            yield AspectStats(id="villain_aspect").data_bind(aspect_data=VillainBaseResults.aspect_data)
            yield DifficultyStatistics(id="villain_diff_stats").data_bind(difficulty_data=VillainBaseResults.difficulty_data)
            with Horizontal(id="villains_lists_labels"):
                yield Label("Heroes Played", markup=True, classes="vlistlabels")
                yield Label("Heroes Not Played",markup=True, classes="vlistlabels")
            with Horizontal(id="villain_lists"):
                yield OptionList("Bad", "Good",id="heroes_played")
                yield OptionList("Bad", "Good",id="heroes_unplayed")

    def watch_current_base(self, old_villain: VillainBase, new_villain: VillainBase):
        self.current_base = new_villain
        self.name = new_villain.name
        self.aspect_data = new_villain.aspect_data
        self.difficulty_data = new_villain.difficulty_data
        self.total_plays = new_villain.total_plays
        self.total_wins = new_villain.total_wins
        self.total_win_percentage = new_villain.win_percentage


        ulist = self.query_one("#heroes_unplayed", OptionList)
        ulist.clear_options()
        ulist.add_options(self.current_base.heroes_not_played)
        ulist.highlighted = None

        plist = self.query_one("#heroes_played", OptionList)
        plist.clear_options()
        plist.add_options(self.current_base.heroes_played)
        plist.highlighted = None

        
class AspectSpecificResults(Static):
    aspect_specific_stats: reactive[PlaySpecificStats] = reactive(PlaySpecificStats("Justice"))
    name: reactive[str] = reactive("Justice")

    def compose(self) -> ComposeResult:
        with Vertical(id="best_results"):
            with Horizontal(id="aspect_banner"):
                yield Label("Aspect Statistics for ")
                yield Name(id="aspect_name").data_bind(who=AspectSpecificResults.name)
            with Horizontal(id="best_lists_labels"):
                yield Label("Best 10 Heroes %", markup=True, classes="alistlabels")
                yield Label("Hardest 10 Villlain %",markup=True, classes="alistlabels")
                yield Label("Best 3 Teams %",markup=True, classes="alistlabels")
            with Horizontal(id="best_lists"):
                yield OptionList("Bad", "Good",id="best_hero_aspect", classes="olists")
                yield OptionList("Bad", "Good",id="hardest_villain_aspect", classes="olists")
                yield OptionList("Bad", "Good",id="best_team_aspect", classes="olists")
            with Horizontal(id="worst_lists_labels"):
                yield Label("Worst 10 Heroes %", markup=True, classes="alistlabels")
                yield Label("Easiest 10 Villlain %",markup=True, classes="alistlabels")
                yield Label("Worst 3 Teams %",markup=True, classes="alistlabels")
            with Horizontal(id="worst_lists"):
                yield OptionList("Bad", "Good",id="worst_hero_aspect", classes="olists")
                yield OptionList("Bad", "Good",id="easiest_villain_aspect", classes="olists")
                yield OptionList("Bad", "Good",id="worst_team_aspect", classes="olists")
            with Horizontal(id="most_lists_labels"):
                yield Label("10 Most Played Heroes", markup=True, classes="alistlabels")
                yield Label("10 Most Played Villlain",markup=True, classes="alistlabels")
                yield Label("3  Most Played Teams",markup=True, classes="alistlabels")
            with Horizontal(id="most_lists"):
                yield OptionList("Bad", "Good",id="most_hero_aspect", classes="olists")
                yield OptionList("Bad", "Good",id="most_villain_aspect", classes="olists")
                yield OptionList("Bad", "Good",id="most_team_aspect", classes="olists")



    def watch_aspect_specific_stats(self, old_specific: PlaySpecificStats, new_specific: PlaySpecificStats):
        self.aspect_specific_stats = new_specific
        self.name = new_specific.name
        self.query_one("#aspect_name").who = self.name

        hlist = self.query_one("#best_hero_aspect", OptionList)
        hlist.clear_options()
        hero_data = [f"{x["name"]} - {round(x["percent"]*100)}%" for x in self.aspect_specific_stats.get_best_x_heroes(10)]
        hlist.add_options(hero_data)
        hlist.highlighted = None

        vlist = self.query_one("#hardest_villain_aspect", OptionList)
        vlist.clear_options()
        villain_data = [f"{x["name"]} - {round(x["percent"]*100)}%" for x in self.aspect_specific_stats.get_best_x_villains(10)]
        vlist.add_options(villain_data)
        vlist.highlighted = None

        tlist = self.query_one("#best_team_aspect", OptionList)
        tlist.clear_options()
        team_data = [f"{x["name"]} - {round(x["percent"]*100)}%" for x in self.aspect_specific_stats.get_best_x_teams(3)]
        tlist.add_options(team_data)
        tlist.highlighted = None

        hwlist = self.query_one("#worst_hero_aspect", OptionList)
        hwlist.clear_options()
        whero_data = [f"{x["name"]} - {round(x["percent"]*100)}%" for x in self.aspect_specific_stats.get_worst_x_heroes(10)]
        hwlist.add_options(whero_data)
        hwlist.highlighted = None

        vwlist = self.query_one("#easiest_villain_aspect", OptionList)
        vwlist.clear_options()
        wvillain_data = [f"{x["name"]} - {round(x["percent"]*100)}%" for x in self.aspect_specific_stats.get_worst_x_villains(10)]
        vwlist.add_options(wvillain_data)
        vwlist.highlighted = None

        twlist = self.query_one("#worst_team_aspect", OptionList)
        twlist.clear_options()
        wteam_data = [f"{x["name"]} - {round(x["percent"]*100)}%" for x in self.aspect_specific_stats.get_worst_x_teams(3)]
        twlist.add_options(wteam_data)
        twlist.highlighted = None

        hmlist = self.query_one("#most_hero_aspect", OptionList)
        hmlist.clear_options()
        mhero_data = [f"{x["name"]} - {x["plays"]} plays" for x in self.aspect_specific_stats.get_most_x_heroes(10)]
        hmlist.add_options(mhero_data)
        hmlist.highlighted = None

        vmlist = self.query_one("#most_villain_aspect", OptionList)
        vmlist.clear_options()
        mvillain_data = [f"{x["name"]} - {x["plays"]} plays" for x in self.aspect_specific_stats.get_most_x_villains(10)]
        vmlist.add_options(mvillain_data)
        vmlist.highlighted = None

        tmlist = self.query_one("#most_team_aspect", OptionList)
        tmlist.clear_options()
        mteam_data = [f"{x["name"]} - {x["plays"]} plays" for x in self.aspect_specific_stats.get_most_x_teams(3)]
        tmlist.add_options(mteam_data)
        tmlist.highlighted = None

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
            with Horizontal(id="best_lists_labels"):
                yield Label("Best 10 Heroes %", markup=True, classes="alistlabels")
                yield Label("Hardest 10 Villlain %",markup=True, classes="alistlabels")
                yield Label("Best 3 Teams %",markup=True, classes="alistlabels")
            with Horizontal(id="best_lists"):
                yield OptionList("Bad", "Good",id="best_hero_overall", classes="olists")
                yield OptionList("Bad", "Good",id="hardest_villain_overall", classes="olists")
                yield OptionList("Bad", "Good",id="best_team_overall", classes="olists")
            with Horizontal(id="worst_lists_labels"):
                yield Label("Worst 10 Heroes %", markup=True, classes="alistlabels")
                yield Label("Easiest 10 Villlain %",markup=True, classes="alistlabels")
                yield Label("Worst 3 Teams %",markup=True, classes="alistlabels")
            with Horizontal(id="worst_lists"):
                yield OptionList("Bad", "Good",id="worst_hero_overall", classes="olists")
                yield OptionList("Bad", "Good",id="easiest_villain_overall", classes="olists")
                yield OptionList("Bad", "Good",id="worst_team_overall", classes="olists")
            with Horizontal(id="most_lists_labels"):
                yield Label("10 Most Played Heroes", markup=True, classes="alistlabels")
                yield Label("10 Most Played Villlain",markup=True, classes="alistlabels")
                yield Label("3  Most Played Teams",markup=True, classes="alistlabels")
            with Horizontal(id="most_lists"):
                yield OptionList("Bad", "Good",id="most_hero_overall", classes="olists")
                yield OptionList("Bad", "Good",id="most_villain_overall", classes="olists")
                yield OptionList("Bad", "Good",id="most_team_overall", classes="olists")

            
    
    def watch_overall_data(self, old_overall_data : OverallData, new_overall_data : OverallData):
        self.overall_data = new_overall_data
        self.solo_plays = new_overall_data.overall_true_solo_plays
        self.multiplayer_plays = new_overall_data.overall_multi_plays
        self.multihanded_solo_plays = new_overall_data.overall_solo_plays
        self.aspect_data = self.overall_data.aspect_data
        self.difficulty_data = self.overall_data.difficulty_data
        self.total_plays = new_overall_data.overall.plays
        self.total_wins = new_overall_data.overall.wins
        self.total_win_percentage = new_overall_data.overall.win_percentage
        self.solo_plays = new_overall_data.overall_true_solo_plays
        self.multihanded_solo_plays = new_overall_data.overall_solo_plays
        self.multiplayer_plays = new_overall_data.overall_multi_plays

        hlist = self.query_one("#best_hero_overall", OptionList)
        hlist.clear_options()
        hero_data = [f"{x["name"]} - {round(x["percent"]*100)}%" for x in self.overall_data.overall_specific_stats.get_best_x_heroes(10)]
        hlist.add_options(hero_data)
        hlist.highlighted = None

        vlist = self.query_one("#hardest_villain_overall", OptionList)
        vlist.clear_options()
        villain_data = [f"{x["name"]} - {round(x["percent"]*100)}%" for x in self.overall_data.overall_specific_stats.get_best_x_villains(10)]
        vlist.add_options(villain_data)
        vlist.highlighted = None

        tlist = self.query_one("#best_team_overall", OptionList)
        tlist.clear_options()
        team_data = [f"{x["name"]} - {round(x["percent"]*100)}%" for x in self.overall_data.overall_specific_stats.get_best_x_teams(3)]
        tlist.add_options(team_data)
        tlist.highlighted = None

        hwlist = self.query_one("#worst_hero_overall", OptionList)
        hwlist.clear_options()
        whero_data = [f"{x["name"]} - {round(x["percent"]*100)}%" for x in self.overall_data.overall_specific_stats.get_worst_x_heroes(10)]
        hwlist.add_options(whero_data)
        hwlist.highlighted = None

        vwlist = self.query_one("#easiest_villain_overall", OptionList)
        vwlist.clear_options()
        wvillain_data = [f"{x["name"]} - {round(x["percent"]*100)}%" for x in self.overall_data.overall_specific_stats.get_worst_x_villains(10)]
        vwlist.add_options(wvillain_data)
        vwlist.highlighted = None

        twlist = self.query_one("#worst_team_overall", OptionList)
        twlist.clear_options()
        wteam_data = [f"{x["name"]} - {round(x["percent"]*100)}%" for x in self.overall_data.overall_specific_stats.get_worst_x_teams(3)]
        twlist.add_options(wteam_data)
        twlist.highlighted = None

        hmlist = self.query_one("#most_hero_overall", OptionList)
        hmlist.clear_options()
        mhero_data = [f"{x["name"]} - {x["plays"]} plays" for x in self.overall_data.overall_specific_stats.get_most_x_heroes(10)]
        hmlist.add_options(mhero_data)
        hmlist.highlighted = None

        vmlist = self.query_one("#most_villain_overall", OptionList)
        vmlist.clear_options()
        mvillain_data = [f"{x["name"]} - {x["plays"]} plays" for x in self.overall_data.overall_specific_stats.get_most_x_villains(10)]
        vmlist.add_options(mvillain_data)
        vmlist.highlighted = None

        tmlist = self.query_one("#most_team_overall", OptionList)
        tmlist.clear_options()
        mteam_data = [f"{x["name"]} - {x["plays"]} plays" for x in self.overall_data.overall_specific_stats.get_most_x_teams(3)]
        tmlist.add_options(mteam_data)
        tmlist.highlighted = None
