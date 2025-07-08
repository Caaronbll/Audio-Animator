import librosa
import numpy as np

def analyze_hits(audio_path, frame_duration=0.05, threshold_ratio=0.37):
    """
    Analyze amplitude spikes in an audio file (e.g., high-hats).

    Returns:
        hit_windows: list of {start, end, amplitude_curve}
        times: timestamps for each frame
        sr: sample rate
    """
    y, sr = librosa.load(audio_path, sr=None)
    print(f"Audio loaded. Sample rate: {sr} Hz")
    print(f"Audio duration: {len(y)/sr:.2f} seconds")

    frame_length = int(sr * frame_duration)
    rms = librosa.feature.rms(y=y, frame_length=frame_length, hop_length=frame_length)[0]
    times = librosa.frames_to_time(range(len(rms)), sr=sr, hop_length=frame_length)
    threshold = np.max(rms) * threshold_ratio

    hit_windows = []
    in_hit = False
    hit_start_idx = None

    for i in range(len(rms)):
        if not in_hit and rms[i] > threshold:
            hit_start_idx = i
            in_hit = True
        elif in_hit and rms[i] <= threshold:
            hit_end_idx = i
            if hit_end_idx > hit_start_idx + 1:
                window = {
                    'start': times[hit_start_idx],
                    'end': times[hit_end_idx],
                    'amplitude_curve': rms[hit_start_idx:hit_end_idx+1].tolist()
                }
                hit_windows.append(window)
            in_hit = False

    print(f"Detected {len(hit_windows)} valid hit windows.")
    return hit_windows, times, sr


