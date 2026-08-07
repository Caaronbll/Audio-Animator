#!/usr/bin/env python3

from PIL import Image, ImageDraw


def chh_animation_logic(frame, width=1280, height=720):
    """Returns the closed hi-hat animation layer for one frame."""

    # Create a transparent layer for the instrument.
    animation_layer = Image.new(
        "RGBA",
        (width, height),
        (0, 0, 0, 0)
    )

    hit_status = frame["hit_status"]

    # Return an empty layer when no sound is present.
    if hit_status is None:
        return animation_layer

    average_amplitude = frame["average_amplitude"]
    max_amplitude = frame["max_amplitude"]

    radius_scale = 1.7

    # Determine the circle size from the frame amplitude.
    if average_amplitude < 0.1:
        radius = 0
    else:
        radius = max(
            int(max_amplitude * radius_scale),
            10
        )

    # Attacks are fully visible; decays fade with amplitude.
    if hit_status == "attack":
        alpha = 255
    else:
        alpha = int(max_amplitude * 10)

    center_x = width // 2
    center_y = height // 2

    draw = ImageDraw.Draw(animation_layer)

    draw.ellipse(
        (
            center_x - radius,
            center_y - radius,
            center_x + radius,
            center_y + radius
        ),
        fill=(207, 203, 37, alpha)
    )

    return animation_layer

