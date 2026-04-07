# Statistical Analysis Module for RPG Character Manager - provides data analysis and statistical insights

import pandas as pd
import numpy as np
from collections import Counter

class StatisticalAnalyzer:
    # Analyzes character data to provide statistical insights and metrics. Works with Character objects and DataFrames for comprehensive analysis.
    
    def __init__(self, roster):
        # Initialize analyzer with a character roster.
        self.roster = roster
        
    def get_average_stats(self):
        # Calculate average stats across all characters.
        if not self.roster.characters:
            return {}
        
        df = self.roster.get_dataframe()
        if df.empty:
            return {}
        
        # Get numeric columns only (exclude Name, Race, Class columns)
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        return df[numeric_cols].mean().to_dict()
    
    def get_median_stats(self):
        # Calculate median stats across all characters.
        if not self.roster.characters:
            return {}
        
        df = self.roster.get_dataframe()
        if df.empty:
            return {}
        
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        return df[numeric_cols].median().to_dict()
    
    def get_max_stats(self):
        # Get maximum stat values across roster.
        if not self.roster.characters:
            return {}
        
        df = self.roster.get_dataframe()
        if df.empty:
            return {}
        
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        return df[numeric_cols].max().to_dict()
    
    def get_min_stats(self):
        # Get minimum stat values across roster.
        if not self.roster.characters:
            return {}
        
        df = self.roster.get_dataframe()
        if df.empty:
            return {}
        
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        return df[numeric_cols].min().to_dict()
    
    def get_stat_variance(self):
        # Calculate variance of stats across roster.
        if not self.roster.characters:
            return {}
        
        df = self.roster.get_dataframe()
        if df.empty:
            return {}
        
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        return df[numeric_cols].var().to_dict()
    
    def get_stat_std_deviation(self):
        # Calculate standard deviation of stats across roster.
        if not self.roster.characters:
            return {}
        
        df = self.roster.get_dataframe()
        if df.empty:
            return {}
        
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        return df[numeric_cols].std().to_dict()
    
    def get_class_distribution(self):
        # Get distribution of character classes in roster.
        if not self.roster.characters:
            return {}
        
        df = self.roster.get_dataframe()
        if df.empty or 'Class' not in df.columns:
            return {}
        
        return df['Class'].value_counts().to_dict()
    
    def get_race_distribution(self):
        # Get distribution of character races in roster.
        if not self.roster.characters:
            return {}
        
        df = self.roster.get_dataframe()
        if df.empty or 'Race' not in df.columns:
            return {}
        
        return df['Race'].value_counts().to_dict()
    
    def get_level_distribution(self):
        # Get distribution of character levels in roster.
        if not self.roster.characters:
            return {}
        
        df = self.roster.get_dataframe()
        if df.empty or 'Level' not in df.columns:
            return {}
        
        return df['Level'].value_counts().sort_index().to_dict()
    
    def get_characters_by_class(self, char_class):
        # Get list of characters in a specific class.
        df = self.roster.get_dataframe()
        if df.empty or 'Class' not in df.columns:
            return []
        
        class_chars = df[df['Class'] == char_class]['Name'].tolist()
        return class_chars
    
    def get_characters_by_race(self, race):
        # Get list of characters of a specific race.
        df = self.roster.get_dataframe()
        if df.empty or 'Race' not in df.columns:
            return []
        
        race_chars = df[df['Race'] == race]['Name'].tolist()
        return race_chars
    
    def get_average_level(self):
        # Get average level of characters in roster.
        if not self.roster.characters:
            return 0
        
        df = self.roster.get_dataframe()
        if df.empty or 'Level' not in df.columns:
            return 0
        
        return df['Level'].mean()
    
    def get_total_characters(self):
        # Get total number of characters.
        return len(self.roster)
    
    def get_strongest_character(self, stat='Level'):
        # Get character with highest value for a stat.
        if not self.roster.characters:
            return None
        
        df = self.roster.get_dataframe()
        if df.empty or stat not in df.columns:
            return None
        
        idx = df[stat].idxmax()
        return df.loc[idx, 'Name']
    
    def get_weakest_character(self, stat='Level'):
        # Get character with lowest value for a stat.
        if not self.roster.characters:
            return None
        
        df = self.roster.get_dataframe()
        if df.empty or stat not in df.columns:
            return None
        
        idx = df[stat].idxmin()
        return df.loc[idx, 'Name']
    
    def generate_statistical_report(self):
        # Generate a comprehensive statistical report of the roster.
        if not self.roster.characters:
            return "No characters in roster."
        
        report = []
        report.append("\n" + "=" * 50)
        report.append("📊 ROSTER STATISTICAL REPORT")
        report.append("=" * 50)
        
        # Basic counts
        report.append(f"\n📈 ROSTER STATUS:")
        report.append(f"   Total Characters: {self.get_total_characters()}")
        report.append(f"   Average Level: {self.get_average_level():.1f}")
        
        # Class distribution
        report.append(f"\n🎮 CLASS DISTRIBUTION:")
        class_dist = self.get_class_distribution()
        for cls, count in sorted(class_dist.items()):
            percentage = (count / self.get_total_characters()) * 100
            report.append(f"   {cls}: {count} ({percentage:.1f}%)")
        
        # Race distribution
        report.append(f"\n👥 RACE DISTRIBUTION:")
        race_dist = self.get_race_distribution()
        for race, count in sorted(race_dist.items()):
            percentage = (count / self.get_total_characters()) * 100
            report.append(f"   {race}: {count} ({percentage:.1f}%)")
        
        # Level distribution
        report.append(f"\n📊 LEVEL DISTRIBUTION:")
        level_dist = self.get_level_distribution()
        for level in sorted(level_dist.keys()):
            count = level_dist[level]
            percentage = (count / self.get_total_characters()) * 100
            report.append(f"   Level {level}: {count} character(s) ({percentage:.1f}%)")
        
        # Average stats
        report.append(f"\n⚡ AVERAGE CHARACTER STATS:")
        avg_stats = self.get_average_stats()
        for stat, value in sorted(avg_stats.items()):
            report.append(f"   {stat}: {value:.1f}")
        
        # Summary stats
        report.append(f"\n🔍 CHARACTER EXTREMES:")
        report.append(f"   Strongest (by Level): {self.get_strongest_character('Level')}")
        report.append(f"   Weakest (by Level): {self.get_weakest_character('Level')}")
        
        report.append("\n" + "=" * 50 + "\n")
        
        return "\n".join(report)
    
    def get_character_comparison(self, char1_name, char2_name):
        # Compare two specific characters.
        char1 = self.roster.get_character(char1_name)
        char2 = self.roster.get_character(char2_name)
        
        if not char1 or not char2:
            return "One or both characters not found."
        
        comparison = []
        comparison.append("\n" + "=" * 50)
        comparison.append(f"🎯 CHARACTER COMPARISON")
        comparison.append("=" * 50)
        
        comparison.append(f"\n{char1_name.upper()}")
        comparison.append(f"   Race: {char1.race}")
        comparison.append(f"   Class: {char1.char_class}")
        comparison.append(f"   Level: {char1.level}")
        comparison.append(f"   Total Stats: {char1.get_total_stats()}")
        comparison.append(f"   Average Stat: {char1.get_average_stats():.1f}")
        
        comparison.append(f"\n{char2_name.upper()}")
        comparison.append(f"   Race: {char2.race}")
        comparison.append(f"   Class: {char2.char_class}")
        comparison.append(f"   Level: {char2.level}")
        comparison.append(f"   Total Stats: {char2.get_total_stats()}")
        comparison.append(f"   Average Stat: {char2.get_average_stats():.1f}")
        
        comparison.append(f"\n⚔️ STAT-BY-STAT COMPARISON:")
        for stat_name in char1.attributes.keys():
            val1 = char1.attributes.get(stat_name, 0)
            val2 = char2.attributes.get(stat_name, 0)
            diff = val1 - val2
            winner = char1_name if diff > 0 else (char2_name if diff < 0 else "TIE")
            comparison.append(f"   {stat_name}: {char1_name} ({val1}) vs {char2_name} ({val2}) → {winner}")
        
        comparison.append("\n" + "=" * 50 + "\n")
        
        return "\n".join(comparison)


