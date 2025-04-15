from character_base_class import Character
from custom_settings import ABILITY_TYPES
import random

class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=20) 
        base_damage = self.basic_damage()
        self.arcaneShield = False
        self.abilities = {
            "1": {
                "name": "Shadow Fire",
                "description": "Heals the Mage by 20% of their basic damage and deals additional 20% as bonus damage.",
                "type": ABILITY_TYPES[4],
                "damage": int(base_damage) + int(base_damage * 0.2),
                "heal": int(base_damage * 0.2)
            },
            "2": {
                "name": "Arcane Shield",
                "description": "Reduces damage taken by 50% for the next turn.",
                "type": ABILITY_TYPES[2],
                "damage": 0,
                "heal" : 0
            }
        }
       
    def special_ability(self, opponent):
        print("\nSpecial Abilities:")
        for key, ability in self.abilities.items():
            print(f"{key}. {ability['name']} - {ability['description']}")
        action = input("Which ability do you want to use? ")
        
        if action in self.abilities:
            ability = self.abilities[action]
            if ability["type"] == ABILITY_TYPES[4]: 
                #Type is universal
                damage = ability["damage"]
                opponent.health -= damage
                print(f"\n{self.name} uses {ability["name"]} on {opponent.name} for {damage} damage!")
                
                self.health += ability["heal"]
                if self.health > self.max_health:
                    self.health = self.max_health
                print(f"{self.name} heals {ability["heal"]}! Current health: {self.health}/{self.max_health}")
            elif ability["type"] == ABILITY_TYPES[2]: 
                #Type is block
                self.arcaneShield = True
                print(f"\n{self.name} activates {ability["name"]}! Damage taken will be reduced by 50% for the next turn.")
            return True
        else:
            print("Invalid choice. Please select a valid ability.")
                
            
