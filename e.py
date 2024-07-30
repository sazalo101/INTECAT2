import numpy as np
import matplotlib.pyplot as plt

def analyze_signal_fft(f1, f2, fs, duration):
    """
    Analyze the frequency components of a signal s(t) = sin(2πf1t) + sin(2πf2t)
    using Fast Fourier Transform.

    Parameters:
    f1 (float): Frequency of the first sine component in Hz
    f2 (float): Frequency of the second sine component in Hz
    fs (float): Sampling frequency in Hz
    duration (float): Duration of the signal in seconds

    Returns:
    None (displays the plots)
    """
 
    t = np.linspace(0, duration, int(fs * duration), endpoint=False)
    
 
    s = np.sin(2 * np.pi * f1 * t) + np.sin(2 * np.pi * f2 * t)
    
  
    fft_result = np.fft.fft(s)
    
   
    freqs = np.fft.fftfreq(len(t), 1/fs)
    
    
    magnitude_spectrum = np.abs(fft_result) / len(t)
    
  
    plt.figure(figsize=(12, 8))
    
   
    plt.subplot(2, 1, 1)
    plt.plot(t, s)
    plt.title('Time Domain Signal')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    
   
    plt.subplot(2, 1, 2)
    plt.plot(freqs[:len(freqs)//2], magnitude_spectrum[:len(freqs)//2])
    plt.title('Frequency Spectrum')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude')
    plt.xlim(0, max(f1, f2) * 1.5) 
    
    plt.tight_layout()
    plt.show()
    
 
    threshold = 0.1  
    detected_freqs = freqs[magnitude_spectrum > threshold]
    print("Detected frequency components:")
    for freq in detected_freqs:
        if freq > 0:  
            print(f"{freq:.2f} Hz")


f1, f2 = 50, 120  
fs = 1000  
duration = 1 

analyze_signal_fft(f1, f2, fs, duration)