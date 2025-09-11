# -*- coding: utf-8 -*-
"""
Created on Tue Sep  9 11:45:05 2025

@author: Priya
"""

#a.	Generate two sine wave signals with frequencies of 5 Hz and 10 Hz, 
#both sampled at 1000 Hz for 1 second. Add the two signals together and plot the result.

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

fs = 1000
f1 = 5
f2 = 10 
t = np.linspace(0, 1, fs, endpoint=False)  
sine_wave_1 = np.sin(2 * np.pi * f1 * t)
sine_wave_2 = np.sin(2 * np.pi * f2 * t)
combined_wave = sine_wave_1 + sine_wave_2

plt.figure(figsize=(10, 5))

plt.plot(t, combined_wave)
plt.title("Combined Sine Wave Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.show()


#b.Generate a 5 Hz sine wave and a 10 Hz cosine wave, both sampled at 500 Hz
#for 2 seconds. Multiply the two signals element-wise and plot the resulting signal.

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

fs = 500
t = np.linspace(0, 2, fs, endpoint=False) 

f_sine = 5  
sine_wave = np.sin(2 * np.pi * f_sine * t)

f_cosine = 10 
cosine_wave = np.cos(2 * np.pi * f_cosine * t)

result = sine_wave * cosine_wave

plt.figure(figsize=(10, 10))

plt.subplot(4, 2, 4)
plt.plot(t, result)
plt.title('Result_wave')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')


#c.Generate a 5 Hz sine wave signal and shift it in time by 0.1 seconds.
# Plot the original and shifted signals on the same graph for comparison.

import numpy as np
import matplotlib.pyplot as plt

frequency = 5 
amplitude = 1
time_shift = 0.1 

sampling_rate = 100 
duration = 1 
t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)

original_signal = amplitude * np.sin(2 * np.pi * frequency * t)
shifted_signal = amplitude * np.sin(2 * np.pi * frequency * (t - time_shift))

plt.figure(figsize=(10, 6))
plt.plot(t, original_signal,label = 'Original Signal')
plt.plot(t, shifted_signal,label = 'Shifted Signal')
plt.title('Original and Time-Shifted Sine Waves')
plt.xlabel('Time')
plt.ylabel('Amplitude')


#d.	Generate a 10 Hz sine wave and scale its amplitude by a factor of 3. 
#Plot the original and scaled signals together.

import numpy as np
import matplotlib.pyplot as plt

frequency = 10
amplitude = 1
scaled_amplitude = 3

sampling_rate = 1000 
duration = 1 
t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)

original_signal = amplitude * np.sin(2 * np.pi * frequency * t)
scaled_signal = amplitude * scaled_amplitude * np.sin(2 * np.pi * frequency * t)

plt.figure(figsize=(10, 6))
plt.plot(t, original_signal, label='Original Sine Wave')

plt.plot(t, scaled_signal, label='Scaled Sine Wave')
plt.title('Original and Scaled Sine Waves')
plt.xlabel('Time')
plt.ylabel('Amplitude')

#e.	Generate a 5 Hz sine wave and reverse it in time. 
#Plot the original and reversed signals on the same graph.

import numpy as np
import matplotlib.pyplot as plt

frequency = 10
amplitude = 1
sampling_rate = 1000 
duration = 1 
t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)

original_signal = amplitude * np.sin(2 * np.pi * frequency * t)
reversed_signal = original_signal[::-1]

plt.figure(figsize=(10, 6))
plt.plot(t, original_signal, label='Original Sine Wave')
plt.plot(t, reversed_signal, label='Reversed Sine Wave')
plt.title('Original and Reversed Sine Waves')
plt.xlabel('Time')
plt.ylabel('Amplitude')