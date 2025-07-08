from moviepy.editor import VideoClip, AudioFileClip, CompositeVideoClip
import numpy as np
from PIL import Image, ImageDraw


# === Input from your hit_windows ===
# For now, we'll test with just the first hit
hit = hit_windows[0]
frame_duration = 0.05  # already defined earlier
video_duration = times[-1]  # same as audio duration


# === Visual parameters ===
width, height = 720, 720
circle_color = (255, 200, 50)  # yellow-orange
max_radius = 120


# === Light behavior ===
def make_frame(t):
    # Check if we're in the hit window
    if hit['start'] <= t <= hit['end']:
        # Find the right frame in the amplitude_curve
        rel_time = t - hit['start']
        idx = int(rel_time // frame_duration)
        if idx >= len(hit['amplitude_curve']):
            amp = 0
        else:
            amp = hit['amplitude_curve'][idx]
    else:
        amp = 0


    # Create blank black frame
    img = Image.new("RGB", (width, height), (0, 0, 0))
    draw = ImageDraw.Draw(img)


    # Draw glowing circle if amp > 0
    if amp > 0:
        radius = int(max_radius * amp)
        center = (width // 2, height // 2)
        bbox = [
            center[0] - radius, center[1] - radius,
            center[0] + radius, center[1] + radius
        ]
        draw.ellipse(bbox, fill=circle_color)


    return np.array(img)


# === Create video clip ===
video_clip = VideoClip(make_frame, duration=video_duration)


# === Add original audio ===
audio_clip = AudioFileClip(hh_audiopath)
video_with_audio = video_clip.set_audio(audio_clip)


# === Export video ===
video_with_audio.write_videofile("high_hat_visual.mp4", fps=20)
