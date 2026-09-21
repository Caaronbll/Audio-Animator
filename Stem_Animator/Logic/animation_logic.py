#!/usr/bin/env python3

from PIL import Image, ImageDraw


def chh_animation_logic(frame, width=1280, height=720):
    """Returns a CHH layer, or None when no hit is active."""

    hit_status = frame["hit_status"]

    if hit_status is None:
        return None

    animation_layer = Image.new(
        "RGBA",
        (width, height),
        (0, 0, 0, 0)
    )

    center_x = width // 2
    center_y = height // 2

    radius = int(frame["max_amp"] * 2)
    radius = min(radius, 80) 
    if radius < 5:
        return None
    

    draw = ImageDraw.Draw(animation_layer)

    draw.ellipse(
        (
            center_x - radius,
            center_y - radius,
            center_x + radius,
            center_y + radius
        ),
        fill=(229, 235, 130, 250)
    )

    return animation_layer



def ohh_animation_logic(frame, width=1280, height=720):
    """Returns an OHH layer, or None when no hit is active."""

    if frame["hit_status"] is None:
        return None

    animation_layer = Image.new(
        "RGBA",
        (width, height),
        (0, 0, 0, 0)
    )

    draw = ImageDraw.Draw(animation_layer)

    center_x = width // 2
    center_y = height // 2

    radius = int(frame["sum_amp"]) * 1.2 * 1.3
    alpha = int(frame["alpha"] * 0.7)

    draw.ellipse(
        (
            center_x - radius,
            center_y - radius,
            center_x + radius,
            center_y + radius
        ),
        fill=(229, 235, 130, alpha)
    )

    return animation_layer


def shaker_animation_logic(frame, width=1280, height=720):
    """Returns an Shaker layer, or None when no hit is active."""

    if frame["hit_status"] is None:
        return None

    animation_layer = Image.new(
        "RGBA",
        (width, height),
        (0, 0, 0, 0)
    )

    draw = ImageDraw.Draw(animation_layer)

    center_x = width // 2
    center_y = height // 2

    rms_amp = min(max(frame["rms_amp"], 1), 18)
    alpha = frame["alpha"]
    radius = 80

    draw.ellipse(
        (
            center_x - radius,
            center_y - radius,
            center_x + radius,
            center_y + radius
        ),
        fill=(178, 211, 242, alpha)
    )

    return animation_layer


def clap_animation_logic(frame, width=1280, height=720):
    """Returns an Clap layer, or None when no hit is active."""

    if frame["hit_status"] is None:
        return None

    animation_layer = Image.new(
        "RGBA",
        (width, height),
        (0, 0, 0, 0)
    )

    draw = ImageDraw.Draw(animation_layer)

    max_amp = min(max(frame["max_amp"], 0), 100)
    alpha = int((max_amp / 100) * 170)

    draw.rectangle(
        (0, 0, width, height),
        fill=(189, 171, 98, alpha)
    )

    return animation_layer


def pad_animation_logic(frame, width=1280, height=720):
    """Returns a centered pad animation layer."""

    rms_amp = max(0, min(frame["rms_amp"], 10))
    max_amp = max(10, min(frame["max_amp"], 50))

    alpha = int(
    20 + ((max_amp - 10) / 40) * 140
)

    min_oval_width = 0
    max_oval_width = width * (2 / 3)

    oval_width = min_oval_width + (
        (rms_amp / 10) * (max_oval_width - min_oval_width)
    )

    oval_height = oval_width * (9 / 16)

    center_x = width / 2
    center_y = height / 2

    left = center_x - (oval_width / 2)
    top = center_y - (oval_height / 2)
    right = center_x + (oval_width / 2)
    bottom = center_y + (oval_height / 2)

    animation_layer = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(animation_layer)

    draw.ellipse(
        (left, top, right, bottom),
        fill=(0, 0, 230, alpha)
    )

    return animation_layer

    