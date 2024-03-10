from textual.app import ComposeResult
from textual.reactive import reactive
from textual.containers import Vertical, Horizontal
from textual.widgets import Label, OptionList, Static
from analyze_data import HeroData, VillainData, TeamData, ExpansionData, OverallData, AspectData, DifficultyStats
from widgets.stats import SpecialPlays, AspectStats, DifficultyStatistics, TotalStats

class Name(Static):
     who = reactive("Name")

     def render(self) -> str:
         return f"{self.who}"

class HeroResults(Static):
    current_hero : reactive[HeroData] = reactive(HeroData("Bob"))
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
    current_villain : reactive[VillainData] = reactive(VillainData("Evil Bob"))
    aspect_data : reactive[AspectData] = reactive(AspectData())
    difficulty_data : reactive[DifficultyStats] = reactive(DifficultyStats())
    total_plays : reactive[int] = reactive(0)
    total_wins : reactive[int] = reactive(0)
    total_win_percentage : reactive[float] = reactive(0)
    name : reactive[str] = reactive("Evil Bob")


    def compose(self) -> ComposeResult:
        with Vertical(id="villain_results"):
            with Horizontal(id="villain_banner"):
                yield Label(f"Villain Statistics - ")
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

