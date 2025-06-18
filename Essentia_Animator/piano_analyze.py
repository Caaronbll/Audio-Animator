#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
import essentia
import essentia.standard as es
from moviepy.editor import AudioFileClip, VideoClip
import os

# === Step 1: Load audio ===
audio_path = "Audio_files/hh_audio.wav"
loader = es.MonoLoader(filename=audio_path)
audio = loader()

# === Step 2: Hi-hat detection using Essentia's RhythmExtractor2013 ===
rhythm_extractor = es.RhythmExtractor2013(method="multifeature")
bpm, ticks, _, _, _ = rhythm_extractor(audio)

# For hi-hats, we assume they're frequent and high-frequency,
# so we'll further filter events using SpectralComplexity or high-pass filter (optional)

# === Step 3: Create visual flash events ===
# Circle duration in seconds
circle_duration = 0.1
fps = 30
circle_frames = int(circle_duration * fps)

# Video duration (use full audio length)
audio_clip = AudioFileClip(audio_path)
video_duration = audio_clip.duration

# Build list of flash frame indices
flash_times = ticks  # Assuming ticks ~ hi-hats
flash_frames = [int(t * fps) for t in flash_times]

# === Step 4: Create video frames ===
def make_frame(t):
    frame = np.zeros((720, 1280, 3), dtype=np.uint8)  # Black background
    current_frame = int(t * fps)

    # If current time is within any circle flash frame range, draw a circle
    for ff in flash_frames:
        if ff <= current_frame < ff + circle_frames:
            fig, ax = plt.subplots(figsize=(12.8, 7.2), dpi=100)
            ax.set_facecolor("black")
            circle = plt.Circle((0.5, 0.5), 0.1, color='white', transform=ax.transAxes)
            ax.add_artist(circle)
            ax.set_xlim(0, 1)
            ax.set_ylim(0, 1)
            ax.axis('off')
            fig.canvas.draw()
            frame = np.frombuffer(fig.canvas.tostring_rgb(), dtype=np.uint8)
            frame = frame.reshape(fig.canvas.get_width_height()[::-1] + (3,))
            plt.close(fig)
            break
    return frame

# === Step 5: Generate video ===
video = VideoClip(make_frame, duration=video_duration)
video = video.set_audio(audio_clip)
output_path = "hi_hat_visualization.mp4"
video.write_videofile(output_path, fps=fps)

print(f"Video saved to {output_path}")
