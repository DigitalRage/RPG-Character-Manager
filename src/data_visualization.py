# Data Visualization Module for RPG Character Manager - creates charts and graphs for character stat visualization

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle
import os

class DataVisualization:
    # Handles visualization of character data using Matplotlib.
    # Supports radar charts, bar graphs, and comparison charts.
    
    def __init__(self, output_dir="character_charts"):
        # Initialize visualization module with output directory.
        self.output_dir = output_dir
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
    def create_radar_chart(self, character, save=True):
        # Create a radar chart for a single character's stats.
        #
        # Args:
        #     character: Character object with attributes
        #     save: Whether to save the chart to file
        #
        # Returns:
        #     Filename if saved, None otherwise
        # Get attributes for radar chart
        attributes = character.get_stat_distribution()
        
        # Filter to only numeric attributes (exclude extreme outliers)
        stats_to_plot = {k: v for k, v in attributes.items() if isinstance(v, (int, float))}
        
        if not stats_to_plot:
            print("No numeric attributes to visualize.")
            return None
        
        # Number of variables
        num_vars = len(stats_to_plot)
        
        # Compute angle for each axis
        angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
        values = list(stats_to_plot.values())
        
        # Complete the loop
        angles += angles[:1]
        values += values[:1]
        
        # Create plot
        fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(projection='polar'))
        
        # Plot data
        ax.plot(angles, values, 'o-', linewidth=2, color='#FF6B6B', label=character.name)
        ax.fill(angles, values, alpha=0.25, color='#FF6B6B')
        
        # Fix axis to go in the same direction as expected
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(stats_to_plot.keys(), size=10)
        
        # Set y-axis limits
        max_value = max(values[:-1])
        ax.set_ylim(0, max_value * 1.2)
        ax.set_yticks(np.arange(0, max_value * 1.2, max_value * 0.2))
        
        # Add title and legend
        title = f"📊 {character.name} - Character Profile\n{character.race} {character.char_class} | Level {character.level}"
        plt.title(title, size=16, weight='bold', pad=20)
        ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
        
        # Add gridlines
        ax.grid(True, linestyle='--', alpha=0.7)
        
        # Save figure
        if save:
            filename = f"{self.output_dir}/{character.name}_radar_{character.level}.png"
            plt.tight_layout()
            plt.savefig(filename, dpi=300, bbox_inches='tight')
            print(f"✓ Radar chart saved: {filename}")
            plt.close()
            return filename
        else:
            plt.show()
            return None
    
    def create_bar_chart(self, character, save=True):
        # Create a bar chart for a single character's stats.
        #
        # Args:
        #     character: Character object with attributes
        #     save: Whether to save the chart to file
        #
        # Returns:
        #     Filename if saved, None otherwise
        attributes = character.get_stat_distribution()
        stats_to_plot = {k: v for k, v in attributes.items() if isinstance(v, (int, float))}
        
        if not stats_to_plot:
            print("No numeric attributes to visualize.")
            return None
        
        # Create figure
        fig, ax = plt.subplots(figsize=(12, 6))
        
        # Create bar chart
        names = list(stats_to_plot.keys())
        values = list(stats_to_plot.values())
        colors = plt.cm.viridis(np.linspace(0, 1, len(names)))
        
        bars = ax.bar(names, values, color=colors, edgecolor='black', linewidth=1.5)
        
        # Add value labels on bars
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{int(height)}',
                   ha='center', va='bottom', fontweight='bold')
        
        # Formatting
        title = f"📊 {character.name}'s Character Stats - {character.race} {character.char_class} (Level {character.level})"
        ax.set_title(title, fontsize=14, fontweight='bold', pad=20)
        ax.set_xlabel("Attributes", fontsize=12, fontweight='bold')
        ax.set_ylabel("Value", fontsize=12, fontweight='bold')
        ax.grid(axis='y', alpha=0.3, linestyle='--')
        ax.set_axisbelow(True)
        
        # Rotate x labels if needed
        plt.xticks(rotation=45, ha='right')
        
        if save:
            filename = f"{self.output_dir}/{character.name}_bar_{character.level}.png"
            plt.tight_layout()
            plt.savefig(filename, dpi=300, bbox_inches='tight')
            print(f"✓ Bar chart saved: {filename}")
            plt.close()
            return filename
        else:
            plt.show()
            return None
    
    def create_comparison_chart(self, characters, save=True):
        # Create a comparison chart for multiple characters.
        #
        # Args:
        #     characters: List of Character objects
        #     save: Whether to save the chart to file
        #
        # Returns:
        #     Filename if saved, None otherwise
        if not characters:
            print("No characters to compare.")
            return None
        
        # Get common attributes across all characters
        common_stats = set(characters[0].get_stat_distribution().keys())
        for char in characters[1:]:
            common_stats &= set(char.get_stat_distribution().keys())
        
        # Filter numeric attributes
        common_stats = {k: v for k, v in characters[0].get_stat_distribution().items() 
                       if k in common_stats and isinstance(v, (int, float))}
        
        if not common_stats:
            print("No common numeric attributes to compare.")
            return None
        
        # Prepare data
        x = np.arange(len(common_stats))
        width = 0.8 / len(characters)
        
        fig, ax = plt.subplots(figsize=(14, 6))
        
        # Create bars for each character
        colors = plt.cm.Set3(np.linspace(0, 1, len(characters)))
        for idx, character in enumerate(characters):
            stats = character.get_stat_distribution()
            values = [stats.get(stat, 0) for stat in common_stats.keys()]
            ax.bar(x + idx * width, values, width, label=character.name, color=colors[idx], edgecolor='black')
        
        # Formatting
        title = f"🎯 Character Comparison - {', '.join([c.name for c in characters])}"
        ax.set_title(title, fontsize=14, fontweight='bold', pad=20)
        ax.set_xlabel("Attributes", fontsize=12, fontweight='bold')
        ax.set_ylabel("Value", fontsize=12, fontweight='bold')
        ax.set_xticks(x + width * (len(characters) - 1) / 2)
        ax.set_xticklabels(common_stats.keys(), rotation=45, ha='right')
        ax.legend(fontsize=10)
        ax.grid(axis='y', alpha=0.3, linestyle='--')
        ax.set_axisbelow(True)
        
        if save:
            filename = f"{self.output_dir}/comparison_{len(characters)}_characters.png"
            plt.tight_layout()
            plt.savefig(filename, dpi=300, bbox_inches='tight')
            print(f"✓ Comparison chart saved: {filename}")
            plt.close()
            return filename
        else:
            plt.show()
            return None
    
    def create_attribute_distribution(self, roster, save=True):
        # Create chart showing attribute distribution across roster.
        #
        # Args:
        #     roster: List of characters or CharacterRoster object
        #     save: Whether to save the chart to file
        #
        # Returns:
        #     Filename if saved, None otherwise
        # Handle both list and CharacterRoster objects
        if hasattr(roster, 'get_roster_as_list'):
            characters = roster.get_roster_as_list()
        else:
            characters = roster
        
        if not characters:
            print("No characters in roster.")
            return None
        
        # Collect all stat values
        stat_collections = {}
        for character in characters:
            for stat_name, stat_value in character.get_stat_distribution().items():
                if isinstance(stat_value, (int, float)):
                    if stat_name not in stat_collections:
                        stat_collections[stat_name] = []
                    stat_collections[stat_name].append(stat_value)
        
        if not stat_collections:
            print("No numeric attributes found.")
            return None
        
        # Create box plots
        fig, ax = plt.subplots(figsize=(12, 6))
        
        stat_names = list(stat_collections.keys())
        stat_data = [stat_collections[name] for name in stat_names]
        
        bp = ax.boxplot(stat_data, labels=stat_names, patch_artist=True)
        
        # Color the boxes
        colors = plt.cm.Pastel1(np.linspace(0, 1, len(stat_names)))
        for patch, color in zip(bp['boxes'], colors):
            patch.set_facecolor(color)
        
        ax.set_title(f"📈 Attribute Distribution Across {len(characters)} Characters", 
                    fontsize=14, fontweight='bold', pad=20)
        ax.set_xlabel("Attributes", fontsize=12, fontweight='bold')
        ax.set_ylabel("Value", fontsize=12, fontweight='bold')
        ax.grid(axis='y', alpha=0.3, linestyle='--')
        ax.set_axisbelow(True)
        plt.xticks(rotation=45, ha='right')
        
        if save:
            filename = f"{self.output_dir}/distribution_roster_{len(characters)}.png"
            plt.tight_layout()
            plt.savefig(filename, dpi=300, bbox_inches='tight')
            print(f"✓ Distribution chart saved: {filename}")
            plt.close()
            return filename
        else:
            plt.show()
            return None
