# Quick Start Guide: Data Analysis Module

**Objective:** Get started with the data analysis module in 5 minutes  
**Difficulty:** Beginner-friendly  

---

## 🚀 Installation (2 minutes)

### 1. Verify Python Installation
```bash
python --version
# Should show Python 3.8+ (tested with 3.12.1)
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

Or manually:
```bash
pip install numpy pandas matplotlib seaborn scipy
```

### 3. Verify Installation
```bash
python -c "import numpy, pandas, matplotlib, scipy; print('✓ All packages installed')"
```

---

## 📚 Where to Start

### Option A: Just Want to Run Scripts?
```bash
# Test everything works
python test_all_scripts.py

# Run a specific analysis
python random_walk_plots.py
python list_images.py ../Data/
```

### Option B: Want to Understand What's Happening?

**5-minute overview:**
1. Read [EXECUTIVE_SUMMARY.md](EXECUTIVE_SUMMARY.md) (this explains what module does)
2. Run: `python random_walk_plots.py` (simplest script)
3. Look at generated image files
4. Read [quick reference](#quick-reference-all-11-scripts) below

### Option C: Need Complete Understanding?

**Start with documentation:**
1. Read [INDEX.md](INDEX.md) (navigation guide)
2. Choose your topic:
   - Probability → [STOCHASTIC_PROCESSES.md](STOCHASTIC_PROCESSES.md)
   - Time-series → [TIMESERIES_SPECTRAL.md](TIMESERIES_SPECTRAL.md)
   - Nature/Environment → [ENVIRONMENTAL_ANALYSIS.md](ENVIRONMENTAL_ANALYSIS.md)
   - Files/Images → [DEMOGRAPHICS_ASSET_MANAGEMENT.md](DEMOGRAPHICS_ASSET_MANAGEMENT.md)
3. Read recommended document
4. Run associated scripts

---

## Quick Reference: All 11 Scripts

### Group 1: Probability & Stochastic Processes

**random_walk_plots.py** - Simulate random wandering agents
```bash
python random_walk_plots.py

# Outputs images showing trajectory patterns
# Time: ~1 second
# No arguments needed
```

### Group 2: Oceanographic Time-Series Analysis

**pearson_correlation.py** - How connected are two tidal stations?
```bash
python pearson_correlation.py ../Data/OBS_SHN_SF-BA.csv

# Finds time lag between measurements
# Time: ~1 second
```

**tides_manual.py** - Explore tide patterns interactively
```bash
python tides_manual.py

# Show water heights on specific dates
# Time: <1 second
# No arguments needed
```

**tides_fft.py** - What frequencies appear in tide data?
```bash
python tides_fft.py

# Reveals dominant tidal cycles
# Time: ~1 second
# Outputs frequency spectrum images
```

**tides_manual_fft.py** - Educational FFT (slow but transparent)
```bash
python tides_manual_fft.py

# Shows HOW FFT algorithm works
# Time: ~2 seconds
# No arguments needed
```

### Group 3: Environmental Tree Analysis

**tree_park_sidewalks.py** - How does environment affect tree growth?
```bash
python tree_park_sidewalks.py

# Compares trees in parks vs city sidewalks
# Time: ~5 seconds
# No arguments needed
```

**boxplot_reading_selection.py** - Tree species comparison
```bash
python boxplot_reading_selection.py

# Shows how three species differ
# Time: ~3 seconds
# No arguments needed
```

### Group 4: Demographics & Files

**life_simulation.py** - Calculate how long you've lived
```bash
python life_simulation.py

# Interactive - enter birthdate when prompted
# Time: <1 second
```

**list_images.py** - Find all PNG images in a folder
```bash
python list_images.py ../Data/
# or with export:
python list_images.py ../Data/ --export

# Shows image inventory and statistics
# Time: ~1 second
```

**sort_images.py** - Fix image file timestamps
```bash
python sort_images.py

# Updates file dates based on filename
# Time: ~1 second
# No arguments needed
```

**sort_images1.py** - Organize images by date
```bash
python sort_images1.py

