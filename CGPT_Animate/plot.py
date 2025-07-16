import librosa
import numpy as np
import matplotlib.pyplot as plt

# Load the audio file
audio_path = "./audio_files/hh_audio.wav"
y, sr = librosa.load(audio_path, sr=None)

# Duration to analyze (3 seconds)
duration_sec = 3
sample_limit = int(sr * duration_sec)

# Slice the waveform to first 10 seconds
y_slice = y[:sample_limit]

# Create time axis
t = np.linspace(0, duration_sec, num=sample_limit)

# Plot the waveform
plt.figure(figsize=(12, 4))
plt.plot(t, y_slice, linewidth=0.5)
plt.title("Raw Waveform - First 3 Seconds")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.tight_layout()
plt.show()





