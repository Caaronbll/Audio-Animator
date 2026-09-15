#!/usr/bin/env python3

from PIL import Image, ImageDraw


def piano_animation(note, width=1280, height=720):
    """Creates a circular light-gradient layer for one piano note."""

    layer = Image.new(
        "RGBA",
        (width, height),
        (0, 0, 0, 0)
    )

    draw = ImageDraw.Draw(layer)

    center_x = width // 2
    center_y = height // 2
    max_radius = 150

    for radius in range(max_radius, 0, -1):
        alpha = int(
            255 * (1 - radius / max_radius)
        )

        draw.ellipse(
            (
                center_x - radius,
                center_y - radius,
                center_x + radius,
                center_y + radius
            ),
            fill=(255, 255, 255, alpha)
        )

    return layer