# Creates year/month/day folder structure
# Time: ~1 second
# No arguments needed
```

---

## What Do the Scripts Need?

### Data Files
Some scripts need data files in `../Data/`:
- `OBS_SHN_SF-BA.csv` (tide measurements)
- `arbolado-publico-lineal-2017-2018.csv` (tree data)
- `arbolado-en-espacios-verdes.csv` (tree data)

**Don't have them?** Most scripts work without them or have fallbacks.

### Image Files
Image scripts expect images in `../Data/`:
- PNG format files
- Can be anywhere in subfolders
- Format: `name_YYYYMMDD.png` (optional)

---

## Common Tasks in 30 Seconds

### "Run all tests and confirm everything works"
```bash
python test_all_scripts.py
# Shows ✓ PASS for each script
```

### "Generate random walk visualization"
```bash
python random_walk_plots.py
# Creates 2 PNG image files
```

### "Find all PNG images"
```bash
python list_images.py ../Data/
# Shows list and statistics
```

### "Interactive age calculator"
```bash
python life_simulation.py
# Enter your birthday when prompted
```

### "Analyze tide correlation"
```bash
python pearson_correlation.py ../Data/OBS_SHN_SF-BA.csv
# Creates visualization showing time lag
```

---

## Output Files

Different scripts create different outputs:

| Script | Creates | Example |
|--------|---------|---------|
| random_walk_plots.py | PNG images | single_walk_comparison.png |
| pearson_correlation.py | PNG image | correlation_plot.png |
| tides_fft.py | 2× PNG images | fft_san_fernando.png |
| tree_park_sidewalks.py | PNG image | tree_environment_comparison.png |
| list_images.py | Text file (optional) | image_list.txt |

**Where do they go?**
- Same directory as the script (data_analysis/)
- Check `documentation/` subfolder for README.md files

---

## Troubleshooting

### Problem: "ModuleNotFoundError: No module named 'pandas'"
**Solution:** Install dependencies
```bash
pip install -r requirements.txt
```

### Problem: "FileNotFoundError: OBS_SHN_SF-BA.csv not found"
**Solution:** Check file location or use different path
```bash
# Check if file exists:
ls ../Data/OBS_SHN_SF-BA.csv

# Or specify full path:
python pearson_correlation.py /full/path/to/file.csv
```

### Problem: "No PNG images found"
**Solution:** Images might not be in the expected location
```bash
# Check subfolders too:
python list_images.py ../Data/
```

### Problem: Script runs but creates no output
**Solution:** Check current directory
```bash
# Go to script directory:
cd /workspaces/Unsam-Training/Ejercicios/ejercicios_python/data_analysis

# Then run:
python script_name.py

# Check what was created:
ls -la *.png *.csv *.txt
```

---

## Getting Help

### Within 2 Minutes
- Check this file (you're reading it!)
- Run: `python script_name.py --help` (some scripts support this)

### Within 5 Minutes
- Read [EXECUTIVE_SUMMARY.md](EXECUTIVE_SUMMARY.md) - explains what each module does
- Check the specific script documentation:
  - [STOCHASTIC_PROCESSES.md](STOCHASTIC_PROCESSES.md) →  random walks
  - [TIMESERIES_SPECTRAL.md](TIMESERIES_SPECTRAL.md) → tides
  - [ENVIRONMENTAL_ANALYSIS.md](ENVIRONMENTAL_ANALYSIS.md) → trees
  - [DEMOGRAPHICS_ASSET_MANAGEMENT.md](DEMOGRAPHICS_ASSET_MANAGEMENT.md) → images/dates

### Within 10 Minutes
- Read [INDEX.md](INDEX.md) - navigation hub with quick tables
- Check [README.md](README.md) - 500+ lines of detailed explanation

### Detailed Understanding
- Read the specific technical document
- Look at code comments in source file
- Check error messages and logging output

---

## Next Steps After Getting Started

### Level 1: Run Some Scripts (Now!)
```bash
python random_walk_plots.py
python list_images.py ../Data/
python life_simulation.py
```

### Level 2: Understand One Topic (5-10 min)
Pick one and read its documentation:
- Probability: [STOCHASTIC_PROCESSES.md](STOCHASTIC_PROCESSES.md)
- Time-Series: [TIMESERIES_SPECTRAL.md](TIMESERIES_SPECTRAL.md)
- Environment: [ENVIRONMENTAL_ANALYSIS.md](ENVIRONMENTAL_ANALYSIS.md)
- Files: [DEMOGRAPHICS_ASSET_MANAGEMENT.md](DEMOGRAPHICS_ASSET_MANAGEMENT.md)

### Level 3: Deep Dive (20-30 min)
Read [README.md](README.md) - comprehensive guide with:
- All 11 scripts explained
- Mathematical foundations
- Code examples
- Architecture details

### Level 4: Customize & Extend (1+ hour)
- Modify scripts for your own data
- Add new analysis functions
- Create new visualizations
- Integrate into your workflow

---

## Key Concepts to Know

### These 5 scripts are "independent" (work alone)
1. random_walk_plots.py
2. life_simulation.py
3. list_images.py
4. sort_images.py
5. sort_images1.py

### These 4 work best together (same data)
1. pearson_correlation.py
2. tides_manual.py
3. tides_fft.py
4. tides_manual_fft.py

### These 2 are complementary tools
1. tree_park_sidewalks.py (comparison)
2. boxplot_reading_selection.py (explore multiple species)

---

## One-Liner Commands

```bash
# Test all scripts
python test_all_scripts.py

