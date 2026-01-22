# WM 1st pseudocode

#UI
    #Create a function for the main interface, just named main()
    #Have it greet them to the program.
    #Start a while true loop that will keep the code going until the user chooses to exit.
    #They will be asked what they want to do, 1.Make a character 2.Edit a character 3.Search for a character 4.Exit
    #Each option will call a different funtion



#Inventory
    #Make a dictionary for the items in the game, split into several pieces.
    #It would start with a split between weapons, equipment, and armor.
        #The weapons would then seperate based on class restrictions
            #Then each weapon would have its own stats
        #The equipment would be split into ones with one stat increased, two stats, and three stats.
            #There will be one for each of the one stat, but the two and three stats would only be with ones that make sense.
        #Armor would also be class restricted, based on what was choosen in creator.
            #There would be a few options for each class, with them affecting defense, evasion, speed, and spirit differently
    #Make a function for creating a character inventory.
def new_inven():
    pass
        #It will search for keywords like warrior or mage in their class and mark variables as true where needed.
        #It will print all the valid items for them
        #It would start with weapons and the armor, and then finally do equipment. a variable would keep track of how many equipment they choose, so it will end when they get all 4.
        #All of these would loop until a variable for each becomes true, and lets it move on.
        #It would finally return the character dictionary at the end.
        #When they choose an item, it will use that to search for the item, and if it exists, it will append it to the character dictionaray.
    #Make a fucntion for editing an already made character
def edit_inven():
    pass
        #It will ask if they want to remove an item, or add an item.
            #If they choose either, it will check to see if they have either an item to remove, or an open slot to add to.
            #If they do, they would both ask what item, either to remove, which it would print their items they have, or what they want to add, printing the right items, taking restrictions into account.
            #When they choose a valid item, it would fill a dictionary with a empty place holder if they removed, and if they added it would insert the item into the correct slot.
            #It would return back to the main chunk function of character editer, by Mirai.
    #Function names
    #new_inven()
    #edit_inven()