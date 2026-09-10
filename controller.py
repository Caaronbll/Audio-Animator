#!/usr/bin/env python3

from analyzer_d import Analyzer_d
from Animators.animator_chh import ClosedHihatAnimator
from Animators.animator_ohh import OpenHihatAnimator
from Animators.animator_shaker import ShakerAnimator
from Animators.animator_clap import ClapAnimator
from composer import Composer


# Application settings
BPM = 90
FPS = 60
WIDTH = 1280
HEIGHT = 720

# File paths
CHH_AUDIO_PATH = "./Audio_files/stems/CHH.wav"
OHH_AUDIO_PATH = "./Audio_files/stems/OHH.wav"
SHAKER_AUDIO_PATH = "./Audio_files/stems/Shaker.wav"
CLAP_AUDIO_PATH = "./Audio_files/stems/Clap.wav"

MASTER_AUDIO_PATH = "./Audio_files/tester_logic_file copy.mp3"
VIDEO_OUTPUT_PATH = "final_video.mp4"

JSON_OUTPUT_PATH = "_data.json"




def main():
    """Analyzes audio, creates animations, and renders the final video."""


    """ Analyzer """
    chh_analyzer = Analyzer_d(
        CHH_AUDIO_PATH,
        BPM,
        FPS
    )
    
    ohh_analyzer = Analyzer_d(
        OHH_AUDIO_PATH,
        BPM,
        FPS
    )

    shaker_analyzer = Analyzer_d(
        SHAKER_AUDIO_PATH,
        BPM,
        FPS
    )

    clap_analyzer = Analyzer_d(
        CLAP_AUDIO_PATH,
        BPM,
        FPS
    )
    
    # Get Audio Data
    chh_audio_data = chh_analyzer.get_audio_data()
    ohh_audio_data = ohh_analyzer.get_audio_data()
    shaker_audio_data = shaker_analyzer.get_audio_data()
    clap_audio_data = clap_analyzer.get_audio_data()
    

    """ Animator """
    chh_animator = ClosedHihatAnimator(
        chh_audio_data,
        FPS,
        WIDTH,
        HEIGHT
    )
   
    ohh_animator = OpenHihatAnimator(
        ohh_audio_data,
        FPS,
        WIDTH,
        HEIGHT
    )

    shaker_animator = ShakerAnimator(
        shaker_audio_data,
        FPS,
        WIDTH,
        HEIGHT
    )

    clap_animator = ClapAnimator(
        clap_audio_data,
        FPS,
        WIDTH,
        HEIGHT
    )
    
    # print JSON
    #chh_animator.print_json("CHH_hit_data.json")
    #ohh_animator.print_json("OHH_hit_data.json")
    #shaker_animator.print_json("SHAKER_hit_data.json")
    #clap_animator.print_json("CLAP_hit_data.json")


    # ---            --- #
    ANIMATORS = [
        chh_animator,
        ohh_animator,
        shaker_animator,
        clap_animator,
    ]
    # ---            --- #


    """ Composer """
    composer = Composer(
        ANIMATORS,
        FPS,
        WIDTH,
        HEIGHT
    )

    # Render
    composer.render_video(
        MASTER_AUDIO_PATH,
        VIDEO_OUTPUT_PATH
    )


if __name__ == "__main__":
    main()

