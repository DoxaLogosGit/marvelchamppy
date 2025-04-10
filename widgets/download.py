from textual.widgets import Label, LoadingIndicator
from textual.screen import ModalScreen
from textual.app import ComposeResult
from textual.containers import Vertical
from analyze_data import Statistics
import gui_utils


class DownloadScreen(ModalScreen[Statistics]):

    def compose(self) -> ComposeResult:
        with Vertical(): 
                yield Label("Downloading Data")
                yield LoadingIndicator(id="load")
    
    def on_show(self) -> None:
        plays = gui_utils.download_data()
        parsed_data = gui_utils.read_data(plays)
        self.dismiss(parsed_data)
        