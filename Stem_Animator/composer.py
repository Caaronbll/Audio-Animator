#!/usr/bin/env python3

import subprocess

from PIL import Image


class Composer:
    """Combines animation layers and renders the final video."""

    def __init__(
        self,
        animators,
        fps=60,
        width=1280,
        height=720
    ):
        self.animators = animators
        self.fps = fps
        self.width = width
        self.height = height


    def get_frame(self, frame_index):
        """Combines all animation layers for one frame."""

        final_frame = Image.new(
            "RGBA",
            (self.width, self.height),
            (0, 0, 0, 255)
        )

        # Request the same frame from each animator and composite its layer.
        for animator in self.animators:
            animation_layer = animator.get_animation(frame_index)

            if animation_layer is None:
                continue
                
            final_frame = Image.alpha_composite(
                final_frame,
                animation_layer
            )

        return final_frame.convert("RGB")


    def render_video(
        self,
        audio_path,
        filename="final_video.mp4"
    ):
        """Streams composed frames to FFmpeg and creates an MP4 video."""

        total_frames = min(
            len(animator.hit_data)
            for animator in self.animators
        )

        if total_frames == 0:
            raise ValueError(
                "No animation frames are available to render."
            )

        print(f"Animator count: {len(self.animators)}")
        print(f"Total frames to render: {total_frames}")

        for animator in self.animators:
            print(
                f"{animator.__class__.__name__}: "
                f"{len(animator.hit_data)} frames"
            )

        # Start FFmpeg and configure it to receive raw RGB frames.
        ffmpeg_process = subprocess.Popen(
            [
                "ffmpeg",
                "-y",

                # Raw video input from Python.
                "-f", "rawvideo",
                "-pix_fmt", "rgb24",
                "-s", f"{self.width}x{self.height}",
                "-r", str(self.fps),
                "-i", "-",

                # Audio input.
                "-i", audio_path,

                # Video encoding.
                "-c:v", "libx264",
                "-preset", "medium",
                "-pix_fmt", "yuv420p",

                # Audio encoding.
                "-c:a", "aac",
                "-b:a", "192k",

                # Improve MP4 playback compatibility.
                "-movflags", "+faststart",

                # Stop when the shorter input ends.
                "-shortest",

                filename
            ],
            stdin=subprocess.PIPE
        )

        try:
            # Create and write one completed frame at a time.
            for frame_index in range(total_frames):
                final_frame = self.get_frame(frame_index)

                ffmpeg_process.stdin.write(
                    final_frame.tobytes()
                )

        except BrokenPipeError as error:
            raise RuntimeError(
                "FFmpeg stopped before all frames were written."
            ) from error

        finally:
            if ffmpeg_process.stdin:
                ffmpeg_process.stdin.close()

        ffmpeg_process.wait()

        if ffmpeg_process.returncode != 0:
            raise RuntimeError(
                "FFmpeg failed to create the final video."
            )

        print(f"-Final video saved as {filename}")