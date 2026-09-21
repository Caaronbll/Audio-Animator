#!/usr/bin/env python3

from PIL import Image, ImageDraw

NOTE_POSITIONS = {
    "A3": (480, 400), #
    "B3": (720, 400), #
    "C3": (640, 520),
    "D3": (640, 520),
    "E3": (400, 640), #
    "F3": (320, 560), #
    "G3": (560, 480), # 

    "A4": (480, 200), #
    "B4": (640, 360),
    "C4": (640, 320), #
    "D4": (640, 360),
    "E4": (640, 360),
    "F4": (720, 280), #
    "G4": (640, 240), #

    "A5": (640, 200),
    "B5": (720,  80), #
    "C5": (640, 200),
    "D5": (640, 200),
    "E5": (400, 240), #
    "F5": (320, 160), #
    "G5": (640, 120), #
}

def piano_animation(note, width=1280, height=720):
    """Creates a circular light-gradient layer for one piano note."""

    layer = Image.new(
        "RGBA",
        (width, height),
        (0, 0, 0, 0)
    )

    draw = ImageDraw.Draw(layer)
    
    center_x, center_y = NOTE_POSITIONS[
        note["note_name"]
    ]
    
    attack_frames = 3

    # Keep velocity within the valid MIDI range.
    velocity = max(1, min(note["velocity"], 80))

    # Scale the animation size from velocity.
    full_radius = velocity
    start_radius = max(1, int(full_radius / 7))
    decay_radius = max(1, int(full_radius * 1.7))

    # Scale brightness from 0.0 to 1.0.
    velocity_brightness = velocity / 80
    note_frame = note["note_frame"]
    duration_frames = note["duration_frames"]

    # Clamp pitch to the three-octave range.
    pitch = max(48, min(note["pitch"], 83))

    pitch_scale = (
        (pitch - 48) / (83 - 48)
    )

    # Low notes decay for 300 frames.
    # High notes decay for 120 frames.
    longest_decay = 300
    shortest_decay = 120

    natural_decay_frames = int(
        longest_decay
        - ((longest_decay - shortest_decay) * pitch_scale)
    )


    # Attack
    if note_frame < attack_frames:
        linear_progress = (
            note_frame / (attack_frames - 1)
        )

        attack_progress = linear_progress ** 1.5

        max_radius = int(
            start_radius
            + ((full_radius - start_radius) * attack_progress)
        )

        opacity = 1.0

    # Decay
    else:
        decay_frames = max(
            min(
                duration_frames - attack_frames,
                natural_decay_frames
            ),
            1
        )

        decay_note_frame = note_frame - attack_frames

        decay_progress = min(
            decay_note_frame / decay_frames,
            1.0
        )

        # Expand quickly at first, then gradually slow down.
        expansion_progress = (
            1 - ((1 - decay_progress) ** 1.5)
        )

        max_radius = int(
            full_radius
            + ((decay_radius - full_radius) * expansion_progress)
        )

        # Fade slowly.
        opacity = (1.0 - decay_progress) ** 0.8

    # Clamp the pitch to the three-octave range.
    pitch = max(48, min(note["pitch"], 83))

    pitch_scale = (
        (pitch - 48) / (83 - 48)
    )

    dark_blue = (15, 45, 110)
    light_blue = (175, 225, 255)

    color = tuple(
        int(dark + ((light - dark) * pitch_scale))
        for dark, light in zip(dark_blue, light_blue)
    )

    for radius in range(max_radius, 0, -1):
        alpha = int(
            255 * (1 - radius / max_radius) * opacity * velocity_brightness
        )

        draw.ellipse(
            (
                center_x - radius,
                center_y - radius,
                center_x + radius,
                center_y + radius
            ),
            fill=(*color, alpha)
        )

    return layer