from character_class_map import *
import random
# Function to create player character based on user input
def create_character():
    print("Choose your character:")
    for key, character in enumerate(CHARACTER_LIST, 1):
        # Iterate CHARACTER_LIST
        print(f"{key}. {character}")
    
    hero_choice = input("Enter the number of your class choice: ")

    if hero_choice.isdigit() and 0 <= int(hero_choice) - 1 < len(CHARACTER_LIST):
        # Get the class from the CHARACTER_CLASS_MAP dictionary
        hero_class = CHARACTER_CLASS_MAP[CHARACTER_LIST[int(hero_choice) - 1]]
        # Display the character selected
        print(f"You choose {CHARACTER_LIST[int(hero_choice) - 1]}!")
        name = input("Enter your character's name: ")
        return hero_class(name)
    else:
        #Proceed to default character
        print(f"Invalid choice. Defaulting to {CHARACTER_LIST[0]}.")
        name = input("Enter your character's name: ")
        return default_class(name)

# Battle function with user menu for actions
def battle(player, wizard):
    
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")
        print("5. Back to Select Character ")
        
        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
            # Evil Wizard's turn to attack and regenerate
            if wizard.health > 0:
                wizard.regenerate()
                wizard_attack(player, wizard) 
        elif choice == '2':
            # Call the special ability here
            while True: 
                ability = player.special_ability(wizard)
                if ability:
                    #If valid ability input
                    if wizard.health > 0:
                        wizard.regenerate()
                        wizard_attack(player, wizard) 
                    break        
        elif choice == '3':
            # Call the heal method here
            player.heal()
            # Evil Wizard's turn to attack and regenerate
            if wizard.health > 0:
                wizard.regenerate()
                wizard_attack(player, wizard)
        elif choice == '4':
            player.display_stats() #Display player's stats
            wizard.display_stats() #Display wizard's stats
        elif choice == '5':
            return False
        else:
            print("Invalid choice, try again.")
            continue
        
        if player.health <= 0:
            print(f"{player.name} has been defeated by {wizard.name}. Game Over. Try again!")
            break

    if wizard.health <= 0:
        print(f"Congratulations! {player.name} has defeated {wizard.name}! You are victorious!\n")

#Apply the wizard attack method get a chance to burst
def wizard_attack(player, wizard):
    chance = random.randint(1,10)
    # print(chance)
    if 5 <= chance:
        wizard.dark_blast(player) # Call the dark_blast ability
    else:
        wizard.attack(player)
        
# Main function to handle the flow of the game
def main():
    while True:
        # Character creation phase
        player = create_character()

        # Evil Wizard is created
        wizard = EvilWizard("The Dark Wizard")
    
        # Start the battle
        battle(player, wizard)

if __name__ == "__main__":
    main()