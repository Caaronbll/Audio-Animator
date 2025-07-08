

from moviepy.editor import VideoClip, AudioFileClip
import numpy as np
from load2 import analyze_hits

# === Audio path ===
hh_audiopath = './audio_files/hh_audio.wav'

# === Analyze the high-hat track ===
hit_windows, times, sr = analyze_hits(hh_audiopath)
frame_duration = 0.05
video_duration = times[-1] if len(times) > 0 else 0

# === Check for hits ===
if not hit_windows:
    raise ValueError("No hits detected — check your audio or threshold settings.")

# === Visual parameters ===
width, height = 1280, 1280
circle_color = np.array([255, 200, 50])  # Yellow-orange
max_radius = 100
scale_factor = 54

# === Frame generation ===
def make_frame(t):
    total_amp = 0

    for hit in hit_windows:
        if hit['start'] <= t <= hit['end']:
            rel_time = t - hit['start']
            idx = int(rel_time // frame_duration)
            if idx < len(hit['amplitude_curve']):
                total_amp += hit['amplitude_curve'][idx]

    total_amp = min(total_amp, 1.0)

    # Initialize frame
    frame = np.zeros((height, width, 3), dtype=np.float32)

    if total_amp > 0:
        radius = int(max_radius * total_amp * scale_factor)
        center_x, center_y = width // 2, height // 2
        Y, X = np.ogrid[:height, :width]
        distance = np.sqrt((X - center_x)**2 + (Y - center_y)**2)

        gradient = np.clip(1 - (distance / radius), 0, 1)
        gradient = gradient**4  # Soft, fast falloff

        for c in range(3):
            frame[:, :, c] = gradient * circle_color[c]

    return np.clip(frame, 0, 255).astype(np.uint8)

# === Create and export video ===
video_clip = VideoClip(make_frame, duration=video_duration)
audio_clip = AudioFileClip(hh_audiopath)
video_with_audio = video_clip.set_audio(audio_clip)
video_with_audio.write_videofile("high_hat_visual.mp4", fps=20)

