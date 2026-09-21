#!/usr/bin/env python3

import pretty_midi

class AnalyzerMIDI:
    """Converts a MIDI file into frame-based note data."""

    def __init__(self, midi_path, bpm, fps=60):
        self.midi_path = midi_path
        self.bpm = bpm
        self.fps = fps

        # Load the MIDI file.
        self.midi_data = pretty_midi.PrettyMIDI(self.midi_path)

        if self.midi_data:
            print("- MIDI Data Loaded")

        self.note_data = self.get_note_data()
        self.add_frames()

        # The original MIDI data is no longer needed.
        self.midi_data = None

        

    def get_note_data(self):
        """Extracts note data from every MIDI instrument track."""

        note_data = []

        for instrument in self.midi_data.instruments:
            for note in instrument.notes:
                note_data.append({
                    "pitch": note.pitch,
                    "note_name": pretty_midi.note_number_to_name(note.pitch),
                    "velocity": note.velocity,
                    "start_time": note.start,
                    "end_time": note.end
                })

        note_data.sort(key=lambda note: note["start_time"])

        return note_data

    def add_frames(self):
        """Adds frame timing data to each MIDI note."""

        for note in self.note_data:
            note["start_frame"] = round(
                note["start_time"] * self.fps
            )

            note["end_frame"] = round(
                note["end_time"] * self.fps
            )

            note["duration_frames"] = (
            note["end_frame"] - note["start_frame"]
            )

