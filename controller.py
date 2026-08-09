#!/usr/bin/env python3

from analyzer import Analyzer
from Animators.animator_chh import ClosedHihatAnimator
from Animators.animator_ohh import OpenHihatAnimator
from composer import Composer


# Application settings
BPM = 90
FPS = 60
WIDTH = 1280
HEIGHT = 720

CHH_AUDIO_PATH = "./Audio_files/stems/hh.wav"
OHH_AUDIO_PATH = "./Audio_files/stems/OHh.wav"
FINAL_AUDIO_PATH = "./Audio_files/tester_logic_file copy.mp3"

JSON_OUTPUT_PATH = "CHH_data.json"
VIDEO_OUTPUT_PATH = "final_video.mp4"



def main():
    """Analyzes audio, creates animations, and renders the final video."""


    """ Analyzer """
    chh_analyzer = Analyzer(
        CHH_AUDIO_PATH,
        BPM,
        FPS
    )
    chh_audio_data = chh_analyzer.get_audio_data()

    ohh_analyzer = Analyzer(
        OHH_AUDIO_PATH,
        BPM,
        FPS
    )
    ohh_audio_data = ohh_analyzer.get_audio_data()


    """ Animator """
    chh_animator = ClosedHihatAnimator(
        chh_audio_data,
        FPS,
        WIDTH,
        HEIGHT
    )
    #chh_animator.print_json("CHH_hit_data.json")

    ohh_animator = OpenHihatAnimator(
        ohh_audio_data,
        FPS,
        WIDTH,
        HEIGHT
    )
    ohh_animator.print_json("OHH_hit_data.json")


    # ---                  --- #
    ANIMATORS = [
        chh_animator,
        ohh_animator
    ]
    # ---                  --- #


    """ Composer """
    composer = Composer(
        ANIMATORS,
        FPS,
        WIDTH,
        HEIGHT
    )

    # Render
    composer.render_video(
        FINAL_AUDIO_PATH,
        VIDEO_OUTPUT_PATH
    )


if __name__ == "__main__":
    main()

