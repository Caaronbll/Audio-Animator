#!/usr/bin/env python3

import numpy as np 
import pandas as pd
import matplotlib.pylab as plt
import librosa
import librosa.display
print(librosa.__version__) # print version


audio_path = 'Audio_files/piano_test.wav'
y, sr = librosa.load(audio_path, sr=22050) # sr = sample rate(Hz)

# calculates measuments
total_measurements = len(y)
sample_rate = sr
length_in_seconds = total_measurements / sample_rate
print('Measurements =', total_measurements)
print('Sample Rate =', sample_rate,'(Hz)')
print('Length =', round(length_in_seconds, 2),'(s)')

# Define the number of measurements per group
group_size = 1

# Define a scaling factor
scaling_factor = 100000

# Calculate scaled averages for each group
averages = [np.mean(y[i:i + group_size]) * scaling_factor for i in range(0, len(y), group_size)]

# Display the averages with full precision
#for idx, avg in enumerate(averages, start=1):
#    print(f'Group {idx}: Scaled Average = {avg}')

# Create the time axis for the x-axis (this represents the group numbers)
time = np.arange(1, len(averages) + 1)

# Plot the scaled averages
plt.figure(figsize=(10, 6))
plt.plot(time, averages, marker='', linestyle='-', color='b', label='Scaled Average')
plt.xlabel('Group Number')
plt.ylabel('Scaled Average')
plt.title('Scaled Averages of y for Every 365 Measurements')
plt.grid(True)
plt.legend()

# Show the plot
plt.show()