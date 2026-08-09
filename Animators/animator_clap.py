#!/usr/bin/env python3

import copy
import json

from Logic.animation_logic import clap_animation_logic
from Logic.hit_logic import clap_hit_logic


class ClapAnimator:
    """Converts clap audio data into frame-based animation layers."""

    def __init__(
        self,
        audio_data,
        fps=60,
        width=1280,
        height=720
    ):
        self.audio_data = audio_data
        self.fps = fps
        self.width = width
        self.height = height

        # Convert the analyzer output into closed hi-hat hit data.
        self.hit_data = self.get_hit_data()

        # The original dataset is no longer needed after hit processing.
        self.audio_data = None

        print("-Audio data loaded to Clap Animator")


    def get_hit_data(self):
        """Converts audio data to hit data by adding hit detection."""

        hit_data = copy.deepcopy(self.audio_data)

        return clap_hit_logic(hit_data)


    def get_animation(self, frame_index):
        """Returns the animation layer for one frame."""

        frame = self.hit_data[frame_index]

        return clap_animation_logic(
            frame,
            self.width,
            self.height
        )


    def print_json(self, filename):
        """Saves the processed hit data to a JSON file."""

        json_data = {
            "frames": self.hit_data
        }

        with open(filename, "w") as file:
            json.dump(json_data, file, indent=4)

        print(f"Hit data saved to {filename}")

