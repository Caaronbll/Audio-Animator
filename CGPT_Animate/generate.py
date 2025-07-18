# ----- TITLE -----

# generate.py

# ----- IMPORTS -----

from moviepy.editor import VideoClip, AudioFileClip
from PIL import Image, ImageDraw
import numpy as np


# standard 1280w, 720h 
# low fps, 20


# ----- GENERATE CLASS -----

class Generate:
    def __init__(self, audio_path, frame_duration):
        """
        Initialize the generator.

        Parameters:
            audio_path (str): Path to the audio file to be used in the final video.
            frame_duration (float): Duration of each frame (in seconds).
        """
        self.audio_path = audio_path
        self.frame_duration = frame_duration

    def draw_hh(self, hit_data):
        """
        Draws visuals for high-hat hits.

        Parameters:
            hit_data (list): List of hit dictionaries with amplitude data.
        """
        # (This method is intentionally left empty for now)
        print(hit_data)
