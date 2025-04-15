from player_classes.dark_wizard import EvilWizard
from player_classes.warrior import Warrior
from player_classes.mage import Mage
from player_classes.archer import Archer
from player_classes.paladin import Paladin

CHARACTER_CLASS_MAP = {
    "Warrior": Warrior,
    "Mage": Mage,
    "Archer": Archer,
    "Paladin": Paladin
}

CHARACTER_LIST = list(CHARACTER_CLASS_MAP.keys()) #["Warrior", "Mage", "Archer","Paladin"]
default_class = CHARACTER_CLASS_MAP[CHARACTER_LIST[0]] #Warrior()