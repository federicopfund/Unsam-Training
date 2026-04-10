"""Tree analysis with boxplots and pairplots for forest datasets.

Performs data reading, filtering, and visualization of tree species
measurements from public forestry datasets.
"""

import logging
import sys
import os
from typing import List, Tuple

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def read_and_select_species(
    dataframe: pd.DataFrame,
    columns: List[str],
    target_column: str = 'nombre_cientifico',
    species_list: List[str] = None
) -> pd.DataFrame:
    """Read data and select specific tree species.
    
    Args:
        dataframe: Input DataFrame with tree data.
        columns: Columns to include in output.
        target_column: Column containing species names.
        species_list: List of species to filter (None for all).
    
    Returns:
        Filtered DataFrame with selected species.
    """
    df_selected = dataframe[columns].copy()
    
    if species_list:
        df_selected = df_selected[
            df_selected[target_column].isin(species_list)
        ]
        logger.info(f"Selected {len(species_list)} species: {species_list}")
    
    logger.info(f"DataFrame shape after selection: {df_selected.shape}")
    print(df_selected)
    
    return df_selected


def plot_tree_boxplot(
    dataframe: pd.DataFrame,
    measurement_col: str,
    species_col: str = 'nombre_cientifico',
    output_file: str = None
) -> None:
    """Plot boxplot for tree measurements by species.
    
    Args:
        dataframe: DataFrame with tree data.
        measurement_col: Column to plot (e.g., 'altura_arbol').
        species_col: Column with species names.
        output_file: Optional file path to save the plot.
    """
    plt.figure(figsize=(12, 6))
    dataframe.boxplot(measurement_col, by=species_col)
    plt.suptitle(f'{measurement_col} Distribution by Species')
    plt.xlabel('Species')
    plt.ylabel(measurement_col.replace('_', ' ').title())
    
    if output_file:
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        logger.info(f"Boxplot saved to {output_file}")
    plt.show()


def plot_pairplot(
    dataframe: pd.DataFrame,
    columns: List[str],
    hue_column: str = 'nombre_cientifico',
    output_file: str = None
) -> None:
    """Create pairplot for multiple measurements by species.
    
    Args:
        dataframe: DataFrame with tree data.
        columns: Columns to include in pairplot.
        hue_column: Column to use for color coding.
        output_file: Optional file path to save the plot.
    """
    selected_data = dataframe[columns].copy()
    pairs = sns.pairplot(data=selected_data, hue=hue_column)
    
    if output_file:
        pairs.savefig(output_file, dpi=300, bbox_inches='tight')
        logger.info(f"Pairplot saved to {output_file}")
    plt.show()


def load_forest_dataset(filepath: str) -> pd.DataFrame:
    """Load forest dataset from CSV file.
    
    Args:
        filepath: Path to the CSV file.
    
    Returns:
        DataFrame with forest data.
    """
    try:
        df = pd.read_csv(filepath)
        logger.info(f"Loaded dataset: {filepath} (shape: {df.shape})")
        return df
    except FileNotFoundError:
        logger.error(f"File not found: {filepath}")
        raise
    except Exception as e:
        logger.error(f"Error loading dataset: {e}")
        raise


def main(
    filename: str = 'arbolado-publico-lineal-2017-2018.csv',
    data_dir: str = '../Data/'
) -> None:
    """Main analysis pipeline for tree data.
    
    Args:
        filename: Name of the CSV file to load.
        data_dir: Directory containing the data.
    """
    try:
        logger.info("Starting tree analysis pipeline")
        
        # Load data
        filepath = os.path.join(data_dir, filename)
        df = load_forest_dataset(filepath)
        
        # Define columns to analyze
        columns_of_interest = [
            'nombre_cientifico',
            'ancho_acera',
            'diametro_altura_pecho',
            'altura_arbol'
        ]
        
        # Select specific species
        target_species = [
            'Tilia x moltkei',
            'Jacaranda mimosifolia',
            'Tipuana tipu'
        ]
        
        # Process data
        df_selected = read_and_select_species(
            df,
            columns=columns_of_interest,
            target_column='nombre_cientifico',
            species_list=target_species
        )
        
        # Create visualizations
        logger.info("Creating boxplots...")
        plot_tree_boxplot(
            df_selected,
            measurement_col='altura_arbol',
            output_file='tree_height_boxplot.png'
        )
        
        logger.info("Creating pairplot...")
        plot_pairplot(
            df_selected,
            columns=columns_of_interest,
            output_file='tree_measurements_pairplot.png'
        )
        
        logger.info("Tree analysis completed successfully")
        
    except Exception as e:
        logger.error(f"Error in analysis: {e}")
        raise


if __name__ == '__main__':
    try:
        filename = sys.argv[1] if len(sys.argv) > 1 else 'arbolado-publico-lineal-2017-2018.csv'
        main(filename=filename)
    except Exception as e:
        logger.error(f"Failed to execute main: {e}")
        sys.exit(1)