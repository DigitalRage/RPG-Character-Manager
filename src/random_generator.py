# Random Generation Module for RPG Character Manager - uses Faker and random to generate realistic character data

from faker import Faker
import random
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from character import Character

class RandomGenerator:
    # Generates random character data using Faker library.
    # Creates realistic names, backstories, descriptions, and character templates.
    
    def __init__(self, seed=None):
        # Initialize Random Generator with optional seed for reproducibility.
        self.fake = Faker()
        if seed is not None:
            Faker.seed(seed)
            random.seed(seed)
        
        self.races = ["Human", "Dragonborn", "Halfling", "Elf", "Ogre", "Dwarf", "Tiefling"]
        self.classes = ["Black Mage", "Warrior", "Thief", "White Mage"]
        self.skills = [
            "Fireball", "Ice Storm", "Lightning Bolt", "Heal", "Cure",
            "Slash", "Power Attack", "Defend", "Taunt", "Steal",
            "Backstab", "Shadow Dance", "Evade", "Counter", "Berserk"
        ]
        self.personality_traits = [
            "courageous", "cautious", "ambitious", "humble", "loyal",
            "cunning", "honest", "secretive", "cheerful", "serious",
            "wise", "foolish", "strong-willed", "flexible", "stubborn"
        ]
        self.locations = [
            "Ancient Forest", "Crystal Caverns", "Volcanic Mountains", "Frozen Tundra",
            "Desert Wastes", "Enchanted Valley", "Dark Swamps", "Sky Citadel",
            "Sunken Temple", "Dark Castle", "Whispering Grove", "Storm Peak"
        ]
    
    def generate_random_name(self):
        # Generate a random character name using Faker.
        return self.fake.first_name()
    
    def generate_race(self):
        # Generate a random race.
        return random.choice(self.races)
    
    def generate_class(self):
        # Generate a random class.
        return random.choice(self.classes)
    
    def generate_level(self, min_level=1, max_level=20):
        # Generate a random character level.
        return random.randint(min_level, max_level)
    
    def generate_random_stats(self):
        # Generate random stat distribution (base values).
        base_value = random.randint(20, 50)
        variance = random.randint(10, 25)
        
        stats = {}
        for stat in ['MP', 'HP', 'Str', 'Atk', 'Def', 'Mag', 'Spr', 'Acc', 'Spd', 'Evs']:
            value = base_value + random.randint(-variance, variance)
            stats[stat] = max(1, value)  # Ensure all stats are at least 1
        
        return stats
    
    def generate_random_skills(self, num_skills=3):
        # Generate random skills for a character.
        num_skills = min(num_skills, len(self.skills))
        return set(random.sample(self.skills, num_skills))
    
    def generate_backstory(self):
        # Generate a random character backstory.
        origin = random.choice(self.locations)
        trait = random.choice(self.personality_traits)
        profession = random.choice(["adventurer", "scholar", "warrior", "mage", "merchant", "knight"])
        
        backstories = [
            f"A {trait} {profession} from {origin}, born with a mysterious gift.",
            f"Exiled from {origin}, seeks redemption through adventure.",
            f"A mysterious traveler with {trait} nature, possessing forbidden knowledge.",
            f"Once a guardian of {origin}, now wandering to protect the innocent.",
            f"A {trait} soul searching for purpose in a dangerous world.",
            f"Escaped from {origin}, determined to master their powers.",
        ]
        
        backstory = random.choice(backstories)
        return backstory
    
    def generate_personality_description(self):
        # Generate a personality description for a character.
        trait1 = random.choice(self.personality_traits)
        trait2 = random.choice(self.personality_traits)
        
        descriptions = [
            f"A {trait1} individual with {trait2} tendencies.",
            f"{trait1.capitalize()} yet {trait2}.",
            f"Appears {trait1}, but harbors {trait2} thoughts.",
            f"Combines {trait1} wisdom with {trait2} instincts.",
            f"A {trait1} heart with {trait2} determination.",
        ]
        
        return random.choice(descriptions)
    
    def generate_quest(self):
        # Generate a random quest for a character.
        verbs = ["retrieve", "defeat", "rescue", "discover", "protect", "investigate"]
        objects = ["lost artifact", "ancient treasure", "mysterious person", "forbidden knowledge",
                  "hidden artifact", "cursed item", "legendary weapon"]
        locations = self.locations
        
        verb = random.choice(verbs)
        obj = random.choice(objects)
        location = random.choice(locations)
        
        return f"{verb.capitalize()} {obj} from {location}."
    
    def generate_equipment_description(self):
        # Generate a random equipment description.
        weapon_types = ["sword", "staff", "bow", "axe", "wand", "spear", "dagger"]
        armor_types = ["armor", "robes", "leather outfit", "chainmail", "cloak"]
        modifiers = ["enchanted", "ancient", "cursed", "blessed", "mysterious", "legendary"]
        
        weapon = random.choice(weapon_types)
        armor = random.choice(armor_types)
        mod1 = random.choice(modifiers)
        mod2 = random.choice(modifiers)
        
        equipment = f"An {mod1} {weapon} and {mod2} {armor}"
        return equipment
    
    def generate_full_character(self, name=None, race=None, char_class=None, level=None):
        # Generate a complete random character with all attributes.
        #
        # Args:
        #     name: Optional character name (generates if None)
        #     race: Optional race (generates if None)
        #     char_class: Optional class (generates if None)
        #     level: Optional level (generates if None)
        #
        # Returns:
        #     Character object with random data
        if name is None:
            name = self.generate_random_name()
        if race is None:
            race = self.generate_race()
        if char_class is None:
            char_class = self.generate_class()
        if level is None:
            level = self.generate_level()
        
        attributes = self.generate_random_stats()
        skills = self.generate_random_skills()
        
        character = Character(
            name=name,
            race=race,
            char_class=char_class,
            level=level,
            attributes=attributes,
            skills=skills
        )
        
        # Add generation data as notes
        character.backstory = self.generate_backstory()
        character.personality = self.generate_personality_description()
        character.equipment = self.generate_equipment_description()
        character.current_quest = self.generate_quest()
        
        return character
    
    def generate_character_template(self, char_class=None):
        # Generate a character template optimized for a specific class.
        #
        # Args:
        #     char_class: Class to optimize for (random if None)
        #
        # Returns:
        #     Character object with class-optimized stats
        if char_class is None:
            char_class = self.generate_class()
        
        name = self.generate_random_name()
        race = self.generate_race()
        level = self.generate_level(1, 10)
        
        # Class-specific stat distributions
        class_stats = {
            'Black Mage': {
                'MP': random.randint(30, 50), 'HP': random.randint(20, 40),
                'Str': random.randint(5, 15), 'Atk': random.randint(5, 15),
                'Def': random.randint(10, 20), 'Mag': random.randint(35, 50),
                'Spr': random.randint(20, 30), 'Acc': random.randint(30, 50),
                'Spd': random.randint(35, 50), 'Evs': random.randint(35, 50)
            },
            'Warrior': {
                'MP': random.randint(5, 15), 'HP': random.randint(60, 80),
                'Str': random.randint(35, 50), 'Atk': random.randint(30, 45),
                'Def': random.randint(35, 50), 'Mag': random.randint(5, 15),
                'Spr': random.randint(10, 20), 'Acc': random.randint(50, 70),
                'Spd': random.randint(20, 35), 'Evs': random.randint(15, 25)
            },
            'Thief': {
                'MP': random.randint(10, 20), 'HP': random.randint(40, 60),
                'Str': random.randint(15, 30), 'Atk': random.randint(30, 45),
                'Def': random.randint(20, 35), 'Mag': random.randint(5, 15),
                'Spr': random.randint(15, 25), 'Acc': random.randint(55, 75),
                'Spd': random.randint(40, 60), 'Evs': random.randint(40, 60)
            },
            'White Mage': {
                'MP': random.randint(30, 50), 'HP': random.randint(30, 50),
                'Str': random.randint(10, 20), 'Atk': random.randint(10, 20),
                'Def': random.randint(15, 25), 'Mag': random.randint(25, 40),
                'Spr': random.randint(30, 45), 'Acc': random.randint(40, 60),
                'Spd': random.randint(30, 45), 'Evs': random.randint(35, 50)
            }
        }
        
        attributes = class_stats.get(char_class, self.generate_random_stats())
        
        # Scale stats based on level
        for stat_key in attributes:
            attributes[stat_key] = int(attributes[stat_key] * (level / 5))
        
        skills = self.generate_random_skills(4)
        
        character = Character(
            name=name,
            race=race,
            char_class=char_class,
            level=level,
            attributes=attributes,
            skills=skills
        )
        
        character.backstory = self.generate_backstory()
        character.personality = self.generate_personality_description()
        character.equipment = self.generate_equipment_description()
        character.current_quest = self.generate_quest()
        
        return character


