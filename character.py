import random  # Import the random module

class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  # Store the original health for maximum health
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

    def attack(self, opponent):
        # Generate a random attack power between 70% and 100% of the base attack power
        damage = random.randint(int(self.attack_power * 0.7), int(self.attack_power))
        
        # Check if the opponent has a 'evadeNextAttack' attribute
        if hasattr(opponent, 'evadeNextAttack') and opponent.evadeNextAttack:
            print(f"\n{self.name} attacks {opponent.name}, but {opponent.name} evades the attack!")
            opponent.evadeNextAttack = False
            return
        
        if hasattr(opponent, 'arcaneShield') and opponent.arcaneShield:
            reduced_damage = damage // 2  # Reduce damage by 50%
            opponent.health -= reduced_damage
            print(f"\n{self.name} attacks {opponent.name}, with {damage} damage but Arcane Shield reduces the damage by 50%! Damage dealt: {reduced_damage}")
            opponent.arcaneShield = False  
            return
        
        #Proceed with the attack
        opponent.health -= damage   
        print(f"\n{self.name} attacks {opponent.name} for {damage} damage!")  
        
        # Print the current stats of the opponent
        print(f"{opponent.name} Current Stats - Health: {opponent.health}/{opponent.max_health}")   
         
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

    # Add your heal method here
    def heal(self):
        #Don't allow the health to exceed the max_health
        self.health += 10 
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"{self.name} regenerates 10 health! Current health: {self.health}/{self.max_health}")


# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)  # Boost health and attack power

    # Add your power attack method here
    def special_ability(self, opponent):
        print("\nAbilities:")
        print("1. Double Damage")
        print("2. Critical Strike")
        action = input("Which ability do you want to use? ")

        if action == "1":
            # Double Damage: Deals double damage
            normal_damage = random.randint(int(self.attack_power * 0.7), int(self.attack_power))
            damage = normal_damage * 2
            opponent.health -= damage
            print(f"\n{self.name} uses Power Strike on {opponent.name} for  {damage} damage!")
            
        elif action == "2":
            # Critical Strike: Chance 100%-200%  Critical Strike
            damage = random.randint(int(self.attack_power), int(self.attack_power * 2))
            opponent.health -= damage
            print(f"\n{self.name} uses Critical Strike on {opponent.name} for {damage} damage!")
        else:
            print("Invalid choice. Please select a valid ability.")
        
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")


# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)  # Boost attack power
        self.arcaneShield = False
       
    def special_ability(self, opponent):
        print("\nAbilities:")
        print("1. Shadow Fire")
        print("2. Arcane Shield")
        action = input("Which ability do you want to use? ")

        if action == "1":
            # Generate a random attack power between 70% and 100% of the base attack power
            attack = random.randint(int(self.attack_power * 0.7), int(self.attack_power))
            
            #Shadow Fire: Heals the Mage by 20% of their of their attack power and deals an additional 20% as bonus damage to the opponent.
            shadow_fire = int(attack * 0.2)
            damage = attack + shadow_fire
           
            #Total attack damage
            opponent.health -= damage
            print(f"\n{self.name} uses Shadow Fire on {opponent.name} for {damage} damage!")
            
            self.health += shadow_fire
            if self.health > self.max_health:
                self.health = self.max_health
            print(f"{self.name} heals {shadow_fire}! Current health: {self.health}/{self.max_health}")
           
        elif action == "2":
            # Arcane Shield: Reduces damage taken by 50% for the next turn
            self.arcaneShield = True
            print(f"\n{self.name} activates Arcane Shield! Damage taken will be reduced by 50% for the next turn.")
        else:
            print("Invalid choice. Please select a valid ability.")
        
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
    
#Archer Class
class Archer(Character):
    def __init__(self,name):
        super().__init__(name, health=120, attack_power=40)
        self.evadeNextAttack = False
    
    def special_ability(self, opponent):
        print("\nAbilities:")
        print("1. Quick Shot")
        print("2. Evasion")
        action = input("Which ability do you want to use? ")
        
        if action == "1":
            self.attack_power = 50
            print(f"\n{self.name} uses Holy Strike on {opponent.name} for {self.attack_power} pure damage!")
            opponent.health -= self.attack_power
            print(f"{self.name} attacks {opponent.name} for {self.attack_power} damage!")   
        elif action == "2":
            self.evadeNextAttack = True
            print(f"\n{self.name} activates Evasion! The next attack will deal no damage.")
        else:
            print("Invalid choice. Please select a valid ability.")
        
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

#Paladin Class
class Paladin(Character):
    def __init__(self,name):
        super().__init__(name, health=120, attack_power=40)
        self.evadeNextAttack = False
        
    def special_ability(self, opponent):
        print("\nAbilities:")
        print("1. Holy Strike")
        print("2. Divine Shield")
        action = input("Which ability do you want to use? ")
        
        if action == "1":
            # Generate a random attack power between 70% and 100% of the base attack power
            normal_damage = random.randint(int(self.attack_power * 0.7), int(self.attack_power))
            
            # Holy Strike: Deals extra damage
            damage = normal_damage + 20  # Add 20 extra damage
            
            opponent.health -= damage
            print(f"\n{self.name} uses Holy Strike on {opponent.name} for {damage} damage!")
            if opponent.health <= 0:
                print(f"{opponent.name} has been defeated!")
        elif action == "2":
            # Divine Shield: Evade the next attack
            self.evadeNextAttack = True
            print(f"\n{self.name} activates Divine Shield! The next attack will deal no damage.")
        else:
            print("Invalid choice. Please select a valid ability.")
        
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)  # Lower attack power
    
    # Evil Wizard's special ability: it can regenerate health
    def regenerate(self):
        self.health += 5  # Lower regeneration amount
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"{self.name} regenerates 5 health! Current health: {self.health}/{self.max_health}")