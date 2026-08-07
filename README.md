# Audio Animator

Audio Animator is a Python project that turns prerecorded musical audio stems into synchronized visual animations.

The project analyzes audio frame by frame, converts the extracted data into instrument-specific animation layers, and combines those layers into a final video.


## Current Architecture

```text
Audio stem
    |
    v
Analyzer
    |
    v
Frame-by-frame audio data
    |
    +--> ClosedHihatAnimator
    +--> OpenHihatAnimator
    +--> Future instrument animators
              |
              v
           Composer
              |
              v
         Final video
```

### Analyzer

The analyzer loads a prerecorded audio stem and divides it into frames based on the selected frames-per-second value.

Each frame can contain data such as:

- Maximum amplitude
- Average amplitude
- Hit status
- Frame number

The analyzer is intended to remain reusable across different instruments.

### Animators

Each instrument animator interprets the analyzer data differently.

Current instrument classes include:

- `ClosedHihatAnimator`
- `OpenHihatAnimator`

Instrument-specific behavior, such as radius, transparency, attack, decay, and visual thresholds, belongs inside the relevant animator.

### Composer

The composer combines transparent animation layers over a black background and renders the frames into a video synchronized with the original audio.

## Project Structure

The exact structure may change as the project develops, but the main files are:

```text
Audio-Animator/
├── analyzer.py
├── animator_chh.py
├── animator_ohh.py
├── composer.py
├── controller.py
├── requirements.txt
├── README.md
└── Audio_files/
    └── stems/
```

Generated JSON data, preview videos, virtual environments, and cache files should not be committed to the repository.

## Requirements

- Python 3
- FFmpeg
- NumPy
- Essentia
- Pillow

Python packages can be installed with:

```bash
pip install -r requirements.txt
```

FFmpeg must be installed separately and available from the terminal.

To confirm that FFmpeg is installed:

```bash
ffmpeg -version
```

## Running the Project

Place the required audio files or stems in the paths configured inside `controller.py`.

Then run:

```bash
python3 controller.py
```

The controller coordinates the analyzer, instrument animators, and composer.

## Current Status

The project currently has a working frame-based audio-analysis and animation pipeline focused on closed and open hi-hats.

The next major milestone is combining multiple instrument layers through the composer and then expanding the system to instruments such as snare and piano.

## Future Development

Planned areas of development include:

- Additional drum animators
- Pitch-aware melodic animations
- Instrument-specific color and shade mapping
- Improved glow and gradient effects
- More reusable animator interfaces
- MIDI-based visualization
- Expanded audio features such as RMS and spectral data

## Project Scope

Audio Animator is designed for prerecorded musical audio, individual stems, and MIDI-based visualization. It is not intended for microphone input or voice analysis.
