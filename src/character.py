# Enhanced Character Class for RPG Manager integrating Pandas DataFrame support for data analysis

import pandas as pd
from datetime import datetime

class Character:
    # Enhanced Character class supporting Pandas DataFrame operations
    # and statistical analysis for RPG character management.
    
    def __init__(self, name, race, char_class, level=1, attributes=None, skills=None, inventory=None):
        # Initialize a character with enhanced features.
        self.name = name
        self.race = race
        self.char_class = char_class
        self.level = level
        self.created_date = datetime.now()
        
        # Default attributes if none provided
        if attributes is None:
            attributes = {
                'MP': 10, 'HP': 50, 'Str': 5, 'Atk': 5, 'Def': 5,
                'Mag': 5, 'Spr': 5, 'Acc': 40, 'Spd': 15, 'Evs': 15
            }
        
        self.attributes = attributes
        self.skills = skills if skills is not None else set()
        self.inventory = inventory if inventory is not None else {}
        self.progression_history = []  # For tracking level ups and changes
        
    def to_dict(self):
        # Convert character to dictionary format.
        return {
            'name': self.name,
            'race': self.race,
            'class': self.char_class,
            'level': self.level,
            'created_date': self.created_date.strftime('%Y-%m-%d %H:%M:%S'),
            **self.attributes,
            'skills_count': len(self.skills)
        }
    
    def to_dataframe_row(self):
        # Convert character to a DataFrame row.
        row = {
            'Name': self.name,
            'Race': self.race,
            'Class': self.char_class,
            'Level': self.level,
        }
        row.update(self.attributes)
        return row
    
    def update_level(self, new_level):
        # Update character level and record progression.
        old_level = self.level
        self.level = new_level
        self.progression_history.append({
            'timestamp': datetime.now(),
            'from_level': old_level,
            'to_level': new_level
        })
    
    def get_total_stats(self):
        # Calculate total combined stats.
        return sum(self.attributes.values())
    
    def get_average_stats(self):
        # Calculate average stat value.
        if not self.attributes:
            return 0
        return sum(self.attributes.values()) / len(self.attributes)
    
    def get_stat_distribution(self):
        # Get distribution of stats for visualization.
        return self.attributes.copy()
    
    def add_skill(self, skill):
        # Add a skill to character.
        self.skills.add(skill)
    
    def remove_skill(self, skill):
        # Remove a skill from character.
        self.skills.discard(skill)
    
    def __repr__(self):
        return f"Character({self.name}, {self.race} {self.char_class}, Level {self.level})"
    
    def __str__(self):
        return f"{self.name} - {self.race} {self.char_class} (Level {self.level})"


class CharacterRoster:
    # Manages a roster of characters using Pandas DataFrames
    # for efficient data analysis and manipulation.
    
    def __init__(self):
        # Initialize character roster.
        self.characters = {}  # name -> Character object
        self.df = pd.DataFrame()  # Pandas DataFrame for analysis
        
    def add_character(self, character):
        # Add a character to the roster.
        self.characters[character.name] = character
        self._update_dataframe()
        
    def remove_character(self, name):
        # Remove a character from the roster.
        if name in self.characters:
            del self.characters[name]
            self._update_dataframe()
            return True
        return False
    
    def get_character(self, name):
        # Retrieve a character by name.
        return self.characters.get(name)
    
    def _update_dataframe(self):
        # Update the internal DataFrame with current characters.
        if self.characters:
            rows = [char.to_dataframe_row() for char in self.characters.values()]
            self.df = pd.DataFrame(rows)
        else:
            self.df = pd.DataFrame()
    
    def get_dataframe(self):
        # Get the character data as a DataFrame.
        self._update_dataframe()
        return self.df
    
    def get_characters_by_class(self, char_class):
        # Filter characters by class.
        return [char for char in self.characters.values() if char.char_class == char_class]
    
    def get_characters_by_race(self, race):
        # Filter characters by race.
        return [char for char in self.characters.values() if char.race == race]
    
    def get_characters_by_level_range(self, min_level, max_level):
        # Filter characters by level range.
        return [char for char in self.characters.values() 
                if min_level <= char.level <= max_level]
    
    def get_roster_as_list(self):
        # Return list of all characters.
        return list(self.characters.values())
    
    def __len__(self):
        # Return number of characters in roster.
        return len(self.characters)
    
    def __iter__(self):
        # Iterate over characters.
        return iter(self.characters.values())
