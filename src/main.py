# Enhanced RPG Character Manager - Main Menu integrating data visualization, statistical analysis, and random generation

import sys
import os

# Add src to path so modules can be imported directly
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from character import Character, CharacterRoster
from data_visualization import DataVisualization
from statistical_analyzer import StatisticalAnalyzer, OptimizationRecommender
from random_generator import RandomGenerator, ProceedralQuestGenerator
from data_manager import DataManager

# Initialize systems
roster = CharacterRoster()
visualizer = DataVisualization()
data_manager = DataManager()
random_gen = RandomGenerator()
quest_gen = ProceedralQuestGenerator()

# Constants
RACES = ("Human", "Dragonborn", "Halfling", "Elf", "Ogre", "Dwarf", "Tiefling")
CLASSES = ("Black Mage", "Warrior", "Thief", "White Mage")


def print_header(title):
    # Print a formatted header.
    print("\n" + "=" * 50)
    print(f"🎭 {title.upper()}")
    print("=" * 50)


def print_menu(options):
    # Print menu options.
    for key, value in options.items():
        print(f"[{key}] {value}")
    print()


def input_with_validation(prompt, validation_func=None, error_msg="Invalid input"):
    # Get validated user input.
    while True:
        user_input = input(prompt).strip()
        if validation_func is None or validation_func(user_input):
            return user_input
        print(error_msg)


def input_choice_from_list(items, prompt="Select an option"):
    # Let user choose from a list.
    for i, item in enumerate(items, 1):
        print(f"[{i}] {item}")
    
    choice = input_with_validation(
        f"\n{prompt} (1-{len(items)}): ",
        lambda x: x.isdigit() and 1 <= int(x) <= len(items),
        "Invalid choice"
    )
    return items[int(choice) - 1]


def select_character(prompt="Select a character"):
    # Select a character from roster.
    if not roster.characters:
        print("No characters in roster.")
        return None
    
    chars = list(roster.characters.keys())
    for i, name in enumerate(chars, 1):
        char = roster.get_character(name)
        print(f"[{i}] {name} ({char.race} {char.char_class} - Level {char.level})")
    
    choice = input_with_validation(
        f"\n{prompt} (1-{len(chars)}): ",
        lambda x: x.isdigit() and 1 <= int(x) <= len(chars),
        "Invalid choice"
    )
    return roster.get_character(chars[int(choice) - 1])


# ======================== CHARACTER MANAGEMENT ========================

def create_character_menu():
    # Create a new character.
    print_header("CREATE CHARACTER")
    
    # Get character name
    name = input_with_validation(
        "Character name: ",
        lambda x: x and x not in roster.characters,
        "Invalid or duplicate name"
    )
    
    # Select class
    print("\nSelect class:")
    char_class = input_choice_from_list(list(CLASSES))
    
    # Select race
    print("\nSelect race:")
    race = input_choice_from_list(list(RACES))
    
    # Select level
    level = input_with_validation(
        "Character level (1-99): ",
        lambda x: x.isdigit() and 1 <= int(x) <= 99,
        "Invalid level"
    )
    level = int(level)
    
    # Create character with default attributes
    character = Character(name, race, char_class, level)
    roster.add_character(character)
    
    print(f"\n✓ Character created: {character}")


def edit_character_menu():
    # Edit an existing character.
    print_header("EDIT CHARACTER")
    
    character = select_character()
    if not character:
        return
    
    while True:
        print(f"\nEditing: {character.name}")
        options = {
            "1": "Edit level",
            "2": "Edit attributes",
            "3": "View character",
            "4": "Back"
        }
        print_menu(options)
        
        choice = input("Choice: ").strip()
        
        if choice == "1":
            new_level = input_with_validation(
                "New level (1-99): ",
                lambda x: x.isdigit() and 1 <= int(x) <= 99,
                "Invalid level"
            )
            character.update_level(int(new_level))
            print(f"✓ Level updated to {new_level}")
        
        elif choice == "2":
            print("Current attributes:")
            for attr, value in character.attributes.items():
                print(f"  {attr}: {value}")
            
            attr_name = input("Attribute to edit: ").strip().upper()
            if attr_name in character.attributes:
                new_value = input_with_validation(
                    "New value: ",
                    lambda x: x.isdigit(),
                    "Invalid value"
                )
                character.attributes[attr_name] = int(new_value)
                print(f"✓ {attr_name} updated to {new_value}")
            else:
                print("Invalid attribute")
        
        elif choice == "3":
            print(f"\n{character}")
            print(f"  Race: {character.race}")
            print(f"  Class: {character.char_class}")
            print(f"  Total Stats: {character.get_total_stats()}")
            print(f"  Average Stat: {character.get_average_stats():.1f}")
            print(f"  Skills: {', '.join(character.skills) if character.skills else 'None'}")
        
        elif choice == "4":
            break


