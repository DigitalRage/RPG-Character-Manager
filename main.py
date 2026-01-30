#Import other files for functions
from char_manager import create_character, edit_character
from character_search import char_search


import sys
#Define main
def main():
    print("Welcome to the Rpg Character Manager. You can create, edit, and search for characters here.")
    while True:
        choice = input("What would you like to do?\n1.Create a new character\n2.Edit an already made character\n3.Search through characters\n4.Exit\n")
        if choice == '1':
            create_character()
        elif choice == '2':
            edit_character()
        elif choice == '3':  
            char_search()
        if choice == '4':
            print("Goodbye")
            sys.exit()
        else:
            print("Invalid choice, try again")
#Run Main
main()