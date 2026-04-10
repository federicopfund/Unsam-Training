"""Comparative analysis of tree species in parks vs sidewalks.

Analyzes tree measurements in different environments (parks and sidewalks)
for comparison of species characteristics.
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


def create_environment_datasets(
    df_parks: pd.DataFrame,
    df_sidewalks: pd.DataFrame,
    species_names: Tuple[str, str],
    column_mapping: Tuple[str, ...]
) -> pd.DataFrame:
    """Create combined dataset for parks and sidewalks.
    
    Args:
        df_parks: DataFrame with park tree data.
        df_sidewalks: DataFrame with sidewalk tree data.
        species_names: Tuple of (park_species, sidewalk_species) names.
        column_mapping: Tuple of (park_height, park_diameter, park_species,
                          sidewalk_height, sidewalk_diameter, sidewalk_species).
    
    Returns:
        Combined DataFrame with standardized columns.
    """
    park_species, sidewalk_species = species_names
    cols = column_mapping
    
    # Process parks data
    df_species_parks = df_parks[
        df_parks[cols[2]] == park_species
    ][list(cols[0:3])].copy()
    
    df_species_parks = df_species_parks.rename(columns={
        cols[0]: 'height',
        cols[1]: 'diameter',
        cols[2]: 'name'
    })
    df_species_parks['environment'] = 'park'
    
    # Process sidewalks data
    df_species_sidewalks = df_sidewalks[
        df_sidewalks[cols[5]] == sidewalk_species
    ][list(cols[3:6])].copy()
    
    df_species_sidewalks = df_species_sidewalks.rename(columns={
        cols[3]: 'height',
        cols[4]: 'diameter',
        cols[5]: 'name'
    })
    df_species_sidewalks['environment'] = 'sidewalk'
    
    # Combine both datasets
    combined_df = pd.concat([df_species_sidewalks, df_species_parks])
    
    logger.info(f"Created combined dataset with {len(combined_df)} records")
    logger.info(f"Parks: {len(df_species_parks)}, Sidewalks: {len(df_species_sidewalks)}")
    
    print(combined_df)
    
    return combined_df


def plot_environment_comparison(
    dataframe: pd.DataFrame,
    variables: List[str],
    output_file: str = None
) -> None:
    """Plot comparison of tree measurements between environments.
    
    Args:
        dataframe: DataFrame with tree data and environment column.
        variables: Variables to plot (e.g., ['diameter', 'height']).
        output_file: Optional file path to save the plot.
    """
    fig, axes = plt.subplots(1, len(variables), figsize=(14, 5))
    
    if len(variables) == 1:
        axes = [axes]
    
    for idx, var in enumerate(variables):
        dataframe.boxplot(var, by='environment', ax=axes[idx])
        axes[idx].set_title(f'{var.title()} by Environment')
        axes[idx].set_xlabel('Environment')
        axes[idx].set_ylabel(var.title())
    
    plt.suptitle('Tree Measurements: Parks vs Sidewalks')
    plt.tight_layout()
    
    if output_file:
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        logger.info(f"Comparison plot saved to {output_file}")
    plt.show()


def load_datasets(
    filepath_parks: str,
    filepath_sidewalks: str
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """Load both datasets.
    
    Args:
        filepath_parks: Path to parks dataset.
        filepath_sidewalks: Path to sidewalks dataset.
    
    Returns:
        Tuple of (parks_df, sidewalks_df).
    """
    try:
        df_parks = pd.read_csv(filepath_parks)
        df_sidewalks = pd.read_csv(filepath_sidewalks)
        logger.info(f"Loaded parks data: {df_parks.shape}")
        logger.info(f"Loaded sidewalks data: {df_sidewalks.shape}")
        return df_parks, df_sidewalks
    except FileNotFoundError as e:
        logger.error(f"File not found: {e}")
        raise
    except Exception as e:
        logger.error(f"Error loading datasets: {e}")
        raise


def main(
    filename_parks: str = 'arbolado-en-espacios-verdes.csv',
    filename_sidewalks: str = 'arbolado-publico-lineal-2017-2018.csv',
    data_dir: str = '../Data/'
) -> None:
    """Main analysis pipeline.
    
    Args:
        filename_parks: Name of parks dataset file.
        filename_sidewalks: Name of sidewalks dataset file.
        data_dir: Directory containing the data.
    """
    try:
        logger.info("Starting tree environment comparison analysis")
        
        # Load datasets
        filepath_parks = os.path.join(data_dir, filename_parks)
        filepath_sidewalks = os.path.join(data_dir, filename_sidewalks)
        
        df_parks, df_sidewalks = load_datasets(
            filepath_parks, filepath_sidewalks
        )
        
        # Define species and columns
        species = ('Tipuana Tipu', 'Tipuana tipu')
        
        columns = (
            'altura_tot', 'diametro', 'nombre_cie',
            'altura_arbol', 'diametro_altura_pecho', 'nombre_cientifico'
        )
        
        variables_to_plot = ['diameter', 'height']
        
        # Create combined dataset
        df_combined = create_environment_datasets(
            df_parks, df_sidewalks, species, columns
        )
        
        # Generate visualization
        logger.info("Creating comparison plots...")
        plot_environment_comparison(
            df_combined,
            variables_to_plot,
            output_file='tree_environment_comparison.png'
        )
        
        logger.info("Tree environment comparison completed successfully")
        
    except Exception as e:
        logger.error(f"Error in analysis: {e}")
        raise


if __name__ == '__main__':
    try:
        if len(sys.argv) >= 3:
            parks_file = sys.argv[1]
            sidewalks_file = sys.argv[2]
        else:
            parks_file = 'arbolado-en-espacios-verdes.csv'
            sidewalks_file = 'arbolado-publico-lineal-2017-2018.csv'
        
        main(filename_parks=parks_file, filename_sidewalks=sidewalks_file)
    except Exception as e:
        logger.error(f"Failed to execute main: {e}")
        sys.exit(1)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Federico Pfund
 E-mail:federicopfund@gmail.com 
"""
#%%