def delete_character_menu():
    # Delete a character.
    print_header("DELETE CHARACTER")
    
    character = select_character("Select character to delete")
    if not character:
        return
    
    confirm = input(f"Delete {character.name}? (y/n): ").strip().lower()
    if confirm == 'y':
        roster.remove_character(character.name)
        print(f"✓ {character.name} deleted")


def browse_characters_menu():
    # Browse all characters.
    print_header("BROWSE CHARACTERS")
    
    if not roster.characters:
        print("No characters in roster.")
        return
    
    for name, char in sorted(roster.characters.items()):
        level_pad = str(char.level).rjust(2)
        print(f"  • {name} ({char.race} {char.char_class}) - Level {level_pad}")


# ======================== DATA VISUALIZATION ========================

def visualization_menu():
    # Character visualization options.
    print_header("CHARACTER VISUALIZATION")
    
    if not roster.characters:
        print("No characters to visualize.")
        return
    
    while True:
        options = {
            "1": "Individual Radar Chart",
            "2": "Individual Bar Chart",
            "3": "Multi-Character Comparison",
            "4": "Attribute Distribution",
            "5": "Back"
        }
        print_menu(options)
        
        choice = input("Choice: ").strip()
        
        if choice == "1":
            character = select_character("Select character for radar chart")
            if character:
                visualizer.create_radar_chart(character)
        
        elif choice == "2":
            character = select_character("Select character for bar chart")
            if character:
                visualizer.create_bar_chart(character)
        
        elif choice == "3":
            print("Select characters to compare (select at least 2):")
            selected = []
            for _ in range(min(3, len(roster.characters))):
                if input(f"Add another character? (y/n): ").strip().lower() == 'y':
                    char = select_character()
                    if char:
                        selected.append(char)
            if len(selected) >= 2:
                visualizer.create_comparison_chart(selected)
        
        elif choice == "4":
            visualizer.create_attribute_distribution(roster)
        
        elif choice == "5":
            break


# ======================== STATISTICAL ANALYSIS ========================

def statistical_analysis_menu():
    # Statistical analysis options.
    print_header("STATISTICAL ANALYSIS")
    
    if not roster.characters:
        print("No characters to analyze.")
        return
    
    analyzer = StatisticalAnalyzer(roster)
    
    while True:
        options = {
            "1": "View Statistical Report",
            "2": "Compare Two Characters",
            "3": "Export Analysis Report",
            "4": "Back"
        }
        print_menu(options)
        
        choice = input("Choice: ").strip()
        
        if choice == "1":
            print(analyzer.generate_statistical_report())
        
        elif choice == "2":
            if len(roster.characters) < 2:
                print("Need at least 2 characters to compare.")
                continue
            
            print("Select first character:")
            char1 = select_character()
            if not char1:
                continue
            
            print("\nSelect second character:")
            char2 = select_character()
            if char2:
                print(analyzer.get_character_comparison(char1.name, char2.name))
        
        elif choice == "3":
            filename = data_manager.export_analysis_report(roster, analyzer)
            if filename:
                print(f"✓ Report saved to: {filename}")
        
        elif choice == "4":
            break


def optimization_menu():
    # Character optimization recommendations.
    print_header("CHARACTER OPTIMIZATION")
    
    character = select_character()
    if character:
        recommender = OptimizationRecommender(character)
        print(recommender.get_recommendations())


# ======================== RANDOM GENERATION ========================

def random_generator_menu():
    # Random character generation options.
    print_header("RANDOM GENERATOR")
    
    while True:
        options = {
            "1": "Generate Random Character",
            "2": "Generate Class Template",
            "3": "Generate Random Quest",
            "4": "Back"
        }
        print_menu(options)
        
        choice = input("Choice: ").strip()
        
        if choice == "1":
            character = random_gen.generate_full_character()
            
            print(f"\n✓ Generated: {character}")
            print(f"  Backstory: {character.backstory}")
            print(f"  Personality: {character.personality}")
            print(f"  Equipment: {character.equipment}")
            print(f"  Quest: {character.current_quest}")
            
            add = input("\nAdd to roster? (y/n): ").strip().lower()
            if add == 'y':
                if character.name not in roster.characters:
                    roster.add_character(character)
                    print("✓ Added to roster")
                else:
                    new_name = input("Name already exists. New name: ").strip()
                    character.name = new_name
                    roster.add_character(character)
                    print("✓ Added with new name")
        
        elif choice == "2":
            print("\nSelect class for template:")
            char_class = input_choice_from_list(list(CLASSES))
            
            character = random_gen.generate_character_template(char_class)
            
            print(f"\n✓ Generated {char_class} template: {character}")
            print(f"  Stats: {character.attributes}")
            
            add = input("\nAdd to roster? (y/n): ").strip().lower()
            if add == 'y':
                if character.name not in roster.characters:
                    roster.add_character(character)
                    print("✓ Added to roster")
                else:
                    new_name = input("Name already exists. New name: ").strip()
                    character.name = new_name
                    roster.add_character(character)
                    print("✓ Added with new name")
        
        elif choice == "3":
            print(quest_gen.generate_quest())
        
        elif choice == "4":
            break


