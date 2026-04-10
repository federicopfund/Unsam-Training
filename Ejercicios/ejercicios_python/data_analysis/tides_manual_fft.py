"""Manual FFT implementation and analysis.

Demonstrates FFT calculation and analysis of tide data with
manual implementation of frequency analysis techniques.
"""

import logging
import sys
import os
from typing import Tuple

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


def compute_fft_manual(
    y: np.ndarray,
    sampling_rate: float = 24.0
) -> Tuple[np.ndarray, np.ndarray]:
    """Manual FFT computation for time-series data.
    
    Computes the FFT of a real-valued time series and returns
    normalized positive frequencies and their complex amplitudes.
    
    Args:
        y: Array of real numbers representing time series (required: real vector).
        sampling_rate: Sampling rate (default 24 = 24 samples per unit time).
    
    Returns:
        Tuple of (frequencies, fft_transform):
            - frequencies: Array of positive frequencies
            - fft_transform: Complex FFT values for positive frequencies
    """
    n = len(y)
    
    # FFT computation and normalization
    freq = np.fft.fftfreq(n, d=1/sampling_rate)[:n//2]
    transform = (np.fft.fft(y) / n)[:n//2]
    
    logger.info(f"Computed FFT for {n} samples at {sampling_rate} Hz sampling rate")
    
    return freq, transform


def detect_frequency_peaks(
    fft_values: np.ndarray,
    frequencies: np.ndarray,
    prominence: float = 8.0
) -> Tuple[np.ndarray, float, float]:
    """Detect dominant frequency peaks in FFT.
    
    Args:
        fft_values: FFT complex values.
        frequencies: Corresponding frequencies.
        prominence: Minimum prominence for peak detection.
    
    Returns:
        Tuple of (peak_index, angle, frequency) for dominant peak.
    """
    magnitude = np.abs(fft_values)
    
    # Find peaks with specified prominence
    peak_indices = signal.find_peaks(magnitude, prominence=prominence)[0]
    
    if len(peak_indices) == 0:
        logger.warning("No peaks found with specified prominence threshold")
        return None, None, None
    
    # Get the last (rightmost) peak
    peak_idx = peak_indices[-1]
    
    angle = np.angle(fft_values)[peak_idx]
    frequency = frequencies[peak_idx]
    magnitude_val = magnitude[peak_idx]
    
    logger.info(f"Detected peak at frequency {frequency:.4f} Hz, "
                f"magnitude {magnitude_val:.4f}, phase {angle:.4f}")
    
    return peak_idx, angle, frequency


def plot_fft_analysis(
    frequencies: np.ndarray,
    fft_values: np.ndarray,
    peak_idx: int = None,
    title: str = "FFT Analysis",
    output_file: str = None
) -> None:
    """Plot FFT magnitude spectrum with peak detection.
    
    Args:
        frequencies: Frequency array.
        fft_values: FFT values.
        peak_idx: Index of dominant peak (optional).
        title: Plot title.
        output_file: Optional output file path.
    """
    plt.figure(figsize=(12, 6))
    
    magnitude = np.abs(fft_values)
    plt.plot(frequencies, magnitude, linewidth=1.5)
    
    plt.xlabel("Frequency (cycles per unit time)")
    plt.ylabel("Power (Energy)")
    plt.title(title)
    plt.xlim(0, 4)
    plt.grid(True, alpha=0.3)
    
    # Highlight peak if detected
    if peak_idx is not None:
        peak_freq = frequencies[peak_idx]
        peak_mag = magnitude[peak_idx]
        plt.scatter(peak_freq, peak_mag, color='red', s=100, zorder=5)
        plt.annotate(f'Peak at {peak_freq:.3f}',
                     xy=(peak_freq, peak_mag),
                     xytext=(peak_freq + 0.2, peak_mag + 1),
                     arrowprops=dict(arrowstyle='->', color='red'))
    
    if output_file:
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        logger.info(f"Plot saved to {output_file}")
    
    plt.show()


def main(
    data_file: str = '../Data/OBS_SHN_SF-BA.csv',
    start_date: str = '2014-01',
    end_date: str = '2014-06'
) -> None:
    """Main manual FFT analysis pipeline.
    
    Args:
        data_file: Path to tide data CSV file.
        start_date: Start date for analysis.
        end_date: End date for analysis.
    """
    try:
        logger.info("Starting manual FFT analysis pipeline")
        
        # Load data
        logger.info(f"Loading data from {data_file}")
        df = pd.read_csv(data_file, index_col=['Time'], parse_dates=True)
        
        # Extract time period
        alturas_sf = df[start_date:end_date]['H_SF'].to_numpy()
        alturas_ba = df[start_date:end_date]['H_BA'].to_numpy()
        
        logger.info(f"Extracted data: {len(alturas_sf)} samples for San Fernando, "
                    f"{len(alturas_ba)} samples for Buenos Aires")
        
        # Analyze San Fernando
        logger.info("\n--- San Fernando Analysis ---")
        freq_sf, fft_sf = compute_fft_manual(alturas_sf)
        peak_idx_sf, angle_sf, freq_peak_sf = detect_frequency_peaks(fft_sf, freq_sf)
        
        plot_fft_analysis(
            freq_sf, fft_sf, peak_idx_sf,
            title=f"San Fernando FFT Analysis ({start_date} to {end_date})",
            output_file='fft_manual_san_fernando.png'
        )
        
        # Analyze Buenos Aires
        logger.info("\n--- Buenos Aires Analysis ---")
        freq_ba, fft_ba = compute_fft_manual(alturas_ba)
        peak_idx_ba, angle_ba, freq_peak_ba = detect_frequency_peaks(fft_ba, freq_ba)
        
        plot_fft_analysis(
            freq_ba, fft_ba, peak_idx_ba,
            title=f"Buenos Aires FFT Analysis ({start_date} to {end_date})",
            output_file='fft_manual_buenos_aires.png'
        )
        
        # Summary
        print("\n" + "="*60)
        print("MANUAL FFT ANALYSIS SUMMARY")
        print("="*60)
        
        if angle_sf is not None:
            print(f"\nSan Fernando Dominant Peak:")
            print(f"  Frequency: {freq_peak_sf:.4f} Hz")
            print(f"  Phase angle: {angle_sf:.4f} radians")
        
        if angle_ba is not None:
            print(f"\nBuenos Aires Dominant Peak:")
            print(f"  Frequency: {freq_peak_ba:.4f} Hz")
            print(f"  Phase angle: {angle_ba:.4f} radians")
        
        print("="*60 + "\n")
        
        logger.info("Manual FFT analysis completed successfully")
        
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
#%%

# <------------------------------ Imports ----------------------------------->
from scipy import signal # para procesar señales
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
import sys
#%%
# <----------------------------- Calcular_fft ------------------------------->
# <----INPUT-->Debe ser un vector con números reales 
#-------------- representando datos de una serie temporal.
#
# <---OUTPUT-->Devuelve dos vectores, uno de frecuencias 
#-------------- y otro con la transformada propiamente.
#-----------------------------------------------------------------------------

def calcular_fft(y, freq_sampleo = 24.0):
    '''y debe ser un vector con números reales
    representando datos de una serie temporal.
    
    freq_sampleo está seteado para considerar 24 datos por unidad.
    
    Devuelve dos vectores, uno de frecuencias 
    y otro con la transformada propiamente.
    
    La transformada contiene los valores complejos
    que se corresponden con respectivas frecuencias.'''
    
    N = len(y)
    freq = np.fft.fftfreq(N, d = 1/freq_sampleo)[:N//2]
    tran = (np.fft.fft(y)/N)[:N//2]
    return freq, tran
#<--------------------------------------------------------------------------->
# Indico directorio
directorio = '../Data/' 
fname = os.path.join(directorio,'OBS_SHN_SF-BA.csv') # Busco el archivo
df = pd.read_csv(fname, index_col=['Time'], parse_dates=True)

inicio = '2014-01'
fin = '2014-06'
alturas_sf = df[inicio:fin]['H_SF'].to_numpy()
alturas_ba = df[inicio:fin]['H_BA'].to_numpy()

# <-------------------------------------------------------------------------->

freq_sf, fft_sf = calcular_fft(alturas_sf)

plt.plot(freq_sf, np.abs(fft_sf))
plt.xlabel("Frecuencia")
plt.ylabel("Potencia (energía)")
plt.xlim(0,4)
plt.ylim(0,20)
# me quedo solo con el último pico
pico_sf = signal.find_peaks(np.abs(fft_sf), prominence = 8)[0][-1]
print(pico_sf)
# es el pico a analizar, el de la onda de mareas
# marco ese pico con un circulito rojo
plt.scatter(freq_sf[pico_sf], np.abs(fft_sf)[pico_sf], facecolor = 'r')

ang_sf = np.angle(fft_sf)[pico_sf]
print(ang_sf)
# Obtenemos un valor cercano a pi/2. 
# Recordemos que 2pi corresponde a un desfasaje de un ciclo completo de la curva. 
# Como nuestra curva de estudio tiene una frecuencia diaria ligeramente inferior ...
#...a 2 (freq_sf[350]~1.93), 2pi corresponde a 24/1.93 horas ~ 12.44 horas.
# Por lo tanto la fase obtenida con angSF[350] 
print(f'desfasaje de:{ang_sf * 24 / (2 * np.pi * freq_sf[350])}')
# Grafica
plt.show()