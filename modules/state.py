import random
from modules.cards import cards
from modules.investment import Engine

class GameState:
    def __init__(self, starting_cash: float = 100.0):
        # Time tracking
        self.week = 1
        self.day = 1
        
        # Player resources
        self.cash = starting_cash
        self.engine = Engine()
        
        # Action & Card tracking
        self.actions_left = 3
        self.current_hand = []
        
        # UI Feedback
        self.message = "Welcome to Common Pence: The Student Finance Simulator!"

    def draw_new_hand(self, size: int = 5):
        """Draws a random sample of cards from the main deck."""
        self.current_hand = random.sample(cards, min(size, len(cards)))

    def set_message(self, text: str):
        """Updates the current feedback message to display to the user."""
        self.message = text

    def append_message(self, text: str):
        """Adds text to the existing message (useful for chaining events)."""
        self.message += f"\n{text}"

    def advance_day(self):
        """Advances the day, rolls over the week if necessary, and resets daily stats."""
        self.day += 1
        
        if self.day > 5:
            self.day = 1
            self.week += 1
            
        self.actions_left = 3
        self.draw_new_hand()
        
    def get_total_wealth(self) -> float:
        """Calculates total portfolio wealth plus liquid cash."""
        return self.cash + self.engine.get_total()