# ======================== DATA MANAGEMENT ========================

def data_management_menu():
    # Data save/load/export management.
    print_header("DATA MANAGEMENT")
    
    while True:
        options = {
            "1": "Export to CSV",
            "2": "Import from CSV",
            "3": "Export to JSON",
            "4": "Import from JSON",
            "5": "Create Backup",
            "6": "Restore from Backup",
            "7": "Export Detailed Report",
            "8": "Back"
        }
        print_menu(options)
        
        choice = input("Choice: ").strip()
        
        if choice == "1":
            filename = data_manager.export_to_csv(roster)
            if filename:
                print(f"✓ Exported to: {filename}")
        
        elif choice == "2":
            filename = input("Enter CSV filename (or press Enter for default): ").strip()
            loaded_roster = data_manager.import_from_csv(filename if filename else None)
            if loaded_roster.characters:
                for char in loaded_roster:
                    roster.add_character(char)
                print(f"✓ Imported {len(loaded_roster)} characters")
        
        elif choice == "3":
            filename = data_manager.export_to_json(roster)
            if filename:
                print(f"✓ Exported to: {filename}")
        
        elif choice == "4":
            filename = input("Enter JSON filename: ").strip()
            loaded_roster = data_manager.import_from_json(filename)
            if loaded_roster.characters:
                for char in loaded_roster:
                    roster.add_character(char)
                print(f"✓ Imported {len(loaded_roster)} characters")
        
        elif choice == "5":
            backup = data_manager.create_backup(roster)
            if backup:
                print(f"✓ Backup created: {backup}")
        
        elif choice == "6":
            backups = data_manager.list_backups()
            if not backups:
                print("No backups available.")
                continue
            
            print("Available backups:")
            for i, backup in enumerate(backups, 1):
                print(f"[{i}] {backup}")
            
            choice_idx = input_with_validation(
                f"Select backup (1-{len(backups)}): ",
                lambda x: x.isdigit() and 1 <= int(x) <= len(backups),
                "Invalid choice"
            )
            
            loaded_roster = data_manager.restore_from_backup(backups[int(choice_idx) - 1])
            for char in loaded_roster:
                roster.add_character(char)
            print("✓ Restored from backup")
        
        elif choice == "7":
            filename = data_manager.export_to_detailed_csv(roster)
            if filename:
                print(f"✓ Detailed report saved")
        
        elif choice == "8":
            break


# ======================== MAIN MENU ========================

def main():
    # Main menu loop.
    print("\n" + "🎭" * 25)
    print("WELCOME TO THE ENHANCED RPG CHARACTER MANAGER")
    print("🎭" * 25)
    
    while True:
        print(f"\n[{len(roster)} characters in roster]")
        
        options = {
            "1": "Character Visualization",
            "2": "Statistical Analysis",
            "3": "Character Optimization",
            "4": "Create Character",
            "5": "Edit Character",
            "6": "Delete Character",
            "7": "Browse Characters",
            "8": "Random Generator",
            "9": "Data Management",
            "Q": "Quit"
        }
        print_menu(options)
        
        choice = input("Enter choice: ").strip().upper()
        
        if choice == "1":
            visualization_menu()
        elif choice == "2":
            statistical_analysis_menu()
        elif choice == "3":
            optimization_menu()
        elif choice == "4":
            create_character_menu()
        elif choice == "5":
            edit_character_menu()
        elif choice == "6":
            delete_character_menu()
        elif choice == "7":
            browse_characters_menu()
        elif choice == "8":
            random_generator_menu()
        elif choice == "9":
            data_management_menu()
        elif choice == "Q":
            confirm = input("Exit? (y/n): ").strip().lower()
            if confirm == 'y':
                print("\nThank you for using the Enhanced RPG Character Manager!")
                sys.exit()
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
