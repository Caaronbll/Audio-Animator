#!/usr/bin/env python3

from PIL import Image

from piano_animation import piano_animation


WIDTH = 1280
HEIGHT = 720

# The note data is not being used yet.
test_note = {
    "note_name": "C4"
}

light_layer = piano_animation(
    test_note,
    WIDTH,
    HEIGHT
)

background = Image.new(
    "RGBA",
    (WIDTH, HEIGHT),
    (0, 0, 0, 255)
)

test_image = Image.alpha_composite(
    background,
    light_layer
)

test_image.save("piano_light_test.png")

print("- Test image saved")