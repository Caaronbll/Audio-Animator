#!/usr/bin/env python3

from analyzer import Analyzer
from animator_chh import ClosedHihatAnimator
from composer import Composer


# Application settings
BPM = 90
FPS = 60
WIDTH = 1280
HEIGHT = 720

CHH_AUDIO_PATH = "./Audio_files/stems/hh.wav"
FINAL_AUDIO_PATH = "./Audio_files/tester_logic_file copy.mp3"

JSON_OUTPUT_PATH = "CHH_data.json"
VIDEO_OUTPUT_PATH = "final_video.mp4"


def main():
    """Analyzes audio, creates animations, and renders the final video."""

    chh_analyzer = Analyzer(
        CHH_AUDIO_PATH,
        BPM,
        FPS
    )

    chh_audio_data = chh_analyzer.get_audio_data()

    chh_animator = ClosedHihatAnimator(
        chh_audio_data,
        FPS,
        WIDTH,
        HEIGHT
    )

    composer = Composer(
        [chh_animator],
        FPS,
        WIDTH,
        HEIGHT
    )

    composer.render_video(
        FINAL_AUDIO_PATH,
        VIDEO_OUTPUT_PATH
    )


if __name__ == "__main__":
    main()

