import librosa
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# Audio file path
hh_audiopath = './audio_files/hh_audio.wav'

# load audio file
# y = audio time series (amplitude data), sr = original sample rate
y, sr = librosa.load(hh_audiopath, sr=None)

print(f"Audio loaded. Sample rate: {sr} Hz")
print(f"Audio duration: {len(y)/sr:.2f} seconds")


# define frame duration (seconds)
frame_duration = 0.05  # 50 milliseconds

# convert duration to number of audio samples
frame_length = int(sr * frame_duration)

# calculate RMS (amplitude energy) in each frame
rms = librosa.feature.rms(y=y, frame_length=frame_length, hop_length=frame_length)[0]

# get the timestamps for each RMS value
times = librosa.frames_to_time(range(len(rms)), sr=sr, hop_length=frame_length)

# Set your amplitude threshold again
threshold = np.max(rms) * 0.37

# Create a list to store hit/release pairs
hit_windows = []

# Track whether we're inside a "hit" right now
hit_windows = []
in_hit = False
hit_start_idx = None

for i in range(len(rms)):
    if not in_hit and rms[i] > threshold:
        hit_start_idx = i
        in_hit = True
    elif in_hit and rms[i] <= threshold:
        hit_end_idx = i
        # Skip very short hits
        if hit_end_idx > hit_start_idx + 1:
            window = {
                'start': times[hit_start_idx],
                'end': times[hit_end_idx],
                'amplitude_curve': rms[hit_start_idx:hit_end_idx+1].tolist()
            }
            hit_windows.append(window)
        in_hit = False


print(f"Detected {len(hit_windows)} valid high-hat hit windows.")
print("First few:", hit_windows[:5])


# Visualize hit durations on top of the RMS plot
# Plot amplitude curves from the first few hits
num_to_plot = 1  # You can increase this if you want

plt.figure(figsize=(10, 6))
for i in range(min(num_to_plot, len(hit_windows))):
    curve = hit_windows[i]['amplitude_curve']
    times_local = np.linspace(0, len(curve) * frame_duration, len(curve))
    plt.plot(times_local, curve, label=f'Hit {i+1}')

plt.title('Amplitude Curves for First Few High-Hat Hits')
plt.xlabel('Time (seconds since hit start)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()

# Visualize hit durations on top of the RMS plot
plt.figure(figsize=(14, 5))
plt.plot(times, rms, color='orange')
plt.axhline(y=threshold, color='red', linestyle='--', label='Threshold')
for window in hit_windows:
    plt.axvspan(window['start'], window['end'], color='yellow', alpha=0.3)
plt.title('High-Hat Hit/Release Detection')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()




