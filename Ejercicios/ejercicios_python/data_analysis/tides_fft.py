"""FFT analysis for tide data.

Performs Fast Fourier Transform analysis on tide measurements
to identify dominant frequencies and peaks in tidal patterns.
"""

import logging
import sys
import os
from typing import Tuple, List

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import signal

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def calculate_fft(
    time_series: np.ndarray,
    sampling_rate: float = 24.0
) -> Tuple[np.ndarray, np.ndarray]:
    """Calculate Fast Fourier Transform of a time series.
    
    Computes the FFT of real-valued time series data and returns
    the frequency components and their corresponding complex amplitudes.
    
    Args:
        time_series: Array of real numbers representing time-series data.
        sampling_rate: Sampling frequency (default: 24 samples per unit time).
    
    Returns:
        Tuple of (frequencies, fft_values) with positive frequencies only.
    """
    n_samples = len(time_series)
    
    # Compute FFT and extract positive frequencies
    frequencies = np.fft.fftfreq(n_samples, d=1/sampling_rate)[:n_samples//2]
    fft_values = (np.fft.fft(time_series) / n_samples)[:n_samples//2]
    
    logger.info(f"Calculated FFT for {n_samples} samples at {sampling_rate} Hz")
    
    return frequencies, fft_values


def find_spectral_peaks(
    fft_values: np.ndarray,
    frequencies: np.ndarray,
    prominence_threshold: float = 8.0,
    height_threshold: float = 0.5
) -> List[dict]:
    """Find peaks in the frequency spectrum.
    
    Args:
        fft_values: FFT complex values.
        frequencies: Corresponding frequencies.
        prominence_threshold: Minimum prominence for peak detection.
        height_threshold: Minimum height for peak detection.
    
    Returns:
        List of dictionaries with peak information.
    """
    magnitude = np.abs(fft_values)
    
    # Find peaks
    peak_indices, peak_properties = signal.find_peaks(
        magnitude,
        prominence=prominence_threshold,
        height=height_threshold
    )
    
    peaks = []
    for idx in peak_indices:
        peaks.append({
            'index': idx,
            'frequency': frequencies[idx],
            'magnitude': magnitude[idx],
            'phase': np.angle(fft_values[idx])
        })
    
    logger.info(f"Found {len(peaks)} spectral peaks")
    
    return peaks


def plot_frequency_spectrum(
    frequencies: np.ndarray,
    fft_values: np.ndarray,
    peaks: List[dict] = None,
    title: str = "Frequency Spectrum",
    output_file: str = None
) -> None:
    """Plot frequency spectrum with peaks highlighted.
    
    Args:
        frequencies: Frequency array.
        fft_values: FFT values array.
        peaks: List of peak information (optional).
        title: Title for the plot.
        output_file: Optional file path to save the plot.
    """
    plt.figure(figsize=(12, 6))
    
    magnitude = np.abs(fft_values)
    plt.plot(frequencies, magnitude, linewidth=1.5)
    
    # Highlight peaks
    if peaks:
        peak_freqs = [p['frequency'] for p in peaks]
        peak_mags = [p['magnitude'] for p in peaks]
        plt.scatter(peak_freqs, peak_mags, color='red', s=100, zorder=5)
    
    plt.xlabel('Frequency (cycles per unit time)')
    plt.ylabel('Power (Energy)')
    plt.title(title)
    plt.grid(True, alpha=0.3)
    plt.xlim(0, np.max(frequencies))
    
    if output_file:
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        logger.info(f"Plot saved to {output_file}")
    
    plt.show()


def load_tide_data(
    filepath: str,
    start_date: str = None,
    end_date: str = None
) -> Tuple[np.ndarray, np.ndarray]:
    """Load tide data from CSV file.
    
    Args:
        filepath: Path to CSV file with tide data.
        start_date: Optional start date for subsetting.
        end_date: Optional end date for subsetting.
    
    Returns:
        Tuple of (heights_SF, heights_BA) arrays.
    """
    try:
        df = pd.read_csv(filepath, index_col=['Time'], parse_dates=True)
        
        # Subset by dates if provided
        if start_date and end_date:
            df = df[start_date:end_date]
        
        heights_sf = df['H_SF'].to_numpy()
        heights_ba = df['H_BA'].to_numpy()
        
        logger.info(f"Loaded tide data ({len(heights_sf)} samples)")
        
        return heights_sf, heights_ba
    except FileNotFoundError:
        logger.error(f"File not found: {filepath}")
        raise
    except Exception as e:
        logger.error(f"Error loading data: {e}")
        raise


def main(
    data_file: str = '../Data/OBS_SHN_SF-BA.csv',
    start_date: str = '2014-01',
    end_date: str = '2014-06'
) -> None:
    """Main FFT analysis pipeline.
    
    Args:
        data_file: Path to tide data CSV.
        start_date: Start date for analysis.
        end_date: End date for analysis.
    """
    try:
        logger.info("Starting FFT analysis pipeline")
        
        # Load data
        heights_sf, heights_ba = load_tide_data(
            data_file, start_date, end_date
        )
        
        # Analyze San Fernando station
        logger.info("\n--- San Fernando Station Analysis ---")
        freq_sf, fft_sf = calculate_fft(heights_sf)
        peaks_sf = find_spectral_peaks(fft_sf, freq_sf)
        
        plot_frequency_spectrum(
            freq_sf, fft_sf, peaks_sf,
            title=f"FFT: San Fernando ({start_date} to {end_date})",
            output_file='fft_san_fernando.png'
        )
        
        # Analyze Buenos Aires station
        logger.info("\n--- Buenos Aires Station Analysis ---")
        freq_ba, fft_ba = calculate_fft(heights_ba)
        peaks_ba = find_spectral_peaks(fft_ba, freq_ba)
        
        plot_frequency_spectrum(
            freq_ba, fft_ba, peaks_ba,
            title=f"FFT: Buenos Aires ({start_date} to {end_date})",
            output_file='fft_buenos_aires.png'
        )
        
        # Display peak information
        logger.info("\nDominant Frequencies:")
        if peaks_sf:
            print("\nSan Fernando:")
            for peak in sorted(peaks_sf, key=lambda x: x['magnitude'], reverse=True)[:3]:
                print(f"  Frequency: {peak['frequency']:.4f}, "
                      f"Magnitude: {peak['magnitude']:.4f}, "
                      f"Phase: {peak['phase']:.4f}")
        
        if peaks_ba:
            print("\nBuenos Aires:")
            for peak in sorted(peaks_ba, key=lambda x: x['magnitude'], reverse=True)[:3]:
                print(f"  Frequency: {peak['frequency']:.4f}, "
                      f"Magnitude: {peak['magnitude']:.4f}, "
                      f"Phase: {peak['phase']:.4f}")
        
        logger.info("FFT analysis completed successfully")
        
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
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Federico Pfund
 E-mail:federicopfund@gmail.com 
"""


#%%%
# <------------------------------ Imports ----------------------------------->
import matplotlib.pyplot as plt
from scipy import signal
import pandas as pd
import numpy as np
import sys
import os
#%%
# <----------------------------- Calcular_fft ------------------------------->
# <----INPUT-->Debe ser un vector con números reales 
#-------------- representando datos de una serie temporal.
#
# <---OUTPUT-->Devuelve dos vectores, uno de frecuencias 
#-------------- y otro con la transformada propiamente.
#-----------------------------------------------------------------------------
def calcular_fft(y, freq_sampleo = 24.0):
    
    '''
    freq_sampleo está seteado para considerar 24 datos por unidad.
    
    La transformada contiene los valores complejos
    que se corresponden con respectivas frecuencias.'''
    N = len(y)
    freq = np.fft.fftfreq(N, d = 1/freq_sampleo)[:N//2]
    tran = (np.fft.fft(y)/N)[:N//2]
    return freq, tran


# <------------------------------- Ang_frec --------------------------------->
def ang_frec(alturas):
    freq, fft = calcular_fft(alturas)
    plt.plot(freq, np.abs(fft))
    plt.xlabel("Frecuencia")
    plt.ylabel("Potencia (energía)")
    plt.xlim(0,4)
    plt.ylim(0,20)
    # me quedo solo con el último pico
    pico = signal.find_peaks(np.abs(fft), prominence = 8)[0][-1]
    #se grafican los picos como circulitos rojos
    plt.scatter(freq[pico], np.abs(fft)[pico], facecolor='r')

    ang = np.angle(fft)[pico]
    frec = freq[pico]

    return (ang, frec)


# <--------------------------- Sys ------------------------------------------>
if __name__ == '__main__':
    main()
#%%