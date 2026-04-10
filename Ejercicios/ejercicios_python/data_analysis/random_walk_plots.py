"""Random walk analysis and visualization.

Simulates and analyzes random walk processes with smoothing and 
multi-person comparisons using pandas Series and DataFrames.
"""

import logging
from typing import Tuple, List

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def create_single_random_walk(
    periods: int,
    frequency: str = 'min',
    start_date: str = '20200923 14:00'
) -> pd.Series:
    """Create a single random walk series.
    
    Args:
        periods: Number of time periods.
        frequency: Time frequency ('min', 'H', 'D', etc.).
        start_date: Starting date for the index.
    
    Returns:
        Series containing the cumulative random walk.
    """
    idx = pd.date_range(start_date, periods=periods, freq=frequency)
    steps = pd.Series(np.random.randint(-1, 2, periods), index=idx)
    walk = steps.cumsum()
    logger.info(f"Created random walk with {periods} periods")
    return walk


def smooth_walk(series: pd.Series, window: int) -> pd.Series:
    """Apply moving average smoothing to a random walk.
    
    Args:
        series: Input Series with random walk data.
        window: Window size for moving average.
    
    Returns:
        Smoothed Series.
    """
    smoothed = series.rolling(window).mean()
    logger.info(f"Applied smoothing with window size {window}")
    return smoothed


def combine_walks(series1: pd.Series, series2: pd.Series) -> pd.DataFrame:
    """Combine two walks into a single DataFrame.
    
    Args:
        series1: First random walk Series.
        series2: Second random walk Series.
    
    Returns:
        DataFrame with both series.
    """
    df = pd.DataFrame([series1, series2]).T
    logger.info("Combined walks into DataFrame")
    return df


def create_multiple_people_walks(
    num_people: int,
    periods: int,
    people_names: List[str] = None
) -> pd.DataFrame:
    """Create random walks for multiple people.
    
    Args:
        num_people: Number of people walking.
        periods: Time periods for each walk.
        people_names: List of names for the people (optional).
    
    Returns:
        DataFrame with walks for each person.
    """
    if people_names is None or len(people_names) != num_people:
        people_names = [f'Person_{i+1}' for i in range(num_people)]
    
    idx = pd.date_range('20200923 14:00', periods=periods, freq='min')
    steps = np.random.randint(-1, 2, [periods, num_people])
    walks = pd.DataFrame(steps.cumsum(axis=0), index=idx, columns=people_names)
    
    logger.info(f"Created random walks for {num_people} people")
    return walks


def smooth_multiple_walks(
    df: pd.DataFrame,
    window: int,
    min_periods: int = 1
) -> pd.DataFrame:
    """Apply smoothing to multiple walks.
    
    Args:
        df: DataFrame with multiple walks.
        window: Window size for moving average.
        min_periods: Minimum non-null observations in window.
    
    Returns:
        Smoothed DataFrame.
    """
    smoothed = df.rolling(window, min_periods=min_periods).mean()
    
    # Rename columns to indicate smoothing
    smoothed.columns = [f'Smoothed_{col}' for col in df.columns]
    
    logger.info(f"Smoothed {len(df.columns)} walks with window {window}")
    return smoothed


def plot_walk(
    series: pd.Series,
    title: str = "Random Walk",
    output_file: str = None
) -> None:
    """Plot a single random walk.
    
    Args:
        series: Random walk Series to plot.
        title: Title for the plot.
        output_file: Optional file path to save the plot.
    """
    plt.figure(figsize=(12, 6))
    series.plot()
    plt.title(title)
    plt.xlabel('Time')
    plt.ylabel('Position')
    plt.grid(True, alpha=0.3)
    
    if output_file:
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        logger.info(f"Plot saved to {output_file}")
    plt.show()


def plot_walks(
    df: pd.DataFrame,
    title: str = "Random Walks",
    output_file: str = None
) -> None:
    """Plot multiple random walks.
    
    Args:
        df: DataFrame with multiple walks.
        title: Title for the plot.
        output_file: Optional file path to save the plot.
    """
    plt.figure(figsize=(14, 8))
    df.plot(figsize=(14, 8))
    plt.title(title)
    plt.xlabel('Time')
    plt.ylabel('Position')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True, alpha=0.3)
    
    if output_file:
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        logger.info(f"Plot saved to {output_file}")
    plt.show()


def export_walks(
    df: pd.DataFrame,
    filename: str = 'random_walks_export.csv'
) -> None:
    """Export walks to CSV file.
    
    Args:
        df: DataFrame with walks.
        filename: Output CSV filename.
    """
    df.to_csv(filename)
    logger.info(f"Walks exported to {filename}")


def main() -> None:
    """Main pipeline for random walk analysis."""
    try:
        logger.info("Starting random walk analysis")
        
        # Single walk example
        logger.info("\n--- Single Random Walk ---")
        walk1 = create_single_random_walk(periods=120)
        plot_walk(walk1, title="Single Random Walk (120 steps)")
        
        # Smoothed walk
        logger.info("\n--- Smoothed Walk ---")
        smoothed = smooth_walk(walk1, window=5)
        combined = combine_walks(walk1, smoothed)
        plot_walks(
            combined,
            title="Original Walk vs Smoothed Walk",
            output_file='single_walk_comparison.png'
        )
        
        # Multiple people walks (8 hours = 480 minutes)
        logger.info("\n--- Multiple People Walks ---")
        apostle_names = [
            'Pedro', 'Santiago', 'Juan', 'Andrés', 'Bartolomé',
            'Tiago', 'Isca', 'Tadeo', 'Mateo', 'Felipe', 'Simón', 'Tomás'
        ]
        df_walks = create_multiple_people_walks(
            num_people=12,
            periods=8 * 60,
            people_names=apostle_names
        )
        plot_walks(df_walks, title="12 People Random Walk (8 hours)")
        
        # Smooth multiple walks
        logger.info("\n--- Smoothed Multiple Walks ---")
        df_smoothed = smooth_multiple_walks(df_walks, window=45, min_periods=1)
        
        # Combine original and smoothed
        df_combined = pd.concat([df_walks, df_smoothed], axis=1)
        plot_walks(
            df_combined,
            title="Original vs Smoothed Walks (12 people, 8 hours)",
            output_file='multiple_walks_comparison.png'
        )
        
        # Export results
        export_walks(df_walks, 'apostolic_walk_raw.csv')
        export_walks(df_smoothed, 'apostolic_walk_smoothed.csv')
        
        logger.info("Random walk analysis completed successfully")
        
    except Exception as e:
        logger.error(f"Error in random walk analysis: {e}")
        raise


if __name__ == '__main__':
    main()
