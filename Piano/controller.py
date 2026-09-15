#!/usr/bin/env python3

from analyzer_midi import AnalyzerMIDI
from animator_piano import PianoAnimator

# Application settings
BPM = 112
FPS = 60
WIDTH = 1280
HEIGHT = 720

# File paths
PIANO_AUDIO_PATH = "./Files/piano_audio.mp3"
PIANO_MIDI_PATH = "./Files/piano_midi.mid"


def main():


    """ Analyzer """
    piano_analyzer = AnalyzerMIDI(
        PIANO_MIDI_PATH,
        BPM,
        FPS
    )

    piano_note_data = piano_analyzer.note_data
    print(piano_note_data[:10])

    """ Animator """
    piano_animator = PianoAnimator(
        piano_note_data,
        FPS,
        WIDTH,
        HEIGHT,
    )

    piano_frame_data = piano_animator.get_frame_data(1)
    print(piano_frame_data[:10])


if __name__ == "__main__":
    main()

