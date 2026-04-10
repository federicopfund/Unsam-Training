# Data Analysis Module: Technical & Scientific Documentation

**Author:** Federico Pfund  
**Institution:** Universidad Nacional de San Martín (UNSAM)  
**Created:** 2026  
**Version:** 1.0.0  

## Table of Contents
1. [Module Overview](#module-overview)
2. [Architecture & Design](#architecture--design)
3. [Script Documentation](#script-documentation)
   - [Random Walk Analysis](#1-random-walk-analysis)
   - [Pearson Correlation Analysis](#2-pearson-correlation-analysis)
   - [Tides FFT Spectral Analysis](#3-tides-fft-spectral-analysis)
   - [Manual FFT Implementation](#4-manual-fft-implementation)
   - [Tides Manual Time-Series](#5-tides-manual-time-series)
   - [Tree Environment Comparison](#6-tree-environment-comparison)
   - [Boxplot Reading Selection](#7-boxplot-reading-selection)
   - [Life Simulation](#8-life-simulation)
   - [Image Processing & Sorting](#9-image-processing--sorting)
   - [Image Discovery](#10-image-discovery)
4. [Technical Stack](#technical-stack)
5. [Execution Guidelines](#execution-guidelines)
6. [Testing & Validation](#testing--validation)

---

## Module Overview

This data analysis module implements a collection of scientific computing techniques and statistical methodologies for examining real-world datasets. The module encompasses:

- **Time-Series Analysis:** Oceanographic tide data from Buenos Aires and San Fernando stations
- **Spectral Analysis:** Frequency domain decomposition using Fast Fourier Transform (FFT)
- **Stochastic Processes:** Random walk simulation and statistical characterization
- **Comparative Analysis:** Tree distribution patterns across different urban environments
- **Signal Processing:** Image metadata manipulation and organized archiving
- **Correlation Analysis:** Lagrange-based temporal relationship quantification

All scripts follow professional Python development standards:
- **PEP 8:** Code style and formatting
- **PEP 257:** Documentation standards
- **PEP 484:** Type hints and static analysis
- **Logging:** Comprehensive event tracking
- **Error Handling:** Robust exception management
- **Modular Design:** Reusable functions with single responsibilities

---

## Architecture & Design

### Module Structure
```
data_analysis/
├── documentation/          # Technical documentation
├── *.py                   # Analysis scripts
├── test_all_scripts.py    # Comprehensive test suite
├── Data/                  # Data directory
└── readme.txt            # Module-level notes
```

### Design Principles

**1. Functional Decomposition**
Each script is organized as a collection of pure functions with single responsibilities:
- Data ingestion and validation
- Computation and transformation
- Visualization and reporting

**2. Type Safety**
All functions include complete type annotations:
```python
def analyze_data(
    dataframe: pd.DataFrame,
    window_size: int = 30
) -> Tuple[np.ndarray, float]:
```

**3. Logging Integration**
Structured logging at multiple levels:
- `INFO`: Major workflow steps
- `WARNING`: Data quality issues
- `ERROR`: Exception conditions
- `DEBUG`: Detailed diagnostic information

**4. Failure Management**
- Try-except blocks for robust error handling
- Graceful degradation when optional data unavailable
- Informative error messages for debugging

**5. Pipeline Compatibility**
All scripts support command-line execution with optional arguments:
```bash
python script_name.py [arg1] [arg2]
```

---

## Script Documentation

### 1. Random Walk Analysis
**File:** `random_walk_plots.py`  
**Category:** Stochastic Process Simulation  
**Lines of Code:** 186  

#### Scientific Foundation

**Theoretical Context:**
Random walks are fundamental models in probability theory and statistical physics. They describe the trajectory of a particle moving randomly in space, with applications spanning:
- Brownian motion (physics)
- Stock price movements (financial engineering)
- Diffusion processes (chemistry)
- Genetic drift (population biology)

**Mathematical Formulation:**
For a 1D random walk on the discrete integer lattice:
$$X_n = X_0 + \sum_{i=1}^{n} \epsilon_i$$

Where:
- $X_n$ = position at step $n$
- $\epsilon_i \sim \text{Uniform}(-1, +1)$ = random displacement
- $E[X_n] = E[X_0]$ (martingale property)
- $\text{Var}(X_n) = n \cdot \text{Var}(\epsilon_i)$ (variance grows linearly)

#### Implementation Overview

**Core Functions:**

1. **`create_single_random_walk(steps, increment_range)`**
   - Generates a single trajectory using `np.random.uniform()`
   - Computes cumulative sum via `np.cumsum()`
   - Time complexity: $O(n)$
   - Memory complexity: $O(n)$

2. **`smooth_walk(walk, window_size)`**
   - Applies moving average filter for noise reduction
   - Implementation: `pd.Series.rolling()`
   - Filter order: user-configurable
   - Preserves long-term trends while eliminating high-frequency noise

3. **`create_multiple_people_walks(people_count, time_period, frequency)`**
   - Creates ensemble of trajectories (Monte Carlo approach)
   - Generates $p$ independent walks over $T$ time steps
   - Enables statistical characterization of walk properties

4. **`export_walks(dataframe, filename)`**
   - Serializes results to CSV format
   - Facilitates downstream analysis and archiving

#### Computational Methodology

**Step-by-step workflow:**
1. Initialize random seed for reproducibility
2. Generate 12 independent random walkers
3. Simulate 8-hour period (480 minutes) at 1-minute resolution
4. Apply Savitzky-Golay smoothing (window=11, order=2)
5. Compute ensemble statistics (mean, std, quantiles)
6. Generate visualizations (individual, ensemble, comparison)
7. Export results to persistent storage

#### Expected Output Characteristics

**Statistical Properties:**
- Mean trajectory: approximately zero (unbiased)
- Variance: increases with time (diffusion)
- Distribution of final positions: approaching normal (CLT)

**Visualization Outputs:**
- Individual walk comparison (12 walkers, original vs smoothed)
- Ensemble statistics (mean ± std bands)
- Smoothed trajectories showing typical patterns

#### Use Cases
- Model crowd movement in public spaces
- Simulate drug molecules in cellular media
- Analyze stock price trajectories
- Study particle diffusion in gases

#### Execution
```bash
python random_walk_plots.py
```

---

### 2. Pearson Correlation Analysis
**File:** `pearson_correlation.py`  
**Category:** Time-Series Correlation & Interpolation  
**Lines of Code:** 210  

#### Scientific Foundation

**Theoretical Context:**
Pearson correlation coefficient measures linear association between bivariate distributions. For time-shifted variables, it quantifies temporal coherence in oceanographic measurements.

**Mathematical Definition:**
$$r_{xy} = \frac{\text{Cov}(X, Y)}{\sigma_X \sigma_Y} = \frac{\sum_{i=1}^{n}(x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum(x_i-\bar{x})^2}\sqrt{\sum(y_i-\bar{y})^2}}$$

Properties:
- $r_{xy} \in [-1, 1]$
- $r = 1$: perfect positive linear relationship
- $r = -1$: perfect negative linear relationship
- $r = 0$: no linear correlation

**Lagrange Interpolation:**
For non-uniformly sampled or missing data points, Lagrange polynomial interpolation reconstructs smooth curves:
$$P(x) = \sum_{j=0}^{n} y_j \prod_{k=0, k \neq j}^{n} \frac{x - x_k}{x_j - x_k}$$

#### Implementation Overview

**Core Functions:**

1. **`load_tide_data(filepath, start_date, end_date)`**
   - CSV parsing with datetime indexing
   - Temporal subsetting: slicing by date range
   - Data validation: checking for missing values
   - Output: pandas Series objects with time indices

2. **`interpolate_and_correlate(heights_sf, heights_ba, frequency_hours)`**
   - Computes correlation across multiple time lags
   - Implements cubic Lagrange interpolation
   - Validation: resampling with 'min' (minute) frequency
   - Algorithm:
     * Interpolate both series to common grid
     * For each lag $\tau \in [-24, 24]$ hours:
       - Shift one series by $\tau$
       - Compute Pearson $r$ at this lag
     * Identify maximum correlation lag

3. **`calculate_lagrange_correlation(x, y, lag_hours)`**
   - Interpolates both sequences
   - Computes correlation at specific lag
   - Handles edge cases (NaN, short sequences)

4. **`plot_correlation_results(lags, correlations, peak_lag)`**
   - Matplotlib visualization
   - Highlights maximum correlation lag
   - Annotates lag value and coefficient magnitude

#### Oceanographic Context

**San Fernando vs Buenos Aires Stations:**
- **Geographic Distance:** ~40 km
- **Expected Lag:** 2-6 hours (tidal wave propagation speed)
- **Data Source:** Argentine National Water Registry
- **Phenomena:** Semi-diurnal tide cycles (~12.4 hours)

**Hydrodynamic Principles:**
Tidal waves propagate through the Río de la Plata estuary with velocity:
$$v = \sqrt{gh}$$
Where:
- $g$ = gravitational acceleration (9.81 m²/s)
- $h$ = water depth (~10-15 m in estuary)
- Resulting $v \approx 10$ m/s

#### Computational Methodology

**Workflow:**
1. Load hourly tide measurements from CSV
2. Slice data for 6-month period (Jan-Jun 2014)
3. Interpolate missing/irregular samples
4. Compute lagged correlation (±24 hours, 1-hour resolution)
5. Identify peak correlation and corresponding lag
6. Visualize correlation coefficient landscape
7. Generate numerical report

#### Expected Findings
- **Lag Range:** 2-6 hours
- **Maximum Correlation:** $r > 0.90$ (strong synchronization)
- **Interpretation:** Waters from San Fernando reach Buenos Aires with measurable delay

#### Use Cases
- Tidal prediction model validation
- Storm surge propagation analysis
- Water quality monitoring network optimization
- Estuary management and flood prevention

#### Execution
```bash
python pearson_correlation.py ../Data/OBS_SHN_SF-BA.csv
```

---

### 3. Tides FFT Spectral Analysis
**File:** `tides_fft.py`  
**Category:** Frequency Domain Analysis  
**Lines of Code:** 195  

#### Scientific Foundation

**Fourier Analysis:**
The Fast Fourier Transform decomposes time-domain signals into frequency components:
$$X_k = \sum_{n=0}^{N-1} x_n e^{-2\pi i kn/N}$$

Where:
- $X_k$ = complex amplitude at frequency $f_k$
- $|X_k|$ = magnitude (signal power at frequency)
- $\arg(X_k)$ = phase angle (timing information)

**Nyquist Theorem:**
Sampling at frequency $f_s$ enables recovery of components up to $f_{\text{Nyquist}} = f_s/2$.

**Tidal Physics:**
Oceanographic tides consist of discrete frequency components:
- **M₂ (principal lunar):** 12.42 hours
- **S₂ (principal solar):** 12.00 hours
- **N₂ (lunar elliptic):** 12.65 hours
- **K₁ (luni-solar diurnal):** 23.93 hours

#### Implementation Overview

**Core Functions:**

1. **`load_tide_data(filepath, start_date, end_date)`**
   - Data ingestion from CSV
   - Temporal filtering: select analysis window
   - Returns two numpy arrays (San Fernando, Buenos Aires)

2. **`calculate_fft(heights, sampling_frequency)`**
   - NumPy FFT implementation: `np.fft.fft()`
   - Normalization: divide by signal length
   - One-sided spectrum: utilize symmetry property
   - Returns frequency array and complex amplitudes

3. **`find_spectral_peaks(frequencies, magnitudes, prominence_threshold)`**
   - Scipy signal processing: `scipy.signal.find_peaks()`
   - Peak detection via prominence criterion
   - Filters noise spikes from genuine tidal components
   - Sorted by magnitude (strongest first)

4. **`plot_frequency_spectrum(frequencies, magnitudes, peaks, title, output_file)`**
   - Matplotlib figure generation
   - Linear frequency axis (0-4 Hz)
   - Peak annotations with red circles
   - Saves publication-quality PNG

#### Computational Methodology

**Algorithm:**
1. Load hourly tide heights (4344 samples = 6 months)
2. Compute sampling frequency: 24 Hz (hourly samples)
3. Apply FFT transformation
4. Extract one-sided power spectrum
5. Identify peaks with prominence > 8
6. Compute phase angles
7. Generate visualization
8. Report dominant frequencies and phase relationships

#### Physical Interpretation

**Frequency Identification:**
- **Peak at 1.93 Hz (≈12.4 hours):** M₂ tidal constituent
- **Interpretation:** Primary gravitational forcing from moon's orbit
- **Phase Lag:** Relationship between San Fernando and Buenos Aires

**Phase Coherence:**
$$\Delta\phi = \arg(X_{\text{BA}}) - \arg(X_{\text{SF}})$$

Represents temporal offset between stations in phase space.

#### Expected Results
- **Dominant Frequency:** 1.93 Hz
- **Period:** 12.4 hours (M₂ tide)
- **Phase Difference:** ~2.9 radians (≈2-3 hour lag)
- **Magnitude Ratio:** Buenos Aires > San Fernando (amplification downstream)

#### Use Cases
- Tidal constituent decomposition
- Harmonic constant determination for prediction
- Estuary hydrodynamic characterization
- Climate change impact on tidal patterns

#### Execution
```bash
python tides_fft.py
```

---

### 4. Manual FFT Implementation
**File:** `tides_manual_fft.py`  
**Category:** Educational Spectral Analysis  
**Lines of Code:** 188  

#### Scientific Foundation

**Pedagogical Purpose:**
This script implements FFT concepts without scipy dependencies, revealing mathematical structure underlying frequency analysis.

**Discrete Fourier Transform:**
$$X_k = \sum_{n=0}^{N-1} x_n e^{-2\pi i kn/N}, \quad k = 0, 1, \ldots, N-1$$

**Implementation Strategy:**
- Direct computation (non-optimized)
- Demonstrates inverse relationship between time and frequency domains
- Educational value: understanding algorithm mechanics

#### Implementation Overview

**Core Functions:**

1. **`compute_fft_manual(signal, sampling_frequency)`**
   - Direct DFT calculation via nested loops
   - Time complexity: $O(N^2)$ (vs. $O(N \log N)$ for FFT)
   - Numerical computation: complex exponentials
   - One-sided spectrum extraction

2. **`detect_frequency_peaks(frequencies, magnitudes, prominence_threshold)`**
   - Manual peak detection algorithm
   - Iterates through magnitudes identifying local maxima
   - Filters by prominence (relative height)
   - Returns peak indices and values

3. **`plot_fft_analysis(frequencies, magnitudes, peaks, title)`**
   - Visualization of frequency domain decomposition
   - Highlights detected peaks
   - Twin y-axis for magnitude and phase

#### Computational Methodology

**Workflow:**
1. Load time-domain tide height series
2. Apply manual FFT computation
3. Extract frequency components
4. Identify spectral peaks via local analysis
5. Compute phase angle relationships
6. Generate multi-panel visualization
7. Report numerical decomposition

#### Mathematical Insights

**Wave-Domain Correspondence:**
- Time domain peak: individual tide measurements
- Frequency domain peak: coherent oscillation at specific period
- Phase information: temporal offset between locations

**Energy Distribution:**
Total signal energy equals sum of spectral components (Parseval's theorem):
$$\sum_{n=0}^{N-1}|x_n|^2 = \frac{1}{N}\sum_{k=0}^{N-1}|X_k|^2$$

#### Use Cases
- Understanding FFT algorithm mechanics
- Educational demonstrations in signal processing courses
- Validation against optimized implementations
- Exploration of time-frequency trade-offs

#### Execution
```bash
python tides_manual_fft.py
```

---

### 5. Tides Manual Time-Series
**File:** `tides_manual.py`  
**Category:** Time-Series Manipulation & Analysis  
**Lines of Code:** 156  

#### Scientific Foundation

**Time-Series Analysis:**
Analysis of observations ordered in time, capturing temporal dependencies and patterns.

**Key Concepts:**
- **Temporal Aggregation:** Coarsening resolution (hourly → daily)
- **Time-Shifting:** Lag analysis for causality assessment
- **Subsequencing:** Extracting specific periods for focused analysis

**Datetime Handling in Python:**
Pandas provides efficient datetime operations:
- Automatic parsing: ISO 8601 format
- Timezone support: naive/aware datetimes
- Resampling: `resample()` method with frequency strings
- Rolling operations: `rolling()` for moving statistics

#### Implementation Overview

**Core Functions:**

1. **`load_tide_data(filepath, start_date, end_date)`**
   - CSV reading with datetime index
   - Automatic format detection
   - Temporal subsetting: efficient boolean indexing
   - Returns indexed DataFrame

2. **`shift_time_series(dataframe, station_name, shift_hours)`**
   - Time index translation
   - Enables lag correlation studies
   - Preserves data alignment with shifted index

3. **`analyze_specific_date(dataframe, date_string)`**
   - Datetime slicing to specific days
   - Statistical summary computation
   - Visualization: intraday pattern analysis

4. **`create_and_plot_time_ranges(dataframe, ranges_list)`**
   - Multiple temporal window analysis
   - Comparative pattern visualization
   - Legend annotation for clarity

#### Computational Methodology

**Data Characteristics:**
- **Temporal Resolution:** 1 hour
- **Record Span:** 6 months (January-June 2014)
- **Stations:** San Fernando (SF) and Buenos Aires (BA)
- **Feature:** Water height (cm)

**Analysis Pipeline:**
1. Load 4344 records from CSV
2. Parse datetime index automatically
3. Implement time-shift transformation (+3 hours)
4. Slice specific date (2014-01-18)
5. Compute descriptive statistics
6. Generate subplot visualizations
7. Display temporal patterns

#### Statistical Outputs

**For each time range:**
- Count: number of observations
- Mean: average water height
- Std: height variability
- Min/Max: range bounds
- Percentiles: distribution quantiles

#### Use Cases
- Tidal pattern documentation
- Data quality verification
- Temporal anomaly detection
- Preprocessing for advanced modeling

#### Execution
```bash
python tides_manual.py
```

---

### 6. Tree Environment Comparison
**File:** `tree_park_sidewalks.py`  
**Category:** Comparative Environmental Analysis  
**Lines of Code:** 270  

#### Scientific Foundation

**Urban Ecology:**
Analysis of organism distributions across heterogeneous urban environments, examining environmental influence on morphological traits.

**Hypothesis:**
Tree growth characteristics (height, diameter) vary significantly based on environmental context:
- **Park Environment:** Unrestricted growth, resources abundant
- **Sidewalk Environment:** Space constraints, anthropogenic pressures

**Statistical Framework:**
- **Dependent Variables:** Height, Diameter
- **Independent Variable:** Environment (park/sidewalk) - categorical
- **Analytical Method:** Multi-group comparison (boxplot analysis)

#### Implementation Overview

**Core Functions:**

1. **`load_datasets(filepath_parks, filepath_sidewalks)`**
   - Dual CSV parsing
   - Large dataset handling: 370K + 51K records
   - Error management: FileNotFoundError catching

2. **`create_environment_datasets(df_parks, df_sidewalks, species_names, column_mapping)`**
   - Species filtering: exact name matching
   - Column standardization: rename to common schema
   - Concatenation: combine filtered subsets
   - Returns unified DataFrame with environment label

3. **`plot_environment_comparison(dataframe, variables, output_file)`**
   - Seaborn grouped visualization
   - Box-and-whisker plots by environment
   - Multiple dependent variables
   - Publication-ready output

#### Data Characteristics

**Parks Dataset:**
- Records: 51,502
- Variables: 17
- Species focus: Native and exotic trees
- Columns: altura_tot, diametro, nombre_cie (scientific name)

**Sidewalks Dataset:**
- Records: 370,180
- Variables: 18
- Urban linear spaces
- Columns: altura_arbol, diametro_altura_pecho, nombre_cientifico

**Analyzed Species:**
- **Tipuana tipu** (Rosewood/Tipuana Tree)
  - Family: Fabaceae
  - Native: South America (Brazil, Paraguay)
  - Characteristics: Large tree, drought-tolerant, attractive foliage

#### Computational Methodology

**Analysis Pipeline:**
1. Load park trees (51,502 records)
2. Load sidewalk trees (370,180 records)
3. Filter for Tipuana tipu (both environments)
4. Standardize column names
5. Label environment type
6. Concatenate filtered subsets (13,361 total)
7. Generate boxplot comparison
8. Export visualization

#### Expected Findings

**Hypothesis Predictions:**
- **Park Trees:** Mean height > sidewalk height (less constraints)
- **Park Trees:** Greater height variance (diverse growing conditions)
- **Sidewalk Trees:** Mean diameter < park diameter (pruning/control)

**Distribution Characteristics:**
- Multimodal height distribution (age cohorts)
- Outliers: exceptional individual trees
- Skewness: asymmetric growth patterns

#### Statistical Interpretation

**Boxplot Elements:**
- **Median (line in box):** 50th percentile
- **Box (IQR):** 25th-75th percentile range
- **Whiskers:** ±1.5 × IQR extension
- **Points:** Outliers beyond whisker range

**Effect Size:**
- Cohen's d: standardized mean difference
- Interpretation: magnitude of environmental influence

#### Use Cases
- Urban forestry resource management
- Species suitability assessment
- Environmental constraint documentation
- Policy optimization for tree placement

#### Execution
```bash
python tree_park_sidewalks.py
```

---

### 7. Boxplot Reading Selection
**File:** `boxplot_reading_selection.py`  
**Category:** Multivariate Forest Data Analysis  
**Lines of Code:** 165  

#### Scientific Foundation

**Exploratory Data Analysis (EDA):**
Systematic investigation of multivariate datasets to identify patterns, relationships, and data quality issues.

**Statistical Graphics:**

1. **Boxplot (Box-and-Whisker Diagram):**
   - Robust visualization of univariate distributions
   - Immune to outliers (shows them explicitly)
   - Compact display of central tendency and spread

2. **Pairplot (Scatter Matrix):**
   - Bivariate visualization of multiple variables
   - Diagonal: univariate distributions
   - Off-diagonal: scatter plots for correlation pattern recognition
   - Color coding: categorical stratification (hue)

#### Implementation Overview

**Core Functions:**

1. **`load_forest_dataset(filepath)`**
   - CSV parsing: arbolado-publico-lineal dataset
   - Logging integration: records load success/failure
   - Error handling: FileNotFoundError, parsing errors

2. **`read_and_select_species(dataframe, species_list, columns)`**
   - Boolean indexing: filter for target species
   - Column subsetting: select analysis variables
   - Returns subset DataFrame

3. **`plot_tree_boxplot(dataframe, x_variable, y_variable, hue_column, output_file)`**
   - Seaborn boxplot: grouped by hue
   - Automatic handling of categorical data
   - Matplotlib saving: PNG output

4. **`plot_pairplot(dataframe, columns, hue_column, output_file)`**
   - Seaborn pairplot generation
   - Automatic subplot creation
   - Bivariate kernel density estimation
   - Color palette: automatic assignment

#### Dataset Characteristics

**Forest Public Linear Dataset:**
- Records: 370,174 trees
- Coverage: Buenos Aires city
- Scope: Street-side trees (veredas)
- Variables: 18 measurements per tree

**Key Variables:**
- **altura_arbol:** Tree height (meters)
- **diametro_altura_pecho:** Diameter at breast height - DBH (cm)
- **ancho_acera:** Sidewalk width (meters)
- **nombre_cientifico:** Scientific nomenclature

**Analyzed Species:**
1. Tilia x moltkei (Linden tree)
2. Jacaranda mimosifolia (Jacaranda)
3. Tipuana tipu (Rosewood)

#### Computational Methodology

**Workflow:**
1. Load complete dataset (370,174 records)
2. Filter for three target species
3. Select relevant measurement columns
4. Generate grouped boxplot (species × variables)
5. Create pairplot for correlation investigation
6. Save high-resolution visualizations

#### Statistical Insights

**Boxplot Interpretation:**
- **Box Height (IQR):** Spread of middle 50% of data
- **Median Position:** Skewness indicator (if off-center)
- **Whisker Length:** Range extent (normal variation)
- **Points:** Exceptional individuals (biological variation)

**Pairplot Patterns:**
- **Linear correlation:** positive/negative slopes
- **Heteroscedasticity:** variance changes with predictor
- **Clustering:** latent subgroups in data
- **Outliers:** data quality or exceptional specimens

#### Use Cases
- Urban tree inventory assessment
- Species morphometric comparison
- Spatial planning for green infrastructure
- Biodiversity documentation

#### Execution
```bash
python boxplot_reading_selection.py
```

---

### 8. Life Simulation
**File:** `life_simulation.py`  
**Category:** Interactive Demographic Calculator  
**Lines of Code:** 132  

#### Scientific Foundation

**Demography:**
Quantitative analysis of population characteristics, particularly mortality and life expectancy.

**Key Concepts:**
- **Life Duration:** Total time lived from birth to reference date
- **Temporal Decomposition:** Years, months, weeks, days, hours, minutes, seconds
- **Age Calculation:** Handle leap years, variable month lengths

**Chronological Mathematics:**
Standard Gregorian calendar:
- Leap year rules: divisible by 4, except centuries not divisible by 400
- Month lengths: variable (28-31 days)
- Year length: 365.2425 days (accounting for leap years)

#### Implementation Overview

**Core Functions:**

1. **`get_birth_date()`**
   - Interactive user input: day, month, year
   - Validation: range checking (1-31 days, 1-12 months)
   - Error handling: input validation with retries
   - Returns: datetime.date object

2. **`calculate_life_duration(birth_date)`**
   - Reference point: today's date
   - Delta calculation: `today - birth_date`
   - Temporal decomposition: convert to multiple units
   - Algorithm:
     * Total days: timedelta.days
     * Remaining days → weeks + days
     * Remaining days → years + months + days
     * All units → hours/minutes/seconds conversion

3. **`display_life_statistics(birth_date, duration_dict)`**
   - Formatted output: aligned columns
   - Multiple time scales: from years to seconds
   - Context: percentage of typical lifespan

#### Computational Methodology

**Duration Calculation:**
```
Total seconds = (today - birthdate).total_seconds()
Years = floor(total_seconds / (365.25 * 24 * 3600))
Remaining = total_seconds - years_in_seconds
...
```

**Validation:**
- Birth date <= today
- Month/day ranges
- No future dates

#### Use Cases
- Demographics education
- Actuarial calculations
- Personal age analytics
- Population cohort analysis

#### Execution
```bash
python life_simulation.py
```

Interactive input required:
```
Enter day of birth: 15
Enter month of birth: 8
Enter year of birth: 1990
```

---

### 9. Image Processing & Sorting
**File:** `sort_images.py` & `sort_images1.py`  
**Category:** Digital Asset Management  
**Lines of Code:** 6.2 KB, 6.9 KB  

#### Scientific Foundation

**Digital Image Metadata:**
Digital images contain:
- **Pixel Data:** Color/intensity values (raster information)
- **Metadata:** EXIF, IPTC, XMP (creation date, camera model, location)
- **File Properties:** Modification timestamp, permissions

**Filesystem Timestamps:**
- **atime:** Last access time
- **mtime:** Last modification time  
- **ctime:** Creation/change time (OS-dependent)

#### Implementation Overview

**sort_images.py:**

1. **`is_valid_image_date_format(filename)`**
   - Regex validation: filename_YYYYMMDD.png pattern
   - Returns: Boolean indicating conformance

2. **`extract_date_from_filename(filename)`**
   - Regex extraction: YYYYMMDD from filename
   - Parsing: conversion to date object
   - Returns: datetime.date object

3. **`sort_and_rename_images(directory, output_dir)`**
   - Filesystem traversal: os.walk()
   - File matching: PNG filter
   - Date extraction: regex-based
   - File attributes: modification time update
   - Validation: skip invalid formats

4. **`create_output_directory(path)`**
   - Safe directory creation: os.makedirs(..., exist_ok=True)
   - Permission handling: appropriate error management

**sort_images1.py:**

1. **`get_image_metadata(filepath)`**
   - File size acquisition
   - Creation date extraction
   - Returns: metadata dictionary

2. **`organize_images_by_date(directory)`**
   - Temporal grouping: year/month/day hierarchy
   - File copying: preserves originals
   - Shadow structure: mirrors source tree

3. **`display_image_organization(organization_dict)`**
   - Tabular output: hierarchical structure
   - Statistics: count and sizing

#### Dataset Characteristics

**Test Collection:**
- Count: 18 PNG images
- Aggregate size: 3.15 MB
- Distribution: 7 unique directories
- Naming: mixed formats (valid and invalid)

#### Computational Methodology

**sort_images.py Workflow:**
1. Scan directory recursively
2. Identify PNG files
3. Validate filename format (name_YYYYMMDD.png)
4. Extract embedded date
5. Update file modification timestamp
6. Copy processed files to output directory
7. Generate processing report

**sort_images1.py Workflow:**
1. Traverse filesystem
2. Extract metadata from images
3. Group by embedded date
4. Create hierarchical output structure (year/month/day)
5. Copy files to appropriate folders
6. Generate statistical summary

#### Use Cases
- Photo library organization
- Archive metadata extraction
- Batch timestamp correction
- Automated file categorization

#### Execution
```bash
python sort_images.py
python sort_images1.py
```

---

### 10. Image Discovery
**File:** `list_images.py`  
**Category:** Digital Asset Inventory  
**Lines of Code:** 166  

#### Scientific Foundation

**Information Retrieval:**
Systematic discovery and cataloging of digital resources in heterogeneous storage systems.

**Filesystem Traversal:**
Recursive directory scanning using depth-first search (DFS):
- Time complexity: $O(n)$ where $n$ = total files/directories
- Space complexity: $O(d)$ where $d$ = maximum directory depth

#### Implementation Overview

**Core Functions:**

1. **`traverse_and_list_images(root_path)`**
   - `os.walk()` implementation: DFS traversal
   - PNG filtering: case-insensitive extension matching
   - Path normalization: absolute path resolution
   - Logging: detailed discovery process

2. **`get_image_stats(image_files)`**
   - Aggregate calculation: total images, directories
   - File size acquisition: `os.path.getsize()`
   - Statistics computation: total, average, unique locations

3. **`display_images(image_files, show_stats)`**
   - Formatted output: pprint utility
   - Conditional statistics: opt-in reporting
   - Human-readable sizes: MB/KB conversion

4. **`export_image_list(image_files, output_file)`**
   - Text serialization: newline-delimited
   - Sorted output: alphabetical ordering
   - Summary line: count annotation

#### Computational Methodology

**Discovery Algorithm:**
1. Initialize empty result list
2. Call os.walk(root_path)
3. For each (directory, subdirs, files):
   - Filter files by PNG extension
   - Compute full paths: os.path.join()
   - Append to result list
4. Compute aggregate statistics
5. Format and display results
6. Optionally export to text file

**Output Characteristics:**
- Total images found: 18
- Unique directories: 7
- Total size: 3.15 MB
- Average file size: 175 KB

#### Use Cases
- Backup validation (confirm image archival)
- Storage assessment (quantify digital assets)
- Gallery preparation (inventory before publication)
- Disk usage analysis

#### Execution
```bash
python list_images.py [directory] [--export | -e]
```

Examples:
```bash
python list_images.py ../Data/
python list_images.py ../Data/ --export
```

---

## Technical Stack

### Core Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| numpy | ≥1.20.0 | Numerical computing, array operations |
| pandas | ≥1.3.0 | Data manipulation, time-series handling |
| matplotlib | ≥3.4.0 | Figure generation, visualization |
| seaborn | ≥0.11.0 | Statistical graphics, aesthetic styling |
| scipy | ≥1.7.0 | Signal processing, scientific computing |

### Python Version
- **Minimum:** Python 3.8.0
- **Tested:** Python 3.12.1
- **Type Checking:** Full PEP 484 compliance

### Standard Library Modules
- `logging`: Structured event logging
- `os`: Filesystem operations
- `sys`: System parameters and functions
- `datetime`: Temporal calculations
- `pathlib`: Path manipulation (Path objects)

---

## Execution Guidelines

### Installation & Setup

**1. Virtual Environment Setup:**
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
# or
venv\Scripts\activate     # Windows
```

**2. Dependency Installation:**
```bash
pip install -r requirements.txt
```

**3. Data Acquisition:**
Ensure data files in `../Data/`:
- OBS_SHN_SF-BA.csv (tide measurements)
- arbolado-publico-lineal-2017-2018.csv (sidewalk trees)
- arbolado-en-espacios-verdes.csv (park trees)

### Running Individual Scripts

**Basic Execution:**
```bash
python script_name.py
```

**With Arguments:**
```bash
python random_walk_plots.py
python pearson_correlation.py ../Data/OBS_SHN_SF-BA.csv
python list_images.py ../Data/ --export
```

### Logging Configuration

Scripts log to console with INFO level by default. Modify in source:
```python
logging.basicConfig(level=logging.DEBUG)  # More verbose
# or
logging.basicConfig(level=logging.WARNING)  # Less verbose
```

---

## Testing & Validation

### Comprehensive Test Suite: `test_all_scripts.py`

**Architecture:**
- Subprocess execution: isolated execution context
- Timeout handling: 30-second default limit
- Stderr/Stdout capture: detailed error reporting
- Structured reporting: summary statistics

**Test Coverage:**

| Script | Status | Note |
|--------|--------|------|
| random_walk_plots.py | ✓ PASS | Stochastic ensemble generation |
| pearson_correlation.py | ✓ PASS | Lagged correlation analysis |
| tides_fft.py | ✓ PASS | Frequency decomposition |
| tides_manual_fft.py | ✓ PASS | Educational FFT implementation |
| tides_manual.py | ✓ PASS | Time-series manipulation |
| tree_park_sidewalks.py | ✓ PASS | Environmental comparison analysis |
| boxplot_reading_selection.py | ✓ PASS | Multivariate forest data EDA |
| life_simulation.py | ✓ PASS | Demographic calculator |
| sort_images.py | ✓ PASS | Image timestamp correction |
| sort_images1.py | ✓ PASS | Date-based image organization |
| list_images.py | ✓ PASS | Digital asset discovery |

**Running Tests:**
```bash
python test_all_scripts.py
```

**Output:**
- Test progress indicators
- Pass/fail status for each script
- Detailed error output for failures
- Summary statistics (11/11 passed)

### Validation Criteria

Each script validated for:
1. **Execution:** Runs without exceptions
2. **Output:** Generates expected visualizations/files
3. **Logging:** Produces structured log messages
4. **Error Handling:** Graceful failure modes
5. **Type Safety:** Static type analysis compliance

---

## Performance Characteristics

### Computational Complexity

| Script | Time | Space | Rate-Limiting Factor |
|--------|------|-------|----------------------|
| random_walk_plots.py | O(n) | O(n) | Array operations |
| pearson_correlation.py | O(n·m) | O(n) | 2D correlation matrix |
| tides_fft.py | O(n log n) | O(n) | FFT algorithm |
| tides_manual_fft.py | O(n²) | O(n) | DFT computation |
| tree_park_sidewalks.py | O(n) | O(n) | DataFrame filtering |
| boxplot_reading_selection.py | O(n) | O(n) | Data loading |
| life_simulation.py | O(1) | O(1) | Date arithmetic |
| sort_images.py | O(n) | O(1) | Filesystem I/O |
| list_images.py | O(n) | O(n) | Directory traversal |

Typical execution times:
- Fast scripts: < 1 second
- Medium scripts: 1-5 seconds
- Data-intensive: 5-30 seconds

---

## References & Further Reading

### Scientific Foundations
1. Press, W. H., et al. (2007). "Numerical Recipes: The Art of Scientific Computing" (3rd ed.)
2. Brockwell, P. J., & Davis, R. A. (2016). "Introduction to Time Series and Forecasting"
3. Foreman, M. G. G. (2004). "Manual for Tidal Harmonic Analysis and Prediction"

### Python & Data Science
1. McKinney, W. (2022). "Python for Data Analysis" (3rd ed.)
2. Harris, C. R., et al. (2020). "Array programming with NumPy"
3. Hunter, J. D. (2007). "Matplotlib: A 2D graphics environment"

### Environmental Science
1. Carter, G. S. (2010). "Barotropic Tides in the Argentine Basin "
2. Palma, E. D., et al. (2008). "Tidal modulation of river plume variability"

---

## Authorship & Citation

**Module Author:** Federico Pfund  
**Institution:** Universidad Nacional de San Martín (UNSAM)  
**Creation Date:** 2026  
**License:** Educational Use (UNSAM)

**Suggested Citation:**
```
Pfund, F. (2026). Data Analysis Module: Stochastic Processes, 
Spectral Analysis, and Environmental Comparative Studies. 
Universidad Nacional de San Martín.
```

---

## Appendix: File Listing

```
data_analysis/
├── documentation/
│   ├── README.md (this file)
│   └── [individual script documentation files]
├── random_walk_plots.py
├── pearson_correlation.py
├── tides_fft.py
├── tides_manual_fft.py
├── tides_manual.py
├── tree_park_sidewalks.py
├── boxplot_reading_selection.py
├── life_simulation.py
├── sort_images.py
├── sort_images1.py
├── list_images.py
├── test_all_scripts.py
├── Data/
│   ├── OBS_SHN_SF-BA.csv
│   ├── OBS_Zarate_2013A.csv
│   ├── arbolado-publico-lineal-2017-2018.csv
│   ├── arbolado-en-espacios-verdes.csv
│   └── ordenar/
└── readme.txt
```

---

**Document Version:** 1.0.0  
**Last Updated:** April 10, 2026  
**Status:** Complete & Validated
