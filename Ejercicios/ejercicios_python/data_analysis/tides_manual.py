"""Tide data analysis with time series manipulation and visualization.

Performs reading, manipulation, and visualization of tide measurements
from multiple monitoring stations.
"""

import logging
import sys
import os
from typing import Tuple

import pandas as pd
import matplotlib.pyplot as plt

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def load_tide_data(filepath: str) -> pd.DataFrame:
    """Load tide data from CSV file.
    
    Args:
        filepath: Path to the CSV file.
    
    Returns:
        DataFrame with tide data indexed by time.
    """
    try:
        df = pd.read_csv(filepath, index_col=['Time'], parse_dates=True)
        logger.info(f"Loaded tide data from {filepath}")
        return df
    except FileNotFoundError:
        logger.error(f"File not found: {filepath}")
        raise
    except Exception as e:
        logger.error(f"Error loading data: {e}")
        raise


def shift_time_series(
    df: pd.DataFrame,
    col1: str,
    col2: str,
    time_shift: int,
    height_offset: float,
    start_date: str = '12-25-2014'
) -> None:
    """Shift one time series by a specified lag.
    
    Args:
        df: DataFrame with tide data.
        col1: Column to shift.
        col2: Column to compare with.
        time_shift: Time lag for shifting.
        height_offset: Height offset between measurements.
        start_date: Date to start analysis.
    """
    df_subset = df[start_date:].copy()
    
    shifted_col = df_subset[col1].shift(time_shift) - height_offset
    
    # Create comparison DataFrame
    df_comparison = pd.DataFrame({
        col1: shifted_col,
        col2: df_subset[col2]
    })
    
    logger.info(f"Applied time shift of {time_shift} and height offset of {height_offset}")
    df_comparison.plot(figsize=(14, 6))
    plt.title(f'Tide Comparison: {col1} (shifted) vs {col2}')
    plt.xlabel('Date')
    plt.ylabel('Height (m)')
    plt.grid(True, alpha=0.3)
    plt.show()


def create_and_plot_time_ranges(
    df: pd.DataFrame,
    time_ranges: list,
    col_name: str = None
) -> None:
    """Plot multiple time ranges of tide data.
    
    Args:
        df: DataFrame with tide data.
        time_ranges: List of tuples with date ranges.
        col_name: Specific column to plot (if None, plot all).
    """
    fig, axes = plt.subplots(len(time_ranges), 1, figsize=(14, 4*len(time_ranges)))
    
    if len(time_ranges) == 1:
        axes = [axes]
    
    for idx, (start_date, end_date) in enumerate(time_ranges):
        df_range = df[start_date:end_date]
        
        if col_name:
            df_range[col_name].plot(ax=axes[idx])
            axes[idx].set_title(f'{col_name} from {start_date} to {end_date}')
        else:
            df_range.plot(ax=axes[idx])
            axes[idx].set_title(f'Tide Data from {start_date} to {end_date}')
        
        axes[idx].set_ylabel('Height (m)')
        axes[idx].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    logger.info(f"Plotted {len(time_ranges)} time ranges")


def analyze_specific_date(df: pd.DataFrame, start_date: str, end_date: str) -> None:
    """Analyze and display data for a specific date range.
    
    Args:
        df: DataFrame with tide data.
        start_date: Start date for analysis.
        end_date: End date for analysis.
    """
    df_subset = df[start_date:end_date]
    logger.info(f"Data from {start_date} to {end_date}")
    print(df_subset)
    print(f"\nStatistics:\n{df_subset.describe()}")


def main(data_file: str = '../Data/OBS_SHN_SF-BA.csv') -> None:
    """Main analysis pipeline.
    
    Args:
        data_file: Path to the tide data CSV file.
    """
    try:
        logger.info("Starting tide data analysis")
        
        # Load data
        df = load_tide_data(data_file)
        logger.info(f"Data shape: {df.shape}")
        logger.info(f"Columns: {list(df.columns)}")
        
        # Analyze specific date
        logger.info("\n--- Analysis for 1-18-2014 ---")
        analyze_specific_date(df, '1-18-2014 9:00', '1-18-2014 18:00')
        
        # Plot multiple time ranges
        logger.info("\n--- Plotting Time Ranges ---")
        time_ranges = [
            ('10-15-2014', '12-15-2014'),  # Tides in RdlP
            ('12-25-2014', '12-31-2014')   # Storm waves
        ]
        
        create_and_plot_time_ranges(df, time_ranges)
        
        # Shift analysis
        logger.info("\n--- Time Shift Analysis ---")
        shift_time_series(
            df,
            col1='H_SF',
            col2='H_BA',
            time_shift=2,
            height_offset=3,
            start_date='12-25-2014'
        )
        
        logger.info("Tide analysis completed successfully")
        
    except Exception as e:
        logger.error(f"Error in analysis: {e}")
        raise


if __name__ == '__main__':
    data_file = sys.argv[1] if len(sys.argv) > 1 else '../Data/OBS_SHN_SF-BA.csv'
    try:
        main(data_file)
    except Exception as e:
        logger.error(f"Failed to execute main: {e}")
        sys.exit(1)
