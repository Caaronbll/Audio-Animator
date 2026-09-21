#!/usr/bin/env python3

from piano_animation import piano_animation
from PIL import Image


class PianoAnimator:
    """Converts Piano MIDI data into frame-based animation layers."""

    def __init__(self, note_data, fps=60, width=1280, height=720):
        self.note_data = note_data
        self.fps = fps
        self.width = width
        self.height = height

        print("- Note data loaded to Piano Animator")

    def get_frame_data(self, frame_index):
        """Returns all notes active during the requested frame."""

        frame_data = []

        for note in self.note_data:
            if note["start_frame"] <= frame_index < note["end_frame"]:
                note_frame = frame_index - note["start_frame"]

                progress = (
                    note_frame / note["duration_frames"]
                )

                frame_data.append({
                    **note,
                    "note_frame": note_frame,
                    "progress": progress
                })

        return frame_data


    def get_animation(self, frame_index):
        """Returns the combined piano animation layer for one frame."""

        frame_data = self.get_frame_data(frame_index)

        if not frame_data:
            return None

        combined_layer = Image.new(
            "RGBA",
            (self.width, self.height),
            (0, 0, 0, 0)
        )

        animation_exists = False

        for note in frame_data:
            note_layer = piano_animation(
                note,
                self.width,
                self.height
            )

            if note_layer is not None:
                combined_layer = Image.alpha_composite(
                    combined_layer,
                    note_layer
                )
                animation_exists = True

        if not animation_exists:
            return None

        return combined_layer
