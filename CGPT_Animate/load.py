import librosa
import numpy as np
import matplotlib.pyplot as plt

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

# optional: Plot waveform
plt.figure(figsize=(14, 5))
plt.plot(times, rms, color='orange')
plt.title('RMS Amplitude Over Time')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.show()