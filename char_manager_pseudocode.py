# MH 1st character management

# dictionary to contain all characters
chracters = {
    # FOR ALL CHARACTERS
    # race and class stored in tuple
    # skills stored a set
    # atributtes in nested dictionary
    # inventory in list
    "example_char" : {
        "race" : ("Dragonborn"),
        "class" : ("White Mage"),
        "level" : 10,
        "atributtes" : {
            "MP" : 1,
            "HP" : 2,
            "Str" : 3,
            "Atk" : 4,
            "Def" : 5,
            "Mag" : 6,
            "Spr" : 7,
            "Acc" : 8,
            "Spd" : 9,
            "Evs" : 10
        },
        "skills" : {"Cure", "Esuna"},
        "inventory" : ["Wand"]
    }
}

# tuple of races
    # tuple that contians all available races
race_options = ("Human", "Dragonborn", "Halfling", "Elf", "Ogre", "Dwarf", "Tiefling")

# tuple of classes
    # tuple containing all available classes
class_options = ("Black Mage", "Warrior", "Thief", "White Mage")

# return characters function,takes in character dictionary:
def char_return(character_dictionary):
    # returns character dictionary for easy access
    return character_dictionary

# Create character function, takes in character dictionary, race tuple, class tuple:
def create_character(character_dictionary, races, classes):
    # ask character name
    name = input("What is your characters name?")
    character_dictionary[name] = {}
    while True:
        # print class tuple
        for i in classes: print(f"{i}\n")
        # ask character class
        class_choice = input("What class is your character?")
        # if not valid class ask again
        if class_choice not in classes: continue
        else: break
    while True:
        # print race tuple
        for i in races: print(f"{i}\n")
        # ask character race
        race_choice = input("What race is your character?")
        # if not valid race ask again
        if race_choice not in races: continue
        else: break
    # ask character current level
    level = input("What level is your character?")
    # asks for character current inventory
    # creates new character with given name in the dictionary
    # adds given class under new character
    # adds given race under new character
    # sets new characters stats using Blaines set level function
    # sets new characters inventory with Wills new inventory function
    # returns updated character dictionary

# character editing function, takes in character dictionary:
    # User chooses character to edit with Warrens search function
    # ask what they want to edit (inventory, skills, attributes, name)
    # if they want to edit inventory run Wills edit inventory function
    # update inventory for that character in the character dictionary
    # if they want to edit skill run Blains update skills function
    # update skills for that character in the character dictionary
    # if they want to update attributes run Blaines update attribute function
    # update attributes for that character in the character dictionary
    # if they want to update name ask for the new name for the character
    # update name for that character in the character dictionary
    # ask if they want to keep editing, if they do then go back to the start of the function
    # if they don't return the updated dictionary

