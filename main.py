#Import other files for functions
from char_manager import character_creator
from character_search import insertsearchfunc
from inventoryWUI import character_editor


import sys
from char_manager import *
from character_search import *
from inventoryWUI import *
from skill_stat_manager import *
#Define main
def main():
    print("Welcome to the Rpg Character Manager. You can create, edit, and search for characters here.")
    while True:
        choice = input("What would you like to do?\n1.Create a new character\n2.Edit an already made character\n3.Search through characters\n4.Exit\n")
        if choice == '1':
            create_character(chracters,race_options,class_options)
        elif choice == '2':
            edit_character(chracters)
        elif choice == '3':
            char_search()
        if choice == '4':
            print("Goodbye")
            sys.exit()
        else:
            print("Invalid choice, try again")
#Run Main
main()