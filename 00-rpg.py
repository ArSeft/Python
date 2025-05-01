import random
import os

class Player:
    """
    Represents the player character in the RPG game.

    Attributes:
        level (int): The player's current level.
        hp (int): The player's current health points.
        maxhp (int): The player's maximum health points.
        atk (int): The player's attack power.
        xp (int): The player's current experience points.
        nextlvlxp (int): The experience points required to reach the next level.
        gold (int): The player's current gold amount.
        health_potions (dict): Inventory of health potions.
        unlocked_mines (list): List of mines unlocked by the player.
    """

    def __init__(self):
        """
        Initializes a new Player instance with default attributes.
        """
        self.level = 1
        self.hp = 100
        self.maxhp = 100
        self.atk = 10
        self.xp = 0
        self.nextlvlxp = 50
        self.gold = 0
        self.health_potions = {"Health Potion": 0}
        self.unlocked_mines = ["Bronze Mine"]

    def gain_xp(self, amount):
        """
        Adds experience points to the player and levels up if the required XP is reached.

        Args:
            amount (int): The amount of XP to add.
        """
        self.xp += amount
        if self.xp >= self.nextlvlxp:
            self.lvl_up()

    def lvl_up(self):
        """
        Levels up the player, increasing stats and unlocking new mines if applicable.
        """
        self.level += 1
        self.maxhp += 20
        self.hp = self.maxhp
        self.atk += 5
        self.xp = 0
        self.nextlvlxp = int(self.nextlvlxp * 1.5)
        print(f"\n*** You leveled up and recovered from your wounds! Now level {self.level}***")
        self.unlock_mines()

    def unlock_mines(self):
        """
        Unlocks new mines based on the player's level.
        """
        mines = {
            3: "Silver Mine",
            5: "Gold Mine",
            8: "Diamond Mine"
        }
        for lvl, mine in mines.items():
            if self.level >= lvl and mine not in self.unlocked_mines:
                self.unlocked_mines.append(mine)
                print(f"\n*** You have unlocked {mine}! ***")

    def show_stats(self):
        """
        Displays the player's current stats, inventory, and unlocked mines.
        """
        print(f"\nLevel: {self.level} \nHP: {self.hp}/{self.maxhp} \nAttack: {self.atk} \nXP: {self.xp}/{self.nextlvlxp} \nGold: {self.gold}")
        print("\nInventory:")
        for item, amount in self.health_potions.items():
            print(f"- {item}: {amount}")
        
        all_mines = ["Bronze Mine", "Silver Mine", "Gold Mine", "Diamond Mine"]
        print("\nMines:")
        for mine in all_mines:
            status = "Unlocked" if mine in self.unlocked_mines else "LOCKED"
            print(f"- {mine} ({status})")

    def use_health_potion(self):
        """
        Uses a health potion to restore the player's health to maximum.
        If no health potions are available, notifies the player.
        """
        if self.health_potions["Health Potion"] > 0:
            self.hp = self.maxhp
            self.health_potions["Health Potion"] -= 1
            print(f"\nYou used a Health Potion! Now at full health ({self.hp}HP). ")
            input("\nPress any key...")
            clear_console()
        else:
            clear_console()
            print("\nYou don't have any Health Potions!")
            input("\nPress any key...")
            clear_console()

class Enemy:
    """
    Represents an enemy in the RPG game.

    Attributes:
        hp (int): The enemy's health points.
        atk (int): The enemy's attack power.
    """

    def __init__(self, player_lvl):
        """
        Initializes a new Enemy instance with stats based on the player's level.

        Args:
            player_lvl (int): The player's current level, used to scale the enemy's stats.
        """
        self.hp = random.randint(20, 40) + (player_lvl * 5)
        self.atk = random.randint(5, 10) + (player_lvl * 2)

def enter_mine(player):
    """
    Allows the player to select and enter a mine.

    Args:
        player (Player): The player instance.
    """
    while True:
        print("\nChoose a mine:")
        all_mines = ["Bronze Mine", "Silver Mine", "Gold Mine", "Diamond Mine"]

        for index, mine in enumerate(all_mines):
            status = "Unlocked" if mine in player.unlocked_mines else "LOCKED"
            print(f"{index + 1}. {mine} ({status})")

        choice = input("\nSelect a mine: ")

        try:
            clear_console()
            choice = int(choice) - 1
            if 0 <= choice < len(all_mines):
                mine_type = all_mines[choice]
                if mine_type in player.unlocked_mines:
                    mine_loop(player, mine_type)
                    return
                else:
                    print("\nThat mine is locked! Level up to unlock it.")
            else:
                print("\nInvalid selection!")
        except ValueError:
            print("\nInvalid input! Please enter a number.")

