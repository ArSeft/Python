import random


#   *MADE WITH PASSION BY SEFT* hope you enjoy my first text game, updates will come soon.


class Player:
    def __init__(self):
        self.level = 1
        self.hp = 100
        self.atk = 10
        self.xp = 0
        self.nextlvlxp = 50
        self.gold = 0
        self.inventory = {"Health Potion": 0}
        self.unlocked_mines = ["Bronze Mine"]  

    def gain_xp(self, amount):
        self.xp += amount
        if self.xp >= self.nextlvlxp:
            self.lvl_up()

    def lvl_up(self):
        self.level += 1
        self.hp += 20
        self.atk += 5
        self.xp = 0
        self.nextlvlxp = int(self.nextlvlxp * 1.5)  
        print(f"\n*** You leveled up! Now level {self.level} ***")
        self.unlock_mines()

    def unlock_mines(self):
        """ Unlocks new mines based on level """
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
        print(f"\nLevel: {self.level} \nHP: {self.hp} \nAttack: {self.atk} \nXP: {self.xp}/{self.nextlvlxp} \nGold: {self.gold}")
        print("\nInventory:")
        for item, amount in self.inventory.items():
            print(f"- {item}: {amount}")
        
        all_mines = ["Bronze Mine", "Silver Mine", "Gold Mine", "Diamond Mine"]
        print("\nMines:")
        for mine in all_mines:
            status = "Unlocked" if mine in self.unlocked_mines else "LOCKED"
            print(f"- {mine} ({status})")

    def use_health_potion(self):
        if self.inventory["Health Potion"] > 0:
            self.hp = 100
            self.inventory["Health Potion"] -= 1
            print("\nYou used a Health Potion! HP restored to 100.")
        else:
            print("\nYou don't have any Health Potions!")

class Enemy:
    def __init__(self, player_lvl):
        self.hp = random.randint(20, 40) + (player_lvl * 5)
        self.atk = random.randint(5, 10) + (player_lvl * 2)

def enter_mine(player):
    """ Allows player to select a mine and stay inside it """
    while True:
        print("\nChoose a mine:")
        all_mines = ["Bronze Mine", "Silver Mine", "Gold Mine", "Diamond Mine"]

        for index, mine in enumerate(all_mines):
            status = "Unlocked" if mine in player.unlocked_mines else "LOCKED"
            print(f"{index + 1}. {mine} ({status})")

        choice = input("\nSelect a mine: ")

        try:
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
    """ Player stays inside the mine until they choose to leave """
    print(f"\nYou have entered {mine_type}.")
    
    xp_rewards = {
        "Bronze Mine": (5, 10),
        "Silver Mine": (10, 20),
        "Gold Mine": (20, 35),
        "Diamond Mine": (40, 60)
    }

    while True:
        print("\n1. Mine for XP")
        print("2. Exit Mine")
        choice = input("\nWhat do you want to do? ")

        if choice == "1":
            reward = random.randint(*xp_rewards[mine_type])
            print(f"\nYou mined in {mine_type} and gained {reward} XP!")
            player.gain_xp(reward)
        elif choice == "2":
            print(f"\nYou left {mine_type}.")
            return
        else:
            print("\nInvalid choice!")

def fight(player):
    """ Handles the fight system and rewards player with XP and Gold """
    enemy = Enemy(player.level)
    print(f"\nA wild monster has appeared! \nAttack: {enemy.atk} \nHP: {enemy.hp}")

    while player.hp > 0 and enemy.hp > 0:
        action = input("Attack (1) or Run Away (2): ")
        if action == "1":
            damage = random.randint(player.atk // 2, player.atk)
            enemy.hp -= damage
            player.hp -= enemy.atk
            print(f"You hit for {damage}! Enemy HP: {max(enemy.hp, 0)}")
            print(f"Enemy hits for {enemy.atk}, Your HP: {max(player.hp, 0)}")
        elif action == "2":
            print("\nYou ran away!")
            return

    if player.hp > 0:
        xp_reward = random.randint(10, 20)
        gold_reward = random.randint(5, 15)
        print(f"\nYou defeated the enemy and gained {xp_reward} XP and {gold_reward} Gold!")
        player.gain_xp(xp_reward)
        player.gold += gold_reward
    else:
        print("\nYou were defeated... Respawning with full HP!")
        player.hp = 100

def shop(player):
    """ Allows player to buy health potions """
    print("\nWelcome to the shop!")
    print("1. Buy Health Potion (10 Gold)")
    print("2. Exit Shop")

    choice = input("\nWhat do you want to buy? ")
    if choice == "1":
        if player.gold >= 10:
            player.gold -= 10
            player.inventory["Health Potion"] += 1
            print("\nYou bought a Health Potion!")
        else:
            print("\nNot enough gold!")
    elif choice == "2":
        return
    else:
        print("\nInvalid choice!")

def main():
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
            enter_mine(player)
        elif choice == "2":
            fight(player)
        elif choice == "3":
            player.show_stats()
        elif choice == "4":
            shop(player)
        elif choice == "5":
            player.use_health_potion()
        elif choice == "6":
            print("\nExiting game, see you later!")
            break
        else:
            print("\nInvalid choice, try again.")

if __name__ == "__main__":
    main()
