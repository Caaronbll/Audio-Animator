from moviepy.editor import VideoClip, AudioFileClip
from PIL import Image, ImageDraw
import numpy as np

# Import hit detection from load.py
from load2 import analyze_hits

# === Audio path ===
hh_audiopath = './audio_files/hh_audio.wav'

# === Analyze the high-hat track ===
hit_windows, times, sr = analyze_hits(hh_audiopath)
frame_duration = 0.05  # Keep in sync with load.py
video_duration = times[-1] if len(times) > 0 else 0

# === Check for at least one hit
if not hit_windows:
    raise ValueError("No hits detected — check your audio or threshold settings.")

# === Visual parameters
width, height = 720, 720
circle_color = (255, 200, 50)
max_radius = 120
hit = hit_windows[0]  # Just one hit for now — expand later

# === Frame generation function
def make_frame(t):
    total_amp = 0  # Accumulate amplitude from all overlapping hits

    # Loop through all hit windows
    for hit in hit_windows:
        if hit['start'] <= t <= hit['end']:
            rel_time = t - hit['start']
            idx = int(rel_time // frame_duration)
            if idx < len(hit['amplitude_curve']):
                total_amp += hit['amplitude_curve'][idx]

    # Optional: clamp amplitude to a maximum of 1.0
    total_amp = min(total_amp, 1.0)

    # Debug prints
    print(f"Time: {t:.2f}s | Total Amplitude: {total_amp:.3f}")

    # Create black frame
    img = Image.new("RGB", (width, height), (0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Draw glow if total amplitude > 0
    if total_amp > 0:
        radius = int(max_radius * total_amp * 100)
        center = (width // 2, height // 2)
        bbox = [
            center[0] - radius, center[1] - radius,
            center[0] + radius, center[1] + radius
        ]
        draw.ellipse(bbox, fill=circle_color)

    return np.array(img)



# === Create and export video
video_clip = VideoClip(make_frame, duration=video_duration)
audio_clip = AudioFileClip(hh_audiopath)
video_with_audio = video_clip.set_audio(audio_clip)
video_with_audio.write_videofile("high_hat_visual.mp4", fps=20)

