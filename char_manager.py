# MH 1st character management

from skill_stat_manager import setup_char_value, get_stats_for_class
from inventoryWUI import new_inven, edit_inven
from character_search import char_search, char_display

# dictionary to contain all characters
characters = {
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
def char_return():
    # returns character dictionary for easy access
    return characters

# Create character function, takes in character dictionary, race tuple, class tuple:
def create_character(character_dictionary, races, classes):
    # ask character name
    name = input("What is your characters name?\n")
    # choose class
    while True:
        for idx, cls in enumerate(classes, start=1):
            print(f"{idx}. {cls}")
        class_choice = input("Choose a class (enter number)\n")
        if class_choice.isdigit() and 1 <= int(class_choice) <= len(classes):
            class_choice = classes[int(class_choice) - 1]
            break
        print("That is not an option.")

    # choose race
    while True:
        print("\n")
        for idx, rc in enumerate(races, start=1):
            print(f"{idx}. {rc}")
        race_choice = input("Choose a race (enter number)\n")
        if race_choice.isdigit() and 1 <= int(race_choice) <= len(races):
            race_choice = races[int(race_choice) - 1]
            break
        print("That is not an option.")

    # choose level
    while True:
        level = input("What level is your character?\n")
        if not level.isdigit():
            print("That is not an option.")
            continue
        level = int(level)
        break

    # create character entry
    character_dictionary[name] = {}
    character_dictionary[name]["class"] = class_choice
    character_dictionary[name]["race"] = race_choice
    character_dictionary[name]["level"] = level

    # set base atributtes using skill_stat_manager helper
    character_dictionary[name]["atributtes"] = get_stats_for_class(class_choice, level)
    # start with empty skills set
    character_dictionary[name]["skills"] = set()

    # set new character inventory with Wills new inventory function
    character_dictionary = new_inven(class_choice, character_dictionary, name)
    # returns updated character dictionary
    return character_dictionary

# character editing function, takes in character dictionary:
def edit_character(character_dictionary):
    while True:
        # User chooses character to edit with Warrens search function
        character = char_search()
        char_display(character)
        # ask what they want to edit (inventory, skills, attributes, name)
        to_edit = input("What do you want to edit?\n1. Inventory\n2. Skills\n3. Atributtes\n")
        if to_edit == "1":
            # edit inventory for that character
            character_dictionary = edit_inven(character_dictionary, character, character_dictionary[character]["class"])
        elif to_edit == "2":
            # simple skills add/remove handler
            action = input("Add or remove skill? (add/remove)\n").strip().lower()
            if action == 'add':
                new_skill = input("Skill name?\n")
                character_dictionary[character].setdefault('skills', set()).add(new_skill)
            elif action == 'remove':
                rem = input("Skill name to remove?\n")
                character_dictionary[character].setdefault('skills', set()).discard(rem)
        elif to_edit == "3":
            # edit attributes for that character
            character_dictionary = setup_char_value(target_name=character)
        else:
            print("Not an option.")

        # ask if they want to keep editing
        while True:
            keep_editing = input("Do you want to keep editing? (Y/N)\n").lower().strip()
            if keep_editing in ("y", "n"):
                break
            else:
                continue
        if keep_editing == "y":
            continue
        else:
            break
    # return the updated dictionary
    return character_dictionary
