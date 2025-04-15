from character_base_class import Character
from custom_settings import ABILITY_TYPES
import random

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)
        base_damage = self.basic_damage()
        self.abilities = {
            "1": {
                "name": "Double Strike",
                "description": "Deals double damage of the attack.",
                "type": ABILITY_TYPES[0], 
                "damage": int(base_damage * 2),
                "heal": 0
            },
            "2": {
                "name": "Critical Strike",
                "description": "Deals 100%-200% chance of the damage.",
                "type": ABILITY_TYPES[0],
                "damage": random.randint(int(base_damage), int(base_damage * 2)),
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
            
            if ability["type"] == ABILITY_TYPES[0]: 
                #Type is damage
                damage = ability["damage"]
                opponent.health -= damage
                print(f"\n{self.name} uses {ability['name']} on {opponent.name} for {damage} damage!")
            elif ability["type"] == ABILITY_TYPES[1]: 
                #Type is heal
                print(f"Not implemented yet!")
            return True
        else:
            print("Invalid choice. Please select a valid ability.")

