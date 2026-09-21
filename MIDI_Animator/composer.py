#!/usr/bin/env python3

import subprocess

from PIL import Image


class Composer:
    """Renders piano animation layers into a video."""

    def __init__(
        self,
        animator,
        fps=60,
        width=1280,
        height=720
    ):
        self.animator = animator
        self.fps = fps
        self.width = width
        self.height = height

        self.total_frames = max(
            note["end_frame"]
            for note in self.animator.note_data
        )

    def render_video(self, audio_path, output_path):
        """Renders the piano animation with its audio."""

        command = [
            "ffmpeg",
            "-y",
            "-f", "rawvideo",
            "-pixel_format", "rgb24",
            "-video_size", f"{self.width}x{self.height}",
            "-framerate", str(self.fps),
            "-i", "-",
            "-i", audio_path,
            "-c:v", "libx264",
            "-pix_fmt", "yuv420p",
            "-c:a", "aac",
            "-shortest",
            output_path
        ]

        process = subprocess.Popen(
            command,
            stdin=subprocess.PIPE
        )

        for frame_index in range(self.total_frames):
            frame = Image.new(
                "RGBA",
                (self.width, self.height),
                (0, 0, 0, 255)
            )

            animation_layer = self.animator.get_animation(
                frame_index
            )

            if animation_layer:
                frame = Image.alpha_composite(
                    frame,
                    animation_layer
                )


            process.stdin.write(
                frame.convert("RGB").tobytes()
            )

        process.stdin.close()
        return_code = process.wait()

        if return_code != 0:
            raise RuntimeError("FFmpeg failed to render the video.")

        print(f"- Video rendered to {output_path}")