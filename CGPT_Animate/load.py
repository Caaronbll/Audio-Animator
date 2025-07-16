import librosa
import numpy as np


class AudioAnalyzer:
    def __init__(self, frame_duration=0.05, threshold_ratio=0.37):
        """
        Initialize with frame analysis settings.
        
        Parameters:
            frame_duration (float): Duration of each frame in seconds.
            threshold_ratio (float): Percentage of max RMS to trigger a hit.
        """
        self.frame_duration = frame_duration
        self.threshold_ratio = threshold_ratio

    def analyze_hh(self, audio_path):
        """
        Analyze a high-hat (or percussive) track for amplitude-based hits.

        Parameters:
            audio_path (str): Path to the audio file.

        Returns:
            hit_windows (list): List of dicts with hit timing and amplitude curve
            times (np.ndarray): Time stamps for each RMS frame
            sr (int): Sample rate of the audio
        """
        y, sr = librosa.load(audio_path, sr=None)
        print(f"Audio loaded. Sample rate: {sr} Hz")
        print(f"Audio duration: {len(y)/sr:.2f} seconds")

        frame_length = int(sr * self.frame_duration)
        rms = librosa.feature.rms(y=y, frame_length=frame_length, hop_length=frame_length)[0]
        times = librosa.frames_to_time(range(len(rms)), sr=sr, hop_length=frame_length)
        threshold = np.max(rms) * self.threshold_ratio

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
                    amp_curve = rms[hit_start_idx:hit_end_idx+1]
                    peak_idx = np.argmax(amp_curve)
                    window = {
                        'start': times[hit_start_idx],
                        'end': times[hit_end_idx],
                        'peak_time': times[hit_start_idx + peak_idx],
                        'peak_amplitude': amp_curve[peak_idx],
                        'amplitude_curve': amp_curve.tolist()
                    }
                    hit_windows.append(window)
                in_hit = False

        print(f"Detected {len(hit_windows)} valid high-hat hit windows.")
        return hit_windows, times, sr


