#!/usr/bin/env python3


def chh_hit_logic(hit_data):
    """Adds closed hi-hat hit-status values to each frame."""

    for index, frame in enumerate(hit_data):
        current_amplitude = frame["max_amplitude"]

        # Mark frames with no amplitude as silence.
        if current_amplitude == 0:
            frame["hit_status"] = None
            continue

        # Mark the first non-silent frame as an attack.
        if index == 0 and current_amplitude != 0:
            frame["hit_status"] = "attack"
            continue

        previous_amplitude = hit_data[
            index - 1
        ]["max_amplitude"]

        # Increasing amplitude indicates a new attack.
        if (
            current_amplitude > previous_amplitude
            and current_amplitude > 1
        ):
            frame["hit_status"] = "attack"
        else:
            frame["hit_status"] = "decay"

    return hit_data


def ohh_hit_logic(hit_data):
    """Adds open hi-hat hit-status values to each frame."""

    for index, frame in enumerate(hit_data):
        current_amplitude = frame["max_amplitude"]

        # Mark frames with no amplitude as silence.
        if current_amplitude == 0:
            frame["hit_status"] = None
            continue

        # Mark the first non-silent frame as an attack.
        if index == 0 and current_amplitude != 0:
            frame["hit_status"] = "attack"
            continue

        previous_amplitude = hit_data[
            index - 1
        ]["max_amplitude"]

        # Increasing amplitude indicates a new attack.
        if (
            current_amplitude > previous_amplitude
            and current_amplitude > 1
        ):
            frame["hit_status"] = "attack"
        else:
            frame["hit_status"] = "decay"

    return hit_data


def shaker_hit_logic(hit_data):
    """Adds shaker hit-status values to each frame."""

    for index, frame in enumerate(hit_data):
        current_amplitude = frame["max_amplitude"]

        # Mark frames with no amplitude as silence.
        if current_amplitude == 0:
            frame["hit_status"] = None
            continue

        # Mark the first non-silent frame as an attack.
        if index == 0 and current_amplitude != 0:
            frame["hit_status"] = "attack"
            continue

        previous_amplitude = hit_data[
            index - 1
        ]["max_amplitude"]

        # Increasing amplitude indicates a new attack.
        if (
            current_amplitude > previous_amplitude
            and current_amplitude > 1
        ):
            frame["hit_status"] = "attack"
        else:
            frame["hit_status"] = "decay"

    return hit_data


def clap_hit_logic(hit_data):
    """Adds clap hit-status values to each frame."""

    for index, frame in enumerate(hit_data):
        current_amplitude = frame["max_amplitude"]

        # Mark frames with no amplitude as silence.
        if current_amplitude == 0:
            frame["hit_status"] = None
            continue

        # Mark the first non-silent frame as an attack.
        if index == 0 and current_amplitude != 0:
            frame["hit_status"] = "attack"
            continue

        previous_amplitude = hit_data[
            index - 1
        ]["max_amplitude"]

        # Increasing amplitude indicates a new attack.
        if (
            current_amplitude > previous_amplitude
            and current_amplitude > 1
        ):
            frame["hit_status"] = "attack"
        else:
            frame["hit_status"] = "decay"

    return hit_data