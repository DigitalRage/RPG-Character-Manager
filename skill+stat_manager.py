#Put inside file function
    #use set level function
def setup_char_value(): 
    #While editing
    while True:
        #Characters starting stats are in nested dictionary
        char_table_lv1 = {
                'Black Mage': { 'Stats': {'MP': 15, 'HP': 50, 'Str': 0, 'Atk': 0, 'Def': 5, 'Mag': 10, 'Spr': 9, 'Acc': 0, 'Spd': 25, 'Evs': 30, 'Lvl': 1}, 'Atributes': {'Fire': 1, 'Fira': 15, 'Firaga': 30, 'Blizzard': 1, 'Blizzara': 17, 'Blizzaraga': 35, 'Thunder': 1, 'Thundara': 18, 'Thundaraga': 35, 'Poison': 5, 'Blind': 6, 'Silence': 7}}, 

        }
        #Player choses single or all stat editor, then opens adding or removing level function, or editing a single stat function
        choice = input('Do you want to: \n1. Edit single stat\n2. Edit level\n3. Edit attributes')
        #Multiply by level function:
        def mult_level(): 
            new_level = input("What is the character Level?\n>")
            char_table = char_table_lv1*[new_level]
        #Based on level stat, other stats are multiplied by 0.1x for actual stat

        #Single stat Function: 
        #Asks player which stat
        #Asks user the value to change by
        #Change single stat
        #Saves to added stats bar in dictionary


        #Choice to add character skills based on class and level
        #If the skill is available (not already used and claimed) and a slot is left, then add the new skill to their inventory; 
        #Else, go back to show skills

        #Choice to remove character skills
        #If no skill to remove, go back to edit
        #else, if the name of skill equals the input of user, remove the skill. 

        #Player is asked if they are still editing
        #if editing equals false, then break
        return char_table