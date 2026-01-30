#WG_CP2 character search for group
#The code for searching though the characters
#from character creator import character return
from char_manager import char_return

#from main import main
from main import main
#define check character
def check_char():
    characters = char_return()
    while True:
        search_val = input("What do you want to search for? This can be a name, a race, a class, or having a certain number in any attribute. ").strip().lower()

        matched_char = []
        for name, data in characters.items():
            # check name match
            if search_val in name.lower():
                matched_char.append(name)
                continue

            # helper to search nested structures
            def search_in(obj):
                if isinstance(obj, dict):
                    return any(search_in(v) for v in obj.values())
                if isinstance(obj, (list, set, tuple)):
                    return any(search_in(v) for v in obj)
                if isinstance(obj, (int, float)):
                    return search_val == str(obj).lower()
                if isinstance(obj, str):
                    return search_val in obj.lower()
                return False

            if search_in(data):
                matched_char.append(name)

        if not matched_char:
            print(f"No characters found matching '{search_val}'. Try again.")
            continue

        print("Matches:")
        for i, name in enumerate(matched_char, 1):
            print(f"{i}. {name}")

        choice = input("Which character do you want to look at? (type name or number) ").strip()
        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(matched_char):
                return matched_char[idx]
        else:
            if choice in matched_char:
                return choice

        print(f"{choice} is not an option; try again.")

#character search function
def char_search():
    #call check_char with characters argunment, & search value
    check = check_char()
    char_display(check)
    #ask if they want to exit
    exit = input("Do you want to exit the searching? do not answer until you are done looking over the character. y/n ").strip().lower()
    #if exit is no

    if exit == "n":
        #continue
        check_char()

    #else   
    else:
        #break
        main()
#character display function
def char_display(char_key):

    characters = char_return()

    race = characters[char_key]["race"]
    print(f"race: {race}")

    race = characters[char_key]["race"]
    print(f"race: {race}\n")
    classs = characters[char_key]["class"]
    print(f"class: {classs}\n")
    level = characters[char_key]["level"]
    print(f"level: {level}\n")
    mp = characters[char_key]["atributtes"]["MP"]
    print(f"MP: {mp}\n")
    hp = characters[char_key]["atributtes"]["HP"]
    print(f"HP: {hp}\n")
    str = characters[char_key]["atributtes"]["Str"]
    print(f"Str: {str}\n")
    atk = characters[char_key]["atributtes"]["Atk"]
    print(f"Atk: {atk}\n")
    deff = characters[char_key]["atributtes"]["Def"]
    print(f"Def: {deff}")
    mag = characters[char_key]["atributtes"]["Mag"]
    print(f"Mag: {mag}\n")
    spr = characters[char_key]["atributtes"]["Spr"]
    print(f"Spr: {spr}\n")
    acc = characters[char_key]["atributtes"]["Acc"]
    print(f"Acc: {acc} \n")
    spd = characters[char_key]["atributtes"]["Spd"]
    print(f"Spd: {spd}\n")
    evs = characters[char_key]["atributtes"]["Evs"]
    print(f"Evs: {evs}\n")
    skills = characters[char_key]["skills"]
    print(f"Skills: {skills}\n")
    inventory = characters[char_key]["inventory"]
    print(f"Inventory: {inventory}\n")
def key_from_value(characters, key_desired):
    for key, value in characters.items():
        if value == key_desired:
            return key

if __name__ == "__main__":
    char_search()