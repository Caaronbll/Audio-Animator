#!/usr/bin/env python3

import essentia.standard as es
import numpy as np


class Analyzer:
    """Converts an audio file into frame-based audio data."""

    def __init__(self, audio_path, bpm, fps=60):
        self.sample_rate = 44100
        self.bpm = bpm
        self.fps = fps
        self.samples_per_frame = int(self.sample_rate / self.fps)

        # Load the audio as a mono signal.
        loader = es.MonoLoader(
            filename=audio_path,
            sampleRate=self.sample_rate
        )
        self.audio = loader()

        # Store basic timing and sample information.
        self.total_samples = len(self.audio)
        self.length_seconds = self.total_samples / self.sample_rate
        self.beat_length = 60 / self.bpm
        self.total_beats = self.length_seconds / self.beat_length
        self.total_measures = self.total_beats / 4

        # Create, scale, and normalize the amplitude envelope.
        self.amplitude_envelope = np.abs(self.audio)
        self.amplitude_envelope *= 100
        self.amplitude_envelope **= 2

        max_amplitude = np.max(self.amplitude_envelope)

        if max_amplitude > 0:
            self.amplitude_envelope = (
                self.amplitude_envelope / max_amplitude
            ) * 100

        self.audio_data = []

        print("-Audio loaded to Analyzer")



    def clear_unneeded(self):
        """Releases sample-level data after frame analysis."""

        self.audio = None
        self.amplitude_envelope = None



    def get_audio_data(self):
        """Returns max, average, and RMS amplitude values for each frame."""

        self.audio_data.clear()

        for start_sample in range(0, len(self.amplitude_envelope), self.samples_per_frame):

            end_sample = start_sample + self.samples_per_frame

            frame_samples = self.amplitude_envelope[
                start_sample:end_sample
            ]

            frame = {
                "frame": len(self.audio_data) + 1,
                "max_amp": round(float(np.max(frame_samples)), 2),
                "avg_amp": round(float(np.mean(frame_samples)),2),
                "rms_amp": round(float(np.sqrt(np.mean(frame_samples ** 2))),2)
            }

            self.audio_data.append(frame)

        self.clear_unneeded()

        print("-Retrieved audio data and cleared analysis memory")

        return self.audio_data



    def print_sample_info(self):
        """Prints information about the loaded audio file."""

        total_frames = (
            self.total_samples // self.samples_per_frame
        )

        print("\n--- SAMPLE INFORMATION ---")
        print(f"Audio Length   : {self.length_seconds:.3f} seconds")
        print(f"Sample Rate    : {self.sample_rate} Hz")
        print(f"Total Samples  : {self.total_samples}")
        print(f"Beats/Minute*  : {self.bpm}")
        print(f"Total Beats    : {self.total_beats}")
        print(f"Total Measures : {self.total_measures}")
        print(f"Frames/Second* : {self.fps}")
        print(f"Total Frames   : {total_frames}")
        print(f"Samples/Frame  : {self.samples_per_frame}")
        print("(*=given)\n")
