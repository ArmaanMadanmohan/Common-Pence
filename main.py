import time
from modules.investment import engine
from modules.cardplay import cards

def calculate_total_wealth(player_engine, cash):
    # For now, assuming 1 unit of stock/bond/etf/bank = $1 for simplicity.
    # You can expand this later using the share_price from your stock class.
    portfolio_value = player_engine.stock + player_engine.bonds + player_engine.etf + player_engine.bank
    return cash + portfolio_value

def game_loop():
    print("Welcome to the Investment Hackathon Game!")
    
    # Initialize game variables
    game_engine = engine() # Instantiate your engine to track shares
    player_cash = 500      # Starting money
    
    # Game Constants
    TOTAL_WEEKS = 5
    DAYS_PER_WEEK = 5
    BASE_GOAL = 1000       # The target goal for week 1
    GOAL_MULTIPLIER = 1.5  # How much the goal increases each week

    for week in range(1, TOTAL_WEEKS + 1):
        # Calculate this week's target goal
        target_goal = int(BASE_GOAL * (GOAL_MULTIPLIER ** (week - 1)))
        
        print(f"\n{'='*30}")
        print(f"--- WEEK {week} START ---")
        print(f"Target Goal to reach by Friday: ${target_goal}")
        print(f"{'='*30}")
        
        for day in range(1, DAYS_PER_WEEK + 1):
            print(f"\n--- Week {week}, Day {day} ---")
            current_wealth = calculate_total_wealth(game_engine, player_cash)
            print(f"Current Cash: ${player_cash}")
            print(f"Total Wealth (Cash + Portfolio): ${current_wealth}")
            
            # --- DAILY ACTION PHASE ---
            print("Available actions: ")
            print("1. Play a Card")
            print("2. Skip Day")
            
            choice = input("What would you like to do? (1/2): ")
            
            if choice == '1':
                # Simplified card selection
                print("\nYour Cards:")
                for idx, c in enumerate(cards):
                    print(f"{idx}. {c.name}")
                
                try:
                    card_choice = int(input("\nSelect a card to play (number): "))
                    selected_card = cards[card_choice]
                    
                    # Ensure the card uses our instantiated engine
                    selected_card.engine = game_engine 
                    
                    # Call your existing play_card method
                    selected_card.play_card()
                    
                    # NOTE: You will need to deduct money from player_cash 
                    # based on what they invested in your cardplay logic!
                    
                except (ValueError, IndexError):
                    print("Invalid card selection. You missed your chance today!")
                    
            elif choice == '2':
                print("You decided to hold your positions and skip the day.")
            else:
                print("Invalid choice. Day skipped.")
                
            time.sleep(1) # Slight pause for readability
            
        # --- END OF WEEK CHECK ---
        print(f"\n{'*'*30}")
        print(f"--- END OF WEEK {week} ---")
        final_wealth = calculate_total_wealth(game_engine, player_cash)
        print(f"Final Wealth: ${final_wealth} / Target: ${target_goal}")
        
        if final_wealth >= target_goal:
            print("🎉 Congratulations! You met the weekly goal. Moving to the next week...")
            time.sleep(2)
        else:
            print("💀 GAME OVER! You failed to meet the weekly target.")
            print(f"You survived for {week - 1} weeks.")
            return # End the game immediately
            
    # If the loop finishes all 5 weeks successfully
    print("\n🏆 YOU WON THE GAME! You survived all 5 weeks and became a master investor!")

if __name__ == "__main__":
    game_loop()
