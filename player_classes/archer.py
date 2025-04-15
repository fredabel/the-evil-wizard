from character_base_class import Character
from custom_settings import ABILITY_TYPES
import random

class Archer(Character):
    def __init__(self,name):
        super().__init__(name, health=120, attack_power=20)
        base_damage = self.basic_damage()
        self.evadeNextAttack = False
        
        self.abilities = {
            "1": {
                "name": "Quick Shot",
                "description": "Deals 50 pure damage.",
                "type": ABILITY_TYPES[0],
                "damage": 50,  # Fixed damage
                "heal": 0
            },
            "2": {
                "name": "Manta Dodge",
                "description": "Evades the next attack completely.",
                "type": ABILITY_TYPES[3],
                "damage": 0,
                "heal": 0
            }
        }
    
    def special_ability(self, opponent):
        print("\nSpecial Abilities:")
        for key, ability in self.abilities.items():
            print(f"{key}. {ability['name']} - {ability['description']}")

        action = input("Which ability do you want to use? ")

        if action in self.abilities:
            ability = self.abilities[action]
            if ability["type"] == "damage":
                # Type is damage
                damage = ability["damage"]
                opponent.health -= damage
                print(f"\n{self.name} uses {ability['name']} on {opponent.name} for {damage} damage!")
            elif ability["type"] == ABILITY_TYPES[3]:
                # Type is evasion
                self.evadeNextAttack = True
                print(f"\n{self.name} uses {ability['name']}! The next attack will deal no damage.")
            return True
        else:
            print("Invalid choice. Please select a valid ability.")