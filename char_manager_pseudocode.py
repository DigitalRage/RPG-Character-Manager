# MH 1st character management

import mult_level
import new_inven
import char_search
import edit_inven
import char_display
import setup_char_value
import edit_inven

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
        "inventory" : {
            "weapon" : ["Wand"],
            "armor" : ["Robes"],
            "equipment one" : ["Classic Italian Pizza"],
            "equipment two" : ["Pot of Petunias"],
            "equipment three" : ["Bowling Pin"],
            "equipment four" : ["Sticky Hand"]
        }
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
    while True:
        # ask character current level
        level = input("What level is your character?")
        if level.isdigit == False: continue
        else : 
            int(level) 
            break
    # creates new character with given name in the dictionary
    character_dictionary[name] = {}
    # adds given class under new character
    character_dictionary[name["class"]] = class_choice 
    # adds given race under new character
    character_dictionary[name["race"]] = race_choice
    character_dictionary[name["level"]] = level
    # sets new characters stats using Blaines set level function
    character_dictionary = mult_level(character_dictionary)
    # sets new characters inventory with Wills new inventory function
    character_dictionary = new_inven(class_choice, character_dictionary, name)
    # returns updated character dictionary
    return character_dictionary

# character editing function, takes in character dictionary:
def edit_character(character_ditionary):
    while True:
        # User chooses character to edit with Warrens search function
        character = char_search()
        char_display(character)
        # ask what they want to edit (inventory, skills, attributes, name)
        to_edit = input("What do you want to edit?\n1. Inventory\n2. Skills\n3. Atributtes")
        if to_edit == "1": 
            # if they want to edit inventory run Wills edit inventory function
            # update inventory for that character in the character dictionary
            character_dictionary = edit_inven()
        if to_edit == "2":
            # temporary pass
            character_dictionary = setup_char_value()
        # if they want to edit skill run Blains update skills function
        # update skills for that character in the character dictionary
        if to_edit == "3":
            # temporary pass
            character_dictionary = edit_inven(character_dictionary,character_dictionary[character], character_dictionary[character["class"]])
        # if they want to update attributes run Blaines update attribute function
        # update attributes for that character in the character dictionary
        while True:
        # ask if they want to keep editing, if they do then go back to the start of the function
            keep_editing = input("Do you want to keep editing? (Y/N)").lower().strip()
            if keep_editing == "y" or "n": break
            else: continue
        if keep_editing == "y": continue
        else: break
    # if they don't return the updated dictionary
    return character_dictionary

