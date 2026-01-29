#WG_CP2 character search for group
#The code for searching though the characters
#from character creator import character return
from char_manager import char_return

#from main import main
from main import main
#define check character
def check_char():
    #characters is character_return
    characters = char_return()
    #Ask what they want to search for save as search value
    search_val = input("What do you want to search for in the character?").strip().lower()

    #list of checked characters, and matched characters
    matched_char = []
    #while searching

    while True:
        #set value of variable to 0 saved as value_key
        value_key = 0
        #get all of the keys and add them to a list

        for i in len(characters):
            keys = list(characters.keys())
        #if loop equal first

        if value_key == 0:
            #for the length of characters

            for i in len(characters):
                #if search value in characters(key value placed in the list at the position equal to the value

                if search_val in characters[keys[value_key]]:
                    #add the character key to list of matched keys
                    matched_char.append(keys(value_key))
                #add 1 to value_key
                value_key += 1

        #if there is characters
        if len(matched_char) > 0:

            #for length of the matched value    
            for i in len(matched_char):
                #display the value from the list of keys starting at the first value and say that they have the specefied value
                print(f"{matched_char(i-1)} has value {search_val}")
        #ask what character they want to look at
        veiw_char = input("What character did you want to look at? ").strip().lower()
        #while true

        while True:
            #if character is in matched keys

            if veiw_char in matched_char:
                #display characters(wanted character)
                return veiw_char
            #else

            else:
                #display not an option
                print(f"{veiw_char} is not on options")
                continue

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
    print(f"race: {race}")
    classs = characters[char_key]["class"]
    print(f"class: {classs}")
    level = characters[char_key]["level"]
    print(f"level: {level}")
    mp = characters[char_key]["attributtes"]["MP"]
    print(f"MP: {mp}")
    hp = characters[char_key]["attributtes"]["HP"]
    print(f"HP: {hp}")
    str = characters[char_key]["attributtes"]["Str"]
    print(f"Str: {str}")
    atk = characters[char_key]["attributtes"]["Atk"]
    print(f"Atk: {atk}")
    deff = characters[char_key]["attributtes"]["Def"]
    print(f"Def: {deff}")
    mag = characters[char_key]["attributtes"]["Mag"]
    print(f"Mag: {mag}")
    spr = characters[char_key]["attributtes"]["Spr"]
    print(f"Def: {spr}")
    acc = characters[char_key]["attributtes"]["Acc"]
    print(f"Acc: {acc}")
    spd = characters[char_key]["attributtes"]["Spd"]
    print(f"Spd: {spd}")
    evs = characters[char_key]["attributtes"]["Evs"]
    print(f"Evs: {evs}")
    skills = characters[char_key]["skills"]
    print(f"Skills: {skills}")
    inventory = characters[char_key]["inventory"]
    print(f"Inventory: {inventory}")
def key_from_value(characters, key_desired):
    for key, value in characters.items():
        if value == key_desired:
            return key

char_search()