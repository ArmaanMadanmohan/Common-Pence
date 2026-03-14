from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Button, Label, Input, Static
from textual.containers import Vertical, Horizontal
from modules.state import GameState

class Card(Button):
    DEFAULT_CSS = """
    Card {
            color: black !important;
            background: #eeeeee !important;
            border: solid black;
            margin: 2 2;
            width: 1fr;
            }
    Card:hover {
            background: #eeeeff !important;
            }
    """
    def __init__(self, label:str, **kwargs):
        super().__init__(label, **kwargs)


class Budget(Static):
    DEFAULT_CSS = """
    Budget {
            color: black !important;
            background: yellow !important;
            padding: 1 2;
            margin: 2 2;
            height: 3;
            width: 16;
            }
    """
    def __init__(self, label:str, **kwargs):
        super().__init__(label, **kwargs)
class OwnedAssets(Static):
    DEFAULT_CSS = """
    OwnedAssets {
            color: black !important;
            background: yellow !important;
            padding: 1 2;
            margin: 2 2;
            height: 10;
            width: 16;
            dock: right;
            }
    """
    def __init__(self, label:str, **kwargs):
        super().__init__(label, **kwargs)

class Assets(Static):
    DEFAULT_CSS = """
    Assets {
            background: green !important;
            padding: 1 0;
            margin: 5 0;
            }
    """
    def __init__(self, label:str, **kwargs):
        super().__init__(label, **kwargs)

class CommonPence(App):
    def __init__(self):
        super().__init__()
        self.state = GameState(starting_cash=100.0)
        self.state.draw_new_hand()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.app.notify(f"{self.id} pressed")
        id = 0
        match self.id:
            case "a0": id = 0
            case "a1": id = 1
            case "a2": id = 2
            case "a3": id = 3
            case "a4": id = 4

        card = self.state.current_hand.pop(id)
        card.play_card(self.state.cash)

    CSS = """
    #hand {
            dock:bottom;
            align-horizontal: center;
            padding: 1 2;
            height: 7;
            }
    Button {
            padding: 1 0;
            }
    Title {
            text-align: center;
            }
    Static {
            text-align: center;
            }
    """

    def compose(self) -> ComposeResult:
            yield Header()
            yield Static(f"Week {self.state.week} Day {self.state.day}")
            yield Horizontal(
                    Budget(f"£{self.state.cash}"),
                    OwnedAssets(f"{self.state.engine.get_all()}")
                    )
            yield Vertical(
                    Assets(f"{self.state.engine.tick()}"),
                    Static(f"{self.state.message}"),
                    )
            yield Vertical(
                Horizontal(
                    Card(self.state.current_hand[0].name, id="a0"),
                    Card(self.state.current_hand[1].name, id="a1"),
                    Card(self.state.current_hand[2].name, id="a2"),
                    Card(self.state.current_hand[3].name, id="a3"),
                    Card(self.state.current_hand[4].name, id="a4"),
                    ),
                Button("skip", id="skip", variant="primary"),
                
                )
            yield Footer()

round = "Round 1 - Stage 2"
CommonPence().run()