class OptimizationRecommender:
    # Provides character optimization recommendations based on stats and build.
    
    def __init__(self, character):
        # Initialize with a character to analyze.
        self.character = character
    
    def get_recommendations(self):
        # Generate optimization recommendations for character.
        recommendations = []
        recommendations.append(f"\n📋 OPTIMIZATION RECOMMENDATIONS FOR {self.character.name.upper()}")
        recommendations.append("-" * 50)
        
        stats = self.character.attributes
        total = self.character.get_total_stats()
        avg = self.character.get_average_stats()
        
        # Analyze strengths and weaknesses
        strong_stats = {k: v for k, v in stats.items() if v > avg * 1.2}
        weak_stats = {k: v for k, v in stats.items() if v < avg * 0.8}
        
        if strong_stats:
            recommendations.append(f"\n✓ STRENGTHS:")
            for stat, value in strong_stats.items():
                recommendations.append(f"   {stat}: {value} (Excellent)")
        
        if weak_stats:
            recommendations.append(f"\n⚠ AREAS FOR IMPROVEMENT:")
            for stat, value in weak_stats.items():
                recommendations.append(f"   {stat}: {value} (Below average)")
        
        # Class-specific recommendations
        recommendations.append(f"\n🎯 CLASS-SPECIFIC RECOMMENDATIONS FOR {self.character.char_class.upper()}:")
        
        class_recommendations = {
            'Black Mage': "Focus on Magic (Mag) and Speed (Spd). Consider reducing Defense.",
            'Warrior': "Focus on Strength (Str) and Defense (Def). Consider improving Speed.",
            'Thief': "Focus on Speed (Spd) and Accuracy (Acc). Balance Evasion (Evs).",
            'White Mage': "Focus on Spirit (Spr) and Magic (Mag). Balance HP and Defense."
        }
        
        rec = class_recommendations.get(self.character.char_class, "Build depends on playstyle.")
        recommendations.append(f"   {rec}")
        
        recommendations.append(f"\n📊 OVERALL ASSESSMENT:")
        recommendations.append(f"   Total Stats: {total}")
        recommendations.append(f"   Average Stat: {avg:.1f}")
        recommendations.append(f"   Character Level: {self.character.level}")
        recommendations.append(f"   Build Diversity: {'Balanced' if len(strong_stats) > 2 else 'Specialized'}")
        
        recommendations.append("-" * 50 + "\n")
        
        return "\n".join(recommendations)
