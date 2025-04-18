from character_base_class import Character
from custom_settings import WIZARD_HEAL
# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=25)
        
    # Evil Wizard can regenerate health
    def regenerate(self):
        self.health += WIZARD_HEAL 
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"\n{self.name} regenerates {WIZARD_HEAL} health! Current health: {self.health}/{self.max_health}")
   
    #Evil Wizard deals 50% bonus damage
    def dark_blast(self,opponent):
        damage = int(self.basic_damage() * 1.5)
        opponent.health -= damage   
        print(f"{self.name} uses Dark Blast (deals 50% bonus damage) on {opponent.name}! for {damage} damage!")
        print(f"{opponent.name} Current Stats - Health: {max(0, opponent.health)}/{opponent.max_health}") 
        
        # Check if the opponent has a 'evadeNextAttack' attribute
        if hasattr(opponent, 'evadeNextAttack') and opponent.evadeNextAttack:
            print(f"\n{self.name} attacks {opponent.name}, but {opponent.name} evades the attack!")
            opponent.evadeNextAttack = False
            return
        # Check if the opponent has a 'arcaneShield' attribute
        if hasattr(opponent, 'arcaneShield') and opponent.arcaneShield:
            reduced_damage = damage // 2  # Reduce damage by 50%
            opponent.health -= reduced_damage
            print(f"\n{self.name} attacks {opponent.name}, with {damage} damage but Arcane Shield reduces the damage by 50%! Damage dealt: {reduced_damage}")
            opponent.arcaneShield = False  
            return
        

    