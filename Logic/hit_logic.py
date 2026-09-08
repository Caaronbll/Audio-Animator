#!/usr/bin/env python3


def chh_hit_logic(hit_data):
    """Adds closed hi-hat hit-status values to each frame."""

    decay_count = 0

    for index, frame in enumerate(hit_data):
        current_amplitude = frame["max_amp"]

        # Mark frames with no amplitude as silence.
        if current_amplitude == 0:
            frame["hit_status"] = None
            decay_count = 0
            continue

        # Mark the first non-silent frame as an attack.
        if index == 0 and current_amplitude != 0:
            frame["hit_status"] = "attack"
            decay_count = 0
            continue

        previous_amplitude = hit_data[index - 1]["max_amp"]

        # Increasing amplitude indicates a new attack.
        if (
            current_amplitude > previous_amplitude
            and current_amplitude > 1
        ):
            frame["hit_status"] = "attack"
            decay_count = 0
        else:
            decay_count += 1
            frame["hit_status"] = "decay"
            frame["decay_frame"] = decay_count

    return hit_data


def ohh_hit_logic(hit_data):
    """Adds open hi-hat hit-status values to each frame."""

    for index, frame in enumerate(hit_data):
        current_amplitude = frame["max_amp"]

        # Mark frames with no amplitude as silence.
        if current_amplitude == 0:
            frame["hit_status"] = None
            continue

        # Mark the first non-silent frame as an attack.
        if index == 0 and current_amplitude != 0:
            frame["hit_status"] = "attack"
            continue

        previous_frame = hit_data[index - 1]
        previous_amplitude = previous_frame["max_amp"]
        

        # Increasing amplitude indicates a new attack.
        if (
            current_amplitude > previous_amplitude
            and current_amplitude > 1
        ):
            frame["hit_status"] = "attack"
        else:
            frame["hit_status"] = "decay"


        if previous_frame["hit_status"] is None:
            frame["sum_amp"] = current_amplitude
            frame["alpha"] = 160
        # Continue the existing sum.
        else:
            frame["sum_amp"] = (
                previous_frame["sum_amp"]
                + round(current_amplitude / 10)
            )
            if frame["max_amp"] < 5:
                frame["sum_amp"] = frame["sum_amp"] + 2
            frame["alpha"] = max(
                0,
                previous_frame["alpha"] - 6
            )

    return hit_data


def shaker_hit_logic(hit_data):
    """Adds shaker hit-status values to each frame."""

    for index, frame in enumerate(hit_data):
        current_amplitude = frame["max_amp"]

        # Mark frames with no amplitude as silence.
        if current_amplitude == 0:
            frame["hit_status"] = None
            continue

        # Mark the first non-silent frame as an attack.
        if index == 0 and current_amplitude != 0:
            frame["hit_status"] = "attack"
            continue

        previous_frame = hit_data[index - 1]
        previous_amplitude = previous_frame["max_amp"]

        # Increasing amplitude indicates a new attack.
        if (
            current_amplitude > previous_amplitude
            and current_amplitude > 1
        ):
            frame["hit_status"] = "attack"
        else:
            frame["hit_status"] = "decay"

        if previous_frame["hit_status"] is None and frame["hit_status"] == "attack":
            frame["alpha"] = max(int(current_amplitude * 2.2), 80)
        elif frame["hit_status"]:
            frame["alpha"] = max(0, previous_frame["alpha"] - 8)
        

    return hit_data


def clap_hit_logic(hit_data):
    """Adds clap hit-status values and cumulative average amplitude."""

    for index, frame in enumerate(hit_data):
        current_amplitude = frame["max_amp"]

        # Mark the first non-silent frame as an attack.
        if index == 0 and current_amplitude != 0:
            frame["hit_status"] = "attack"
            
            continue

        # Silence resets the cumulative value.
        if current_amplitude == 0:
            frame["hit_status"] = None
            continue

        prev_amplitude = hit_data[
            index - 1
        ]["max_amp"]

        # Increasing amplitude indicates a new attack.
        if (
            current_amplitude > prev_amplitude
            and current_amplitude > 1
        ):
            frame["hit_status"] = "attack"

        else:
            frame["hit_status"] = "decay"

    return hit_data