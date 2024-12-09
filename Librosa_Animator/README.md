# Installing Librosa and Prerequisites

Welcome to the repository! This guide will help you install **Librosa**, a Python library for audio and music analysis, along with its necessary dependencies.

---

## System Requirements
Before installing Librosa, ensure you have the following prerequisites:
- Python 3.6 or newer
- Pip (Python's package installer)
- Access to a Linux-based system (or WSL for Windows)

---

## Installation Steps

### 1. Install System Dependencies
Librosa requires certain system libraries to handle audio processing effectively.

Run the following command to install the necessary system libraries:

```bash
sudo apt update
sudo apt install libsndfile1 ffmpeg -y
```

## Task 2: Install Librosa Using Pip

After installing the system dependencies, you can proceed with installing **Librosa** and its Python dependencies using the following command:

```bash
pip3 install librosa
```

## Task 3: Verify the Installation of Librosa

To confirm that Librosa has been installed successfully, confirm the version:

```bash
python3 -c "import librosa; print(librosa.__version__)"
```

If the installation was successful, the version of Librosa will be displayed in the terminal without any errors.