def mine_loop(player, mine_type):
    """
    Handles the mining process in a selected mine.

    Args:
        player (Player): The player instance.
        mine_type (str): The type of mine the player has entered.
    """
    print(f"\nYou have entered {mine_type}.")
    
    xp_rewards = {
        "Bronze Mine": (5, 10),
        "Silver Mine": (10, 20),
        "Gold Mine": (20, 35),
        "Diamond Mine": (40, 60)
    }

    while True:
        print("\nENTER. Mine for XP")
        print("1. Exit Mine")
        choice = input("\nWhat do you want to do? ")

        if choice == "":
            clear_console()
            reward = random.randint(*xp_rewards[mine_type])
            print(f"\nYou mined in {mine_type} and gained {reward} XP!")
            player.gain_xp(reward)
        elif choice == "1":
            print(f"\nYou left {mine_type}.")
            clear_console()
            return
        else:
            clear_console()
            print("\nInvalid choice!")
            input("\nPress any key...")
            clear_console()

def fight(player):
    """
    Initiates a fight between the player and an enemy.

    Args:
        player (Player): The player instance.
    """
    enemy = Enemy(player.level)
    print(f"\nA wild monster has appeared! \nAttack: {enemy.atk} \nHP: {enemy.hp}")

    while player.hp > 0 and enemy.hp > 0:
        action = input("\nAttack (1) or Run Away (2): ")
        if action == "1":
            clear_console()
            damage = random.randint(player.atk // 2, player.atk)
            enemy.hp -= damage
            player.hp -= enemy.atk
            print(f"\nYou hit for {damage}! \nEnemy HP: {max(enemy.hp, 0)}")
            print(f"\nEnemy hits for {enemy.atk} \nYour HP: {max(player.hp, 0)}")
        elif action == "2":
            clear_console()
            print("\nYou ran away!")
            return
        else:
            input("Invalid input...")

    if player.hp > 0:
        xp_reward = random.randint(10, 20)
        gold_reward = random.randint(5, 15)
        clear_console()
        print(f"\nYou defeated the enemy and gained {xp_reward} XP and {gold_reward} Gold!")
        player.gain_xp(xp_reward)
        player.gold += gold_reward
        input("\nPress any key...")
        clear_console()
    else:
        print("\nYou were defeated... Respawning with full HP!")
        player.hp = player.maxhp

def clear_console():
    """
    Clears the console screen.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def shop(player):
    """
    Allows the player to purchase items from the shop.

    Args:
        player (Player): The player instance.
    """
    print(f"\nWelcome to the shop! You have {player.gold} Gold!")
    print("\n1. Buy Health Potion (10 Gold)")
    print("2. Exit Shop")

    choice = input("\nWhat do you want to buy? ")
    if choice == "1":
        if player.gold >= 10:
            player.gold -= 10
            player.health_potions["Health Potion"] += 1
            clear_console()
            print(f"\nYou bought a Health Potion! ")
            input("\nPress any key...")
            clear_console()
        else:
            print("\nNot enough gold!")
    elif choice == "2":
        return
    else:
        print("\nInvalid choice!")

def main():
    """
    The main game loop, allowing the player to choose actions such as mining, fighting, or shopping.
    """
    player = Player()
    while True:
        print("\n1. Mine")
        print("2. Fight")
        print("3. Stats")
        print("4. Shop")
        print("5. Use Health Potion")
        print("6. Quit")

        choice = input("\nWhat do you want to do? ")

        if choice == "1":
            clear_console()
            enter_mine(player)
        elif choice == "2":
            clear_console()
            fight(player)
        elif choice == "3":
            clear_console()
            player.show_stats()
            while True:
                exitstats = input("\nEnter to return: ")
                if exitstats == "":
                    clear_console()
                    break
                else:
                    print("\nInvalid input, press enter!")                 
        elif choice == "4":
            clear_console()
            shop(player)
        elif choice == "5":
            clear_console()
            player.use_health_potion()
        elif choice == "6":
            clear_console()
            print("\nExiting game, see you later!")
            break
        else:
            clear_console()
            print("\nInvalid choice, try again.")
            input("\nPress any key...")
            clear_console()

if __name__ == "__main__":
    main()
