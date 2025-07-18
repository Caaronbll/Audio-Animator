# ----- TITLE -----

# analyzer.py

# ----- IMPORTS -----

import librosa
import numpy as np



# FRAME DURATION TO FRAMES PER SECOND  
# fd 0.05     = 20 fps
# fd 0.025    = 40 fps
# fd 0.01667  = 60 fps



# ----- AUDIO ANALYZER CLASS -----

class AudioAnalyzer:
    def __init__(self, audio_path, frame_duration, threshold_ratio=0.15):
        """
        Initialize the analyzer.

        Parameters:
            audio_path (str): Path to the audio file.
            frame_duration (float): Time duration per frame in seconds.
            threshold_ratio (float): Threshold for detecting hits (ratio of max amplitude).
        """
        self.audio_path = audio_path
        self.frame_duration = frame_duration
        self.threshold_ratio = threshold_ratio

    # ----- USES LIBROSA TO GET HIT DATA -----
    def get_hits(self):
        """
        Analyze the audio and return information about detected hits.

        Returns:
            hit_data (list): List of dictionaries for each hit with:
                - 'amp_start' (float): RMS amplitude at hit start
                - 'amp_max' (float): Maximum amplitude during the hit
                - 'amp_data' (list): List of RMS values across hit
            times (np.ndarray): Array of time values for each frame
            sr (int): Sample rate
        """
        # Load audio (librosa)
        y, sr = librosa.load(self.audio_path, sr=None)
        print(f"Audio loaded. Sample rate: {sr} Hz")

        
        # Frame size setup
        frame_len = int(sr * self.frame_duration)
        rms = librosa.feature.rms(y=y, frame_length=frame_len, hop_length=frame_len)[0]
        times = librosa.frames_to_time(range(len(rms)), sr=sr, hop_length=frame_len)

        threshold = np.max(rms) * self.threshold_ratio

        # Detect hits
        hit_data = []
        in_hit = False
        start_idx = None

        for i in range(len(rms)):
            if not in_hit and rms[i] > threshold:
                start_idx = i
                in_hit = True
            elif in_hit and rms[i] <= threshold:
                end_idx = i
                if end_idx > start_idx + 1:
                    amp_curve = rms[start_idx:end_idx + 1]
                    #print(amp_curve)
                    hit_data.append({
                        'amp_start': float(amp_curve[0]),
                        'amp_max': float(np.max(amp_curve)),
                        'amp_data': amp_curve
                    })
                in_hit = False

        print(f"Detected {len(hit_data)} hit(s).")
        return hit_data, times