# Run all image analysis
python list_images.py ../Data/ --export && python sort_images.py && python sort_images1.py

# Run all tidal analysis
python tides_manual.py && python pearson_correlation.py ../Data/OBS_SHN_SF-BA.csv && python tides_fft.py && python tides_manual_fft.py

# Run all tree analysis
python tree_park_sidewalks.py && python boxplot_reading_selection.py
```

---

## System Requirements

**Minimum:**
- Python 3.8+
- 50 MB free disk space
- 512 MB RAM

**Tested With:**
- Python 3.12.1
- 1 GB RAM
- Ubuntu 24.04.3 LTS

---

## Performance Expectations

| Script | Time | Why |
|--------|------|-----|
| list_images.py | <1 sec | Fast disk scan |
| random_walk_plots.py | 1-2 sec | 12 trajectories |
| life_simulation.py | <1 sec | Simple math |
| pearson_correlation.py | 1 sec | Interpolation |
| boxplot_reading_selection.py | 3 sec | Loads 370K rows |
| tree_park_sidewalks.py | 5 sec | Filters 420K rows |
| tides_fft.py | 1-2 sec | FFT algorithm |
| tides_manual_fft.py | 2 sec | O(n²) algorithm |

**Total test_all_scripts.py:** ~17 seconds

---

## Common Questions

**Q: Can I modify the scripts?**  
A: Yes! They're educational. Make backups first.

**Q: What if I don't have the data files?**  
A: Most scripts have fallback behavior or will show helpful errors.

**Q: Can I use these in my project?**  
A: Yes, with proper attribution. Licensed for educational use.

**Q: How do I use custom data?**  
A: Modify the file path parameter or update the default path in the script.

**Q: Can I run scripts in parallel?**  
A: Yes, test_all_scripts.py does this safely.

**Q: What Python version do I need?**  
A: 3.8+. Tested with 3.12.1.

---

## Documentation Map

```
📚 documentation/
   ├─ THIS FILE (Start here!)
   │
   ├─ EXECUTIVE_SUMMARY.md
   │  └─ For managers/overview
   │
   ├─ INDEX.md
   │  └─ Navigation hub (all documents listed)
   │
   ├─ README.md
   │  └─ Comprehensive master guide (500+ lines)
   │
   ├─ STOCHASTIC_PROCESSES.md
   │  └─ Random walks & probability
   │
   ├─ TIMESERIES_SPECTRAL.md
   │  └─ Tides, correlation, FFT
   │
   ├─ ENVIRONMENTAL_ANALYSIS.md
   │  └─ Trees in parks vs sidewalks
   │
   └─ DEMOGRAPHICS_ASSET_MANAGEMENT.md
      └─ Life simulation, image management
```

---

**Ready to start? Run this:**
```bash
python test_all_scripts.py
```

If you see "✓ PASS" for all scripts, you're good to go! 🎉

---

**Quick Links:**
- [INDEX.md](INDEX.md) - Full navigation
- [README.md](README.md) - Complete reference
- [EXECUTIVE_SUMMARY.md](EXECUTIVE_SUMMARY.md) - High-level overview

**Questions?** See relevant technical document above.  
**Version:** 1.0.0  
**Updated:** April 10, 2026