# <------------------------- Imports ---------------------------------------->
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import sys
#%%
# <----------------------- Por Terminal -------------------------------------->
# por terminal:
""" python arbolado_parques_veredas.py 
    arbolado-publico-lineal-2017-2018.csv 
    arbolado-en-espacios-verdes.csv """
    
#%%
# <----------------------- Preguntas ---------------------------------------->
# 1) ¿Qué tendrías que cambiar para repetir el análisis para otras especies?
# 2) ¿Convendría definir una función?
# <-----------------------Respuestas ---------------------------------------->
# 1) Para poder analizar otras especies, deberia (en mi caso) modificar la
#     lista tipas para que obtenga datos con input()
# 
# 2) Seria bueno hacerlo con una funcion para separar el proceso del main.
#    Esto mismo se puede hacer con el resto de las listas!
#%%
# <----------------------- plot_dataset ------------------------------------->
def plot_dataset(dataset, variables):
    '''
    Plots de dataset generado
    '''
    dataset.boxplot(variables[0],by = 'ambiente')
    dataset.boxplot(variables[1],by = 'ambiente')
    plt.show()#grafico


# <--------------------------- datasets ------------------------------------->
def datasets(df_parques, df_veredas, tipas, cols):
    '''
    Creacion de dataset de arbolado en parques y veredas
    '''
    df_tipas_parques = df_parques[df_parques[cols[2]] == 
                                   tipas[0]][cols[0:3]].copy()
    
    df_tipas_parques = df_tipas_parques.rename(columns={cols[0]: 'altura', 
                                                        cols[1]: 'diametro',
                                                        cols[2]: 'nombre'})
    
    df_tipas_parques['ambiente'] = 'parque'
    df_tipas_veredas = df_veredas[df_veredas[cols[5]] == tipas[1]][cols[3:]].copy()
    df_tipas_veredas = df_tipas_veredas.rename(columns={cols[3]: 'altura',
                                                        cols[4]: 'diametro', 
                                                        cols[5]: 'nombre'})
    df_tipas_veredas['ambiente'] = 'vereda'

    df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques])
    print(df_tipas)

    return df_tipas


# <----------------------------- Main --------------------------------------->

# <---------------------------- Sys ----------------------------------------->
if __name__ == '__main__':
    main()
#%%