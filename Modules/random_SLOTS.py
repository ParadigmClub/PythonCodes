# Made by Medhansh Kapoor - whirlxd.xyz
import random
# using classes to make the code more readable and maintainable
class SlotMachine:
    # declaring the themes and their respective emojis
    def __init__(self):
        self.themes = {
            "default": ['🍒', '🍋', '🍊', '🍉', '🍀', '🍌'],
            "deepSea": ['🐠', '🐚', '🦈', '🐢', '🐟', '🦐'],
            "desert": ['🐫', '🏜️', '☀️', '🌵', '🐪', '🦂']
        }
        self.theme_costs = {"default": 0, "deepSea": 20, "desert": 50}
        self.current_theme = "default"
        self.balance = 100
        self.spin_cost = 20
        self.multiplier_spin_cost = 40
        self.multiplier_winnings = 2
        self.jackpot = 1000
        self.bonus_round_trigger = ['🎁'] * 3
# function to spin the machine - returns a list of 3 emojis from the current theme
    def spinMachine(self):
        return [random.choice(self.themes[self.current_theme]) for i in range(3)]
# function to calculate the winnings based on the result and the multiplier
    def calculateWinnings(self, result, multiplier):
        base_winnings = 10 * multiplier
        if result == self.bonus_round_trigger:
            return self.startBonusRound(multiplier)
        if result[0] == result[1] == result[2]:
            return base_winnings + 90 * multiplier
        elif result[0] == result[1] or result[0] == result[2] or result[2] == result[1]:
            return base_winnings
        else:
            return 0
# function to start the bonus round
    def startBonusRound(self, multiplier):
        print("Congratulations! You've entered the bonus round.")
        return 20 * multiplier
# function to check if the result is a jackpot based on the emojis being repeated
    def checkJackpot(self, result):
        if result == ['🍌'] * 3:
            print("JACKPOT!!! You've won the progressive jackpot!")
            winnings = self.jackpot
            self.jackpot = 1000
            return winnings
        return 0
# function to list the themes available for purchase from the themes dictionary
    def listThemesForPurchase(self):
        purchasable_themes = {theme: cost for theme, cost in self.theme_costs.items() if theme != self.current_theme}
        print("Themes available for purchase:")
        for theme, cost in purchasable_themes.items():
            print(f"{theme}: {cost} credits")
# function to purchase a theme based on the user input
    def purchaseTheme(self):
        self.listThemesForPurchase()
        chosen_theme = input("Enter the name of the theme you'd like to purchase: ").strip().lower()
        if chosen_theme in self.theme_costs and chosen_theme != self.current_theme:
            cost = self.theme_costs[chosen_theme]
            if self.balance >= cost:
                print(f"Purchasing {chosen_theme} theme...")
                self.balance -= cost
                self.current_theme = chosen_theme
                print(f"You now own the {self.current_theme} theme!")
            else:
                print("Insufficient balance.")
        else:
            print("Invalid theme selected.")
# function to run the game and handle the user input
    def runGame(self):
        print("Welcome to the Slot Machine!\n")
        print("Rules:")
        print("- Spin the machine to match symbols.")
        print("- Matching three symbols wins credits based on the multiplier.")
        print("- Special multiplier doubles the stake.\n")

        while True:
            print(f"\nCurrent balance: {self.balance} credits | Current Theme: {self.current_theme}")
            if self.balance < self.spin_cost:
                print("You do not have enough credits to spin. Thanks for playing!") # if the user runs out of credits
                break

            user_input = input("Would you like to spin or buy a theme? (spin/buy): ").strip().lower()

            if user_input == 'spin':
                if self.balance >= self.multiplier_spin_cost:
                    user_choice = input("Do you want to spin with a multiplier? (yes/no): ").strip().lower()
                    if user_choice in ['yes', 'y', 'ye']:
                        self.balance -= self.multiplier_spin_cost
                        multiplier_effect = self.multiplier_winnings
                    else:
                        self.balance -= self.spin_cost
                        multiplier_effect = 1
                else:
                    self.balance -= self.spin_cost
                    multiplier_effect = 1

                result = self.spinMachine()
                print(f"Result: {result}")
                winnings = self.calculateWinnings(result, multiplier_effect)
                jackpot_winnings = self.checkJackpot(result)
                total_winnings = winnings + jackpot_winnings
                self.balance += total_winnings
                self.jackpot += 10
                print(f"You won {total_winnings} credits!")

            elif user_input == 'buy':
                self.purchaseTheme()

            else:
                print("Invalid input. Please enter 'spin' or 'buy'.")

if __name__ == "__main__":
    game = SlotMachine()
    game.runGame()