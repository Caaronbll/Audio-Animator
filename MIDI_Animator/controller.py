#!/usr/bin/env python3

from analyzer_midi import AnalyzerMIDI
from animator_piano import PianoAnimator
from composer import Composer


# Application settings
BPM = 112
FPS = 60
WIDTH = 1280
HEIGHT = 720

# File paths
PIANO_AUDIO_PATH = "./Files/piano_audio.mp3"
PIANO_MIDI_PATH = "./Files/piano_midi.mid"
VIDEO_OUTPUT_PATH = "piano.mp4"


def main():

    """Analyzer"""

    piano_analyzer = AnalyzerMIDI(
        PIANO_MIDI_PATH,
        BPM,
        FPS
    )

    """Animator"""
    
    piano_animator = PianoAnimator(
        piano_analyzer.note_data,
        FPS,
        WIDTH,
        HEIGHT
    )
    
    """Composer"""
    
    composer = Composer(
        piano_animator,
        FPS,
        WIDTH,
        HEIGHT
    )

    composer.render_video(
        PIANO_AUDIO_PATH,
        VIDEO_OUTPUT_PATH
    )
    

if __name__ == "__main__":
    main()

