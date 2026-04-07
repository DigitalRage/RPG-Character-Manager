# Enhanced RPG Character Manager
***
![Screenshot of the RPG Character Manager running](assets/Screenshot%202026-04-06%20192936.png)

The Enhanced RPG Character Manager is a comprehensive Python application that combines object-oriented programming with powerful data analysis and visualization libraries. This project demonstrates the integration of **Pandas**, **Matplotlib**, and **Faker** to create a robust character management system with statistical analysis, visualization capabilities, and procedural content generation. Build and manage an RPG character roster with advanced stat visualization, statistical analysis, and random character generation features.

## How to use
***
1. **Install Python 3.7 or higher** from [python.org](https://www.python.org/)
2. **Clone or download the repository** to your local machine
3. **Navigate to project directory**: `cd RPG-Character-Manager`
4. **Install required libraries** using pip:
   - `pandas>=1.3.0` - Data analysis and manipulation
   - `matplotlib>=3.4.0` - Data visualization (charts and graphs)
   - `faker>=8.0.0` - Realistic random data generation
   - `numpy>=1.21.0` - Numerical computing
   - Install with: `pip install -r requirements.txt`
5. **Run the application**: `python src/main.py`
6. **Follow the on-screen menu** to create characters, visualize data, analyze stats, and export data

## Details on Project features
***
- 🎮 **Core Character Management** - Create, edit, delete, and browse RPG characters with custom races, classes, levels, and attributes
- 📊 **Data Visualization** - Generate radar charts, bar charts, multi-character comparisons, and attribute distribution analysis with automatic PNG export
- 📈 **Statistical Analysis** - Calculate roster statistics (mean, median, min, max, standard deviation), class/race/level distributions, and character comparisons
- 🎯 **Character Optimization** - Receive personalized optimization recommendations based on character build, strengths, weaknesses, and class-specific tips
- 🎲 **Random Generation** - Procedurally generate random characters with Faker-generated names, backstories, personalities, equipment descriptions, and random quests
- 💾 **Data Management** - Export/import character data in CSV and JSON formats, create timestamped backups, restore from previous backups, and validate character data
- 🐼 **Pandas Integration** - Convert character rosters to DataFrames for advanced data analysis and filtering operations
- 📋 **Detailed Reporting** - Generate comprehensive statistical reports and export detailed character information with all attributes

## Installation Instructions
***
This project is designed for educational purposes and learning data analysis with Python.

**Prerequisites:**
- Python 3.7 or higher
- pip package manager
- All required dependencies listed in `requirements.txt`

**Quick Setup:**
```bash
# Clone or download the repository
git clone <repository-url>
cd RPG-Character-Manager

# Install dependencies
pip install -r requirements.txt

# Run the application
python src/main.py
```

**Note:** This is a class project with no executable setup file. All functionality runs through the Python script with an interactive command-line menu.

## Licence
***
This project is made for school and has no copyright. Feel free to use, modify, and distribute.

## Contributers
- DigitalRage

## Contribute
***
Not being used for this class. Instructions for how to submit a change to the repository if it is open source.

### StatisticalAnalyzer Class
**Key Methods:**
- `get_average_stats()`: Calculate mean values
- `get_median_stats()`: Calculate median values
- `get_class_distribution()`: Count by class
- `get_race_distribution()`: Count by race
- `generate_statistical_report()`: Create comprehensive report
- `get_character_comparison()`: Detailed character comparison

### RandomGenerator Class
**Key Methods:**
- `generate_full_character()`: Create complete random character
- `generate_character_template()`: Create class-optimized template
- `generate_backstory()`: Generate character backstory
- `generate_quest()`: Generate random quest

### DataManager Class
**Key Methods:**
- `export_to_csv()`: Save to CSV format
- `import_from_csv()`: Load from CSV
- `export_to_json()`: Save to JSON format
- `import_from_json()`: Load from JSON
- `create_backup()`: Create timestamped backup
- `restore_from_backup()`: Restore from backup file

## Library Integration

### Pandas
- **DataFrame Operations**: Convert roster to DataFrame for analysis
- **Statistical Functions**: Built-in mean, median, min, max calculations
- **Filtering**: Filter characters by attributes using DataFrame queries
- **Export**: Save character data to CSV format

### Matplotlib
- **Radar Charts**: Visualize stats in polar coordinates
- **Bar Charts**: Display attribute comparisons
- **Box Plots**: Show distribution analysis
- **High-Resolution Export**: Save all charts as 300 DPI PNG files

### Faker
- **Name Generation**: Create realistic character names
- **Backstory Components**: Generate personality traits and descriptions
- **Seeding**: Support reproducible random generation

## Error Handling
- **Input Validation**: All user inputs are validated before processing
- **File Operations**: Graceful error handling for save/load operations
- **Data Integrity**: Validation checks ensure character data consistency
- **User Feedback**: Clear error messages guide user corrections

## Example Workflow

```python
# 1. Run the application
python main.py

# 2. Create a character
# Select option 4, fill in character details

# 3. Generate a random character to compare
# Select option 8, generate a random character

# 4. Visualize both characters
# Select option 1, create radar charts for comparison

# 5. Analyze your roster
# Select option 2, view statistical report

# 6. Export your data
# Select option 9, export to JSON for backup
```

## Sample Character Statistics Report

```
==================================================
📊 ROSTER STATISTICAL REPORT
==================================================

📈 ROSTER STATUS:
   Total Characters: 5
   Average Level: 7.4

🎮 CLASS DISTRIBUTION:
   Black Mage: 1 (20.0%)
   Warrior: 2 (40.0%)
   Thief: 1 (20.0%)
   White Mage: 1 (20.0%)

👥 RACE DISTRIBUTION:
   Human: 2 (40.0%)
   Elf: 1 (20.0%)
   Dwarf: 1 (20.0%)
   Dragonborn: 1 (20.0%)

⚡ AVERAGE CHARACTER STATS:
   MP: 12.4
   HP: 54.0
   Str: 14.4
   Atk: 12.8
   ...

🔍 CHARACTER EXTREMES:
   Strongest (by Level): Thalorin
   Weakest (by Level): Grimjaw
```

## Tips & Best Practices

1. **Regular Backups**: Use the backup feature to save your roster periodically
2. **Character Templates**: Generate class templates to quickly create balanced characters
3. **Stat Distribution**: Use visualization to identify character building trends
4. **Comparison Analysis**: Compare characters to optimize builds
5. **Export Reports**: Save analysis reports for record-keeping

## Troubleshooting

### Issue: "No module named 'pandas'"
**Solution**: Install pandas with `pip install pandas`

### Issue: "Charts not saving"
**Solution**: Ensure `character_charts/` directory exists. The application creates it automatically.

### Issue: "Character import fails"
**Solution**: Verify CSV/JSON format matches export structure. Check for encoding issues.

### Issue: "Random generator not working"
**Solution**: Ensure Faker is installed with `pip install faker`

## Credits

- **Pandas**: Data analysis and manipulation
- **Matplotlib**: Data visualization and plotting  
- **Faker**: Realistic data generation
- **NumPy**: Numerical operations

## License

This project is provided as-is for educational purposes.

## Future Enhancements

Potential features for future versions:
- Character leveling system with XP
- Item and equipment management
- Battle system implementation
- Multi-character party management
- Database backend integration
- Web interface
- Multiplayer support

## Support

For issues or questions:
1. Check the Troubleshooting section
2. Review the Usage Guide for detailed instructions
3. Check that all dependencies are properly installed

---

**Thank you for using the Enhanced RPG Character Manager!** 🎭⚔️🛡️

Enjoy creating and managing your RPG characters!
