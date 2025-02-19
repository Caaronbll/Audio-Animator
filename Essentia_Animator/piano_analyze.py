import essentia.standard as es
import numpy as np
import matplotlib.pyplot as plt

def analyze_piano_track(filename):
    # Load the audio file
    audio = es.MonoLoader(filename=filename)()
    
    # Extract pitch
    pitch_extractor = es.PredominantPitchMelodia()
    pitch_values, _ = pitch_extractor(audio)
    
    # Extract volume (RMS energy)
    rms = es.RMS()(audio)
    
    # Detect onsets (note start points)
    onsets = es.OnsetRate()(audio)
    
    # Plot pitch over time
    plt.figure(figsize=(10, 4))
    plt.plot(pitch_values, label='Pitch (Hz)')
    plt.xlabel('Time Frame')
    plt.ylabel('Frequency (Hz)')
    plt.title('Piano Pitch Analysis')
    plt.legend()
    plt.show()
    
    # Print extracted details
    print(f"Average RMS (Volume): {rms:.4f}")
    print(f"Estimated Onset Rate (Notes per second): {onsets:.2f}")
    
    return pitch_values, rms, onsets

# Example usage
if __name__ == "__main__":
    filename = "piano_track.wav"  # Replace with your actual file
    analyze_piano_track(filename)
