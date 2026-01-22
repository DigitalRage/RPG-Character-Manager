# MH 1st character management

# dictionary to contain all characters
# FOR ALL CHARACTERS
    # race and class stored in tuple
    # inventory stored in list
    # set for skills
    # nested dictionary for attributtes

# tuple of races
    # tuple that contians all available races
# tuple of class
    # tuple containing all available classes

# return characters function,takes in character dictionary:
    # returns character dictionary for easy access

# Create character function, takes in character dictionary, race tuple, class tuple:
    # ask character name
    # print class tuple
    # ask character class
    # if not valid class ask again
    # print race tuple
    # ask character race
    # if not valid race ask again
    # ask character current level
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

