from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Button, Label, Input, Static
from textual.containers import Vertical, Horizontal

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

    def on_button_pressed(self) -> None:
        self.app.notify(f"{self.id} pressed")

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
            yield Static(round)
            yield Horizontal(
                    Budget("£500"),
                    OwnedAssets("Assets")
                    )
            yield Vertical(
                    Assets("Assets go here"),
                    Static("Messages here"),
                    )
            yield Vertical(
                Horizontal(
                    Card("Card1", id="hand1"),
                    Card("Card2", id="hand2"),
                    Card("Card3", id="hand3"),
                    Card("Card4", id="hand4"),
                    Card("Card5", id="hand5"),
                    ),
                Button("skip", id="skip", variant="primary"),
                
                )
            yield Footer()

round = "Round 1 - Stage 2"
CommonPence().run()
