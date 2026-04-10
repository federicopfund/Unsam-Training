"""Pearson correlation analysis for tide data.

Analyzes correlation between two tide measuring stations (San Fernando and Buenos Aires)
with various time shifts to find the optimal lag between measurements.
"""

import logging
import sys
from pathlib import Path
from typing import Tuple

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def load_tide_data(filepath: str, start_date: str = None) -> pd.DataFrame:
    """Load tide data from CSV file.
    
    Args:
        filepath: Path to the CSV file containing tide data.
        start_date: Optional start date for data filtering (format: MM-DD-YYYY).
    
    Returns:
        DataFrame with tide data indexed by time.
    """
    try:
        df = pd.read_csv(filepath, index_col=['Time'], parse_dates=True)
        if start_date:
            df = df[start_date:].copy()
        logger.info(f"Loaded tide data from {filepath}")
        return df
    except FileNotFoundError:
        logger.error(f"File not found: {filepath}")
        raise
    except Exception as e:
        logger.error(f"Error loading data: {e}")
        raise


def calculate_lagrange_correlation(
    df: pd.DataFrame,
    col1: str,
    col2: str,
    shift_range: Tuple[int, int] = (-12, 13)
) -> Tuple[np.ndarray, np.ndarray]:
    """Calculate Pearson correlation for various time shifts.
    
    Args:
        df: DataFrame with tide data.
        col1: First column name to correlate.
        col2: Second column name to correlate.
        shift_range: Tuple (min_shift, max_shift) for time lags.
    
    Returns:
        Tuple of (shifts array, correlations array).
    """
    shifts = np.arange(*shift_range)
    correlations = np.zeros(shifts.shape)
    
    margin = abs(shift_range[0])
    for i, shift in enumerate(shifts):
        shifted_col1 = df[col1].shift(shift)[margin:-margin]
        col2_data = df[col2][margin:-margin]
        correlations[i] = pearsonr(shifted_col1, col2_data)[0]
    
    logger.info(f"Calculated correlations for {len(shifts)} shifts")
    return shifts, correlations


def plot_correlation_results(
    shifts: np.ndarray,
    correlations: np.ndarray,
    title: str = "Tide Station Correlation vs Time Shift",
    output_file: str = None
) -> None:
    """Plot correlation results.
    
    Args:
        shifts: Array of time shifts.
        correlations: Array of correlation coefficients.
        title: Title for the plot.
        output_file: Optional file path to save the plot.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(shifts, correlations, marker='o', linestyle='-')
    plt.xlabel('Time Shift (hours)')
    plt.ylabel('Pearson Correlation Coefficient')
    plt.title(title)
    plt.grid(True, alpha=0.3)
    
    if output_file:
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        logger.info(f"Plot saved to {output_file}")
    plt.show()


def interpolate_and_correlate(
    df: pd.DataFrame,
    col1: str,
    col2: str,
    frequency_hours: int = 2,
    hours_window: int = 24
) -> Tuple[np.ndarray, np.ndarray]:
    """Interpolate tide data and calculate correlations at finer resolution.
    
    Args:
        df: DataFrame with tide data.
        col1: First column name.
        col2: Second column name.
        frequency_hours: Sampling frequency (2 = every 30 min, 4 = every 15 min).
        hours_window: Analysis window in hours.
    
    Returns:
        Tuple of (shifts in hours, correlations array).
    """
    # Resample at specified frequency
    resampled_df = df.resample(f'{int(60/frequency_hours)}min').mean()
    # Interpolate missing values
    interpolated_df = resampled_df.interpolate(method='quadratic')
    
    n_samples = hours_window * frequency_hours
    integer_shifts = np.arange(-n_samples, n_samples + 1)
    shifts_hours = integer_shifts / frequency_hours
    
    correlations = np.zeros(len(integer_shifts))
    for i, shift in enumerate(integer_shifts):
        col1_data = interpolated_df[col1].shift(shift)[n_samples:-n_samples]
        col2_data = interpolated_df[col2][n_samples:-n_samples]
        correlations[i] = pearsonr(col1_data, col2_data)[0]
    
    logger.info(f"Interpolated data and calculated {len(correlations)} correlations")
    return shifts_hours, correlations


def main(data_file: str = '../Data/OBS_SHN_SF-BA.csv') -> None:
    """Main analysis pipeline.
    
    Args:
        data_file: Path to the tide data CSV file.
    """
    try:
        logger.info("Starting tide correlation analysis")
        
        # Load basic tide data (hourly)
        df = load_tide_data(data_file, start_date='10-01-2014')
        shifts, correlations = calculate_lagrange_correlation(
            df, 'H_SF', 'H_BA', shift_range=(-12, 13)
        )
        plot_correlation_results(
            shifts, correlations,
            title="Hourly Tide Correlation: San Fernando vs Buenos Aires"
        )
        
        # Load and interpolate data for finer resolution
        logger.info("\nPerforming analysis with interpolated data...")
        shifts_interp, correlations_interp = interpolate_and_correlate(
            df, 'H_SF', 'H_BA', frequency_hours=2, hours_window=24
        )
        plot_correlation_results(
            shifts_interp, correlations_interp,
            title="Interpolated Tide Correlation (30-min intervals)"
        )
        
        # Find optimal shift
        optimal_shift_idx = np.argmax(np.abs(correlations_interp))
        optimal_shift = shifts_interp[optimal_shift_idx]
        optimal_corr = correlations_interp[optimal_shift_idx]
        
        logger.info(
            f"\nOptimal time shift: {optimal_shift:.2f} hours"
            f" (correlation: {optimal_corr:.4f})"
        )
        
    except Exception as e:
        logger.error(f"Error in analysis: {e}")
        raise


if __name__ == '__main__':
    data_file = sys.argv[1] if len(sys.argv) > 1 else '../Data/OBS_SHN_SF-BA.csv'
    main(data_file)
