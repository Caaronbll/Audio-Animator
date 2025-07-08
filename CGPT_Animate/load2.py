import librosa
import numpy as np

def analyze_hits(audio_path, frame_duration=0.05, threshold_ratio=0.37):
    """
    Load audio and return hit window data for visual syncing.

    Parameters:
        audio_path (str): Path to the audio file.
        frame_duration (float): Duration of each frame (in seconds).
        threshold_ratio (float): % of max amplitude used as threshold (0–1).

    Returns:
        hit_windows (list): List of {'start', 'end', 'amplitude_curve'} dicts
        times (np.ndarray): Time stamps for each RMS frame
        sr (int): Sample rate of the audio
    """
    # Load audio
    y, sr = librosa.load(audio_path, sr=None)
    print(f"Audio loaded. Sample rate: {sr} Hz")
    print(f"Audio duration: {len(y)/sr:.2f} seconds")

    # Analyze amplitude
    frame_length = int(sr * frame_duration)
    rms = librosa.feature.rms(y=y, frame_length=frame_length, hop_length=frame_length)[0]
    times = librosa.frames_to_time(range(len(rms)), sr=sr, hop_length=frame_length)
    threshold = np.max(rms) * threshold_ratio

    # Detect hit and release windows
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

    print(f"Detected {len(hit_windows)} valid high-hat hit windows.")
    return hit_windows, times, sr