class ProceedralQuestGenerator:
    # Generates random quests and missions for characters.
    
    def __init__(self):
        # Initialize quest generator with quest data.
        self.objectives = [
            "retrieve", "defeat", "escort", "rescue", "investigate",
            "protect", "destroy", "steal", "repair", "construct"
        ]
        self.targets = [
            "artifact", "treasure", "person", "creature", "document",
            "weapon", "jewel", "prisoner", "refugee", "knowledge"
        ]
        self.locations = [
            "Ancient Forest", "Crystal Caverns", "Volcanic Mountains", "Frozen Tundra",
            "Desert Wastes", "Enchanted Valley", "Dark Swamps", "Sky Citadel"
        ]
        self.rewards = ["gold", "experience", "item", "knowledge", "favor", "title"]
        self.difficulties = ["Easy", "Medium", "Hard", "Legendary"]
    
    def generate_quest(self):
        # Generate a complete random quest.
        objective = random.choice(self.objectives).capitalize()
        target = random.choice(self.targets)
        location = random.choice(self.locations)
        difficulty = random.choice(self.difficulties)
        reward = random.choice(self.rewards)
        reward_value = random.randint(100, 1000) if reward == "gold" else random.randint(50, 300)
        
        quest_text = f"\n{'=' * 50}\n"
        quest_text += f"⚔️ QUEST: {objective} {target.upper()}\n"
        quest_text += f"{'=' * 50}\n"
        quest_text += f"Location: {location}\n"
        quest_text += f"Difficulty: {difficulty}\n"
        quest_text += f"Objective: {objective} the {target} in {location}\n"
        quest_text += f"Reward: {reward_value} {reward}\n"
        quest_text += f"{'=' * 50}\n"
        
        return quest_text
