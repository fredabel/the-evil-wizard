import random  # Import the random module
from custom_settings import HEAL

class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.basic_damage = self.calculate_basic_damage()  # Calculate basic damage dynamically
        self.max_health = health  # Store the original health for maximum health
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

    def calculate_basic_damage(self):

        #Calculates the basic damage as a random value between 80% and 100% of the attack power.
        return random.randint(int(self.attack_power * 0.8), int(self.attack_power))
        
    def attack(self, opponent):
        # Check if the opponent has a 'evadeNextAttack' attribute
        if hasattr(opponent, 'evadeNextAttack') and opponent.evadeNextAttack:
            print(f"\n{self.name} attacks {opponent.name}, but {opponent.name} evades the attack!")
            opponent.evadeNextAttack = False
            return
        
        # Check if the opponent has a 'arcaneShield' attribute
        if hasattr(opponent, 'arcaneShield') and opponent.arcaneShield:
            reduced_damage = self.basic_damage // 2  # Reduce damage by 50%
            opponent.health -= reduced_damage
            print(f"\n{self.name} attacks {opponent.name}, with {self.basic_damage} damage but Arcane Shield reduces the damage by 50%! Damage dealt: {reduced_damage}")
            opponent.arcaneShield = False  
            return
        
        #Proceed with the attack
        opponent.health -= self.basic_damage   
        print(f"\n{self.name} attacks {opponent.name} for {self.basic_damage} damage!")  
        
        # Print the current stats of the opponent
        print(f"{opponent.name} Current Stats - Health: {opponent.health}/{opponent.max_health}")   
         
        # if opponent.health <= 0:
        #     print(f"{opponent.name} has been defeated!")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

    # Add your heal method here
    def heal(self):
        #Don't allow the health to exceed the max_health
        self.health += HEAL
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"{self.name} regenerates 10 health! Current health: {self.health}/{self.max_health}")


