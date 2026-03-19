"""Question 2 – Casino Slot Machine
Starter code:

rate    = [   2,     3,    9,     7,   11]
symbols = ["🍒", "🍋", "⭐", "🔔", "💎"]
money = 50
print("=== SLOT MACHINE === \n")
Goal: build a slot machine with 3 spinning slots

Rules:

Each spin shows 3 random symbols
The player starts with money50
Before each spin, ask the user how much they want to bet
The bet must be between and the current money1
The user can choose to quit the game
Update the player’s money after each round
Winning rules:

All 3 symbols different → player loses the bet
2 of a kind → player gets bet * rate
3 of a kind → player gets bet * 777 * rate
Spin examples:

🍒 🍋 ⭐ → all different → lose
💎 💎 🍋 → 2 of a kind → win bet * 11
⭐ ⭐ ⭐ → 3 of a kind → win bet * 777 * 9
🔔 🍒 🔔 → 2 of a kind → win bet * 7
Important:

The correct depends on the matching symbolrate
Example: 3 × 🍋 → use rate 3
Example: 2 × 💎 → use rate 11
Game ends when:

The player chooses to quit
OR the player runs out of money
Hints:

Use or random.choicerandom.randint
Keep track of symbol indexes to match the correct rate
First check for 3 matches, then for 2 matches"""

#libries
import random

#valius
rate    = [  2,    3,    9,    7,    11]
symbols = ["🍒", "🍋", "⭐", "🔔", "💎"]
money = 50
RED: str = "\033[31m"
GREEN: str = "\033[32m"
YELLOW: str = "\033[33m"
CLEAR: str = "\033[0m"

# functions
def welcome_for_casino() -> str:
    """
    This function printing welcome
    :return: string with welcome message
    """
    return "=== WELCOME FOR CASINO === \n"

def enter_choice() -> str:
    """
    This function is display choise you can choose 1 or 2 or 3
    :return: string with choice message
    """
    user_choice= input(f"{YELLOW}enter {RED}'1'{YELLOW} for to see the rules\nenter {RED}'2'{YELLOW} for continue\nenter {RED}'3'{YELLOW} for end the game{CLEAR}\n")
    return user_choice

def rules() -> None:
    """
    This function is printing the rules
    :return: None
    """
    print("=== RULES ===")
    print("symbols worth")
    for index in range(len(rate)):
        print(f"   {symbols[index]} = {rate[index]}")
    print("\nexplanation: how to get money")
    print(f"🍒 🍋 ⭐ → all different → {RED}lose{CLEAR}\n💎 💎 🍋 → 2 of the same kind → {GREEN}win{CLEAR} → the money is (bet * 11)")
    print(f"⭐ ⭐ ⭐ → 3 of the same kind → {GREEN}win{CLEAR} → the money is (bet * 777 * 9)\n🔔 🍒 🔔 → 2 of the same kind → {GREEN}win{CLEAR} → the money is (bet * 7)\n")


def how_match_bet(coin)-> int:
    """
    This function asking the user to input how much money you want to bet
    :param coin: is the money you have
    :return: int(bet)
    """
    while True:
        try :
            user_bet = int(input("how much bet? \n"))
            if user_bet > coin:
                print(f"{RED}ilegal value{CLEAR}\nplease put not more then your money \n")
            else:
                break
        except ValueError:
            print(f"{RED}input only numbers{CLEAR} \n")
    return user_bet

def spin_3_random_symbols(symbols: list)-> list:
    """
    This function spin 3 random symbols and printing that
    :param symbols: is the list of the symbols
    :return: 3 random symbols
    """
    three_random_symbols = []
    for _ in range(3):
        random_symbol = random.choice(symbols)
        three_random_symbols.append(random_symbol)
    return three_random_symbols

def is_win(three_symbols)-> None:
    """
    This function check if there is a win
    :param three_symbols: 3 random symbols
    :return:
    """
    return three_symbols[0] == three_symbols[1] == three_symbols[2] or three_symbols[0] == three_symbols[1] != three_symbols[2] or three_symbols[0] != three_symbols[1] == three_symbols[2] or three_symbols[0] == three_symbols[2] != three_symbols[1]

def which_symbol_is_double(three_symbols) -> str|None:
    """
    This function check if there is a double in the three_symbols
    :param three_symbols: 3 random symbols
    :return: symbol (the double one)
    """
    new_three_symbols = set(three_symbols)
    for symbol in new_three_symbols:
        if three_symbols.count(symbol) == 2:
            return symbol

def which_symbol_is_triple(three_symbols) -> str|None:
    """
    This function check if there is a triple in the three_symbols
    :param three_symbols: 3 random symbols
    :return: symbol (the triple one)
    """
    new_three_symbols = set(three_symbols)
    for symbol in new_three_symbols:
        if three_symbols.count(symbol) == 3:
            return symbol

def is_triple(three_symbols) -> bool:
    """
    this function check if there is a triple win
    :param three_symbols: 3 random symbols
    :return: bool
    """
    return three_symbols[0] == three_symbols[1] == three_symbols[2]

def rate_symbol(symbol: str, symbols: list, rate: list) -> int|None:
    """
    This function change the symbol to rate symbol for update the money
    :param symbol: symbol
    :param symbols: list of symbols
    :param rate: list of rates
    :return: int(rate_symbol)
    """
    for i in range(len(symbols)):
        if symbol == symbols[i]:
            return rate[i]


#game
print(welcome_for_casino())
user_choice = enter_choice()
while True:

    #rules
    if user_choice == "1":
        rules()
        user_choice = enter_choice()

    #game
    elif money != 0 and user_choice == '2':
        print(f"your balnce is:{YELLOW}{money}{CLEAR}")
        bet = how_match_bet(money)
        money = money - bet
        three_symbols = spin_3_random_symbols(symbols)
        print(three_symbols)
        if is_win(three_symbols):
            if is_triple(three_symbols):
                symbol_triple = which_symbol_is_triple(three_symbols)
                current_rate = rate_symbol(symbol_triple,symbols,rate)
                money = money + (bet * 777 * current_rate)
                print(f"{GREEN}you winner{CLEAR} ✨💰✨")
            else:
                symbol_double = which_symbol_is_double(three_symbols)
                current_rate = rate_symbol(symbol_double, symbols, rate)
                money = money + (bet * current_rate)
                print(f"{GREEN}you winner{CLEAR}")
        else:
            print(f"{RED}You lost this round{CLEAR}")
        if money != 0:
            end_game = input("enter 'end' to finish or enter for continue\n")
            if end_game.lower() == "end":
                user_choice = "3"

    #byebye
    elif user_choice == "3" or money == 0:
        if money == 0:
            print(f"{RED}no money no game{CLEAR}")
        print("=== GOOD BYE ===")
        break

    else:
        print("=== INVALID CHOICE ===")
        user_choice = enter_choice()
