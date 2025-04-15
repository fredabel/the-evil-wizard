# Defeat the Evil Wizard

## Overview
The **Defeat the Evil Wizard** is a Python-based game where players can choose from various character classes, each with unique abilities, to engage in battles against opponents. The game features dynamic combat mechanics, including random attack power, special abilities, and defensive strategies.

---

## Features
- **Character Classes**:
  - **Warrior**: A strong melee fighter with abilities like `Double Strike` and `Critical Strike`.
  - **Mage**: A powerful spellcaster with abilities like `Shadow Fire` and `Arcane Shield`.
  - **Archer**: A ranged attacker with abilities like `Quick Shot` and `Evasion`.
  - **Paladin**: A holy warrior with abilities like `Holy Strike` and `Divine Shield`.
  - **Evil Wizard**: A regenerating opponent with the ability to heal itself during combat and a chance to use special ability.

- **Dynamic Combat**:
  - Randomized attack power for unpredictability.
  - Special abilities that enhance gameplay, such as healing, evasion, and damage boosts.
  - Defensive mechanics like shields and evasion to reduce or negate damage.

---

## Classes and Abilities

### Warrior
- **Double Strike**: Deals double the Warrior's attack power as damage.
- **Critical Strike**: Has a chance to deal 100%-200% of the Warrior's attack power as damage.

### Mage
- **Shadow Fire**: Heals the Mage by 20% of their basic damage and deals additional 20% as bonus damage.
- **Arcane Shield**: Reduces damage taken by 50% for the next turn.

### Archer
- **Quick Shot**: Deals 50 pure damage.
- **Evasion**: Allows the Archer to evade the next attack.

### Paladin
- **Holy Strike**: Deals extra damage by adding 20 to the Paladin's basic damage.
- **Divine Shield**: Evades the next attack completely.

### Evil Wizard
- **Regenerate**: Restores 5 health points each turn, up to the maximum health.
- **Dark Blast**: Deals 50% bonus damage 

---

## How to Play
1. **Choose a Character**:
   - Select a character class to play as (e.g., Warrior, Mage, Archer, Paladin).
2. **Battle Opponents**:
   - Use basic attacks or special abilities to defeat your opponent.
   - Manage your health and use defensive abilities strategically.
3. **Win or Lose**:
   - The game ends when either your character or the opponent is defeated.

---

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/fredabel/the-evil-wizard.git

2. Navigate to the project directory
   ```bash 
    cd the-evil-wizard
3. Run the game
   ```bash 
   python main.py 

## Future Enhancements
- Add more character classes with unique abilities.
- Create a graphical user interface (GUI) using a web-based front end.
- Enhance the user experience with visual elements such as health bars, animations, and interactive menus.

