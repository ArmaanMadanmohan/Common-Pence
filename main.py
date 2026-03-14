import time
from modules.investment import Engine
from modules.cardplay import cards

def calculate_total_wealth(player_engine, cash):
    # For now, assuming 1 unit of stock/bond/etf/bank = $1 for simplicity.
    portfolio_value = player_engine.stock + player_engine.bonds + player_engine.etf + player_engine.bank
    return cash + portfolio_value

def print_week_lore(week):
    if week == 1:
        print("LORE: You're a fresh student with £100 to your name. Your goal this week is simple: survive and build an Emergency Fund. Learn the safety of the bank and low-risk bonds.")
        print("FINANCE TIP: Always pay yourself first. An emergency fund stops unexpected costs from putting you in debt.")
    elif week == 2:
        print("LORE: Textbooks are expensive, and inflation is eating your cash. It's time to learn about investing to make your money work for you.")
        print("FINANCE TIP: Cash loses value over time due to inflation. Investing in assets helps you outpace it.")
    elif week == 3:
        print("LORE: You're eyeing a summer internship, but you need a bigger safety net. Let's introduce ETFs (Exchange Traded Funds) for diversified, steady growth.")
        print("FINANCE TIP: Don't put all your eggs in one basket! ETFs spread your money across many companies, lowering risk.")
    elif week == 4:
        print("LORE: Graduation is looming. You want to start building a passive retirement pot early to take advantage of compound interest.")
        print("FINANCE TIP: Compound interest is the 8th wonder of the world. Earning interest on your interest is how real wealth is built.")
    elif week == 5:
        print("LORE: The Final Boss: Financial Independence. Can you manage high-risk stocks and balance your portfolio to secure your future financial wellbeing?")
        print("FINANCE TIP: High returns usually mean high risk. A balanced portfolio ensures you can weather market crashes.")

def game_loop():
    print("Welcome to Common Pence: The Student Finance Simulator'!")
    print("Your mission: Navigate 5 grueling weeks of student life, make smart financial decisions, and graduate with financial wellbeing.\n")
    time.sleep(1)
    
    # Initialize game variables
    game_engine = engine() # Instantiate your engine to track shares
    player_cash = 100      # Starting money
    
    # Game Constants
    TOTAL_WEEKS = 5
    DAYS_PER_WEEK = 5
    BASE_GOAL = 150       # The target goal for week 1 (adjusted for a $100 start)
    GOAL_MULTIPLIER = 1.5  # How much the goal increases each week

    for week in range(1, TOTAL_WEEKS + 1):
        # Calculate this week's target goal
        target_goal = int(BASE_GOAL * (GOAL_MULTIPLIER ** (week - 1)))
        
        print(f"\n{'='*45}")
        print(f"--- WEEK {week}: FINANCIAL MILESTONE {week} ---")
        print_week_lore(week)
        print(f"\nTarget Goal to reach by Friday: ${target_goal}")
        print(f"{'='*45}")
        
        for day in range(1, DAYS_PER_WEEK + 1):
            print(f"\n--- Week {week}, Day {day} ---")
            current_wealth = calculate_total_wealth(game_engine, player_cash)
            print(f"Current Cash: ${player_cash}")
            print(f"Total Wealth (Cash + Portfolio): ${current_wealth}")
            
            # --- DAILY ACTION PHASE ---
            print("\nAvailable actions: ")
            print("1. Make a Financial Decision (Play a Card)")
            print("2. Hold Positions (Skip Day)")
            
            choice = input("What would you like to do? (1/2): ")
            
            if choice == '1':
                # Simplified card selection
                print("\n🃏 Your Investment Opportunities:")
                for idx, c in enumerate(cards):
                    print(f"{idx}. {c.name}")
                
                try:
                    card_choice = int(input("\nSelect an opportunity to pursue (number): "))
                    selected_card = cards[card_choice]
                    
                    # Ensure the card uses our instantiated engine
                    selected_card.engine = game_engine
                    
                    # Call your existing play_card method
                    selected_card.play_card()
                    
                except (ValueError, IndexError):
                    print("❌ Invalid decision. You missed an opportunity today due to poor planning!")
                    
            elif choice == '2':
                print("You decided to hold your positions and let the market do its work.")
            else:
                print("Invalid choice. The day passed you by.")
                
            time.sleep(1) # Slight pause for readability
            
        # --- END OF WEEK CHECK ---
        print(f"\n{'*'*45}")
        print(f"--- END OF WEEK {week} PERFORMANCE REVIEW ---")
        final_wealth = calculate_total_wealth(game_engine, player_cash)
        print(f"📊 Final Wealth: ${final_wealth} / Target Milestone: ${target_goal}")
        
        if final_wealth >= target_goal:
            print("Congratulations! You made smart financial decisions and hit your milestone.")
            time.sleep(2)
        else:
            print("DEBT TRAP! You failed to meet your financial milestone.")
            print(f"You managed your finances well for {week - 1} weeks, but poor financial knowledge caught up to you.")
            print("Remember: Financial wellbeing comes from making the right financial decisions.")
            return # End the game immediately
            
    # If the loop finishes all 5 weeks successfully
    print("\n🏆 YOU WON! 🏆")
    print("You survived all 5 weeks, built a strong portfolio, and learned the power of compounding!")
    print("You are now ready to tackle real-world personal finance.")

if __name__ == "__main__":
    game_loop()
