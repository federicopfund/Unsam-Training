Data Analysis Module

This folder contains Python scripts for advanced data analysis, visualization, and processing tasks. All scripts follow professional coding standards with proper documentation, logging, and pipeline compatibility.

Files:

1. pearson_correlation.py
   - Analyzes correlation between two tide measuring stations (San Fernando, Buenos Aires)
   - Calculates Pearson correlation coefficients with various time shifts
   - Interpolates data at finer resolution for detailed analysis
   - Usage: python pearson_correlation.py [data_file.csv]

2. random_walk_plots.py
   - Simulates and analyzes random walk processes
   - Creates moving average smoothing with configurable windows
   - Multi-person simulation for 8-hour walks
   - Exports results to CSV format
   - Usage: python random_walk_plots.py

3. boxplot_reading_selection.py
   - Reads and filters tree species data from forest datasets
   - Creates boxplots for tree measurements by species
   - Generates pairplots for multi-dimensional analysis
   - Usage: python boxplot_reading_selection.py [dataset_file.csv]

4. tree_park_sidewalks.py
   - Comparative analysis of tree species in parks vs sidewalks
   - Combines datasets from different environments
   - Generates side-by-side visualizations
   - Usage: python tree_park_sidewalks.py [parks_file.csv] [sidewalks_file.csv]

5. tides_manual.py
   - Tide data analysis with time series manipulation
   - Implements time shifting to find correlations between stations
   - Plots multiple time ranges for visual analysis
   - Usage: python tides_manual.py [tide_data.csv]

6. tides_fft.py
   - Fast Fourier Transform (FFT) analysis of tide data
   - Identifies dominant frequencies in tidal patterns
   - Detects spectral peaks with configurable prominence
   - Analyzes both San Fernando and Buenos Aires stations
   - Usage: python tides_fft.py [data_file.csv] [start_date] [end_date]

7. tides_manual_fft.py
   - Manual FFT implementation and analysis
   - Demonstrates frequency domain signal processing
   - Includes peak detection and phase analysis
   - Educational implementation with detailed documentation
   - Usage: python tides_manual_fft.py [data_file.csv] [start_date] [end_date]

8. life_simulation.py
   - Calculates total seconds lived based on birth date
   - Interactive user input for birth date
   - Displays comprehensive life statistics (years, months, weeks, days, hours, minutes, seconds)
   - Usage: python life_simulation.py

9. sort_images.py
   - Recursively scans directories for PNG images
   - Renames images based on embedded date patterns (name_YYYYMMDD.png)
   - Updates file modification timestamps
   - Creates output directory for processed images
   - Usage: python sort_images.py [root_directory]

10. sort_images1.py
    - Enhanced image organization with metadata extraction
    - Groups images by modification date
    - Creates shadow directory structure organized by date
    - Generates organization reports
    - Usage: python sort_images1.py [root_directory]

11. list_images.py
    - Discovers and lists all PNG images in a directory
    - Displays comprehensive image statistics
    - Exports image list to text file
    - Usage: python list_images.py [root_directory] [--export or -e]

Code Quality & Professional Standards:
- Comprehensive logging for pipeline compatibility
- Proper error handling with informative messages
- Type hints for better code clarity (PEP 484)
- Function-based architecture for modularity and reusability
- Command-line argument support for different environments
- Professional docstrings following PEP 257 conventions
- Configurable parameters for different use cases
- Clean, readable code following PEP 8 style guide

Function Naming Conventions:
- load_* : Loading data from files
- calculate_* : Mathematical computations
- plot_* : Visualization functions
- create_* : Object creation functions
- find_* : Search and detection functions
- display_* : Output and presentation functions
- export_* : Save to file functions
- extract_* : Data extraction functions

Requirements:
pip install pandas numpy matplotlib seaborn scipy

Running Examples:
python pearson_correlation.py ../Data/OBS_SHN_SF-BA.csv
python random_walk_plots.py
python list_images.py ../Data --export
python tides_fft.py ../Data/OBS_SHN_SF-BA.csv 2014-01 2014-06
python boxplot_reading_selection.py arbolado-publico-lineal-2017-2018.csv
