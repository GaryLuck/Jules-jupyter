import nbformat as nbf

nb = nbf.v4.new_notebook()

text = """# Three Waves: Sine, Square, and Sawtooth in Frequency and Time Domains
This notebook displays three basic waveforms in both the time domain and frequency domain.
"""

code = """import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Parameters
fs = 1000  # Sampling frequency
t = np.linspace(0, 1, fs, endpoint=False)
f = 5  # Frequency of waves in Hz

# Generate waves
sine_wave = np.sin(2 * np.pi * f * t)
square_wave = signal.square(2 * np.pi * f * t)
sawtooth_wave = signal.sawtooth(2 * np.pi * f * t)

# Plot Time Domain
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(t, sine_wave)
plt.title('Sine Wave (Time Domain)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(t, square_wave)
plt.title('Square Wave (Time Domain)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(t, sawtooth_wave)
plt.title('Sawtooth Wave (Time Domain)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid(True)

plt.tight_layout()
plt.show()

# Compute and Plot Frequency Domain using FFT
def plot_fft(wave, title, subplot_idx):
    fft_vals = np.fft.fft(wave)
    fft_freq = np.fft.fftfreq(len(wave), 1/fs)

    # Take positive half of the frequencies
    pos_mask = fft_freq > 0
    freqs = fft_freq[pos_mask]
    mags = np.abs(fft_vals[pos_mask]) * 2 / len(wave) # Normalize amplitude

    plt.subplot(3, 1, subplot_idx)
    # Plot up to 50 Hz to see the harmonics clearly
    mask_50hz = freqs <= 50
    plt.stem(freqs[mask_50hz], mags[mask_50hz], basefmt=" ")
    plt.title(title)
    plt.xlabel('Frequency [Hz]')
    plt.ylabel('Magnitude')
    plt.grid(True)

plt.figure(figsize=(12, 8))
plot_fft(sine_wave, 'Sine Wave (Frequency Domain)', 1)
plot_fft(square_wave, 'Square Wave (Frequency Domain)', 2)
plot_fft(sawtooth_wave, 'Sawtooth Wave (Frequency Domain)', 3)

plt.tight_layout()
plt.show()
"""

nb['cells'] = [nbf.v4.new_markdown_cell(text),
               nbf.v4.new_code_cell(code)]

with open('waves.ipynb', 'w') as f:
    nbf.write(nb, f)
