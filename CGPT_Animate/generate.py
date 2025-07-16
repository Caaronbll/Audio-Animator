# test_analyzer.py

from load import AudioAnalyzer  # Replace with actual module name if needed

# Path to your test .wav file
audio_path = "./audio_files/hh_audio.wav"

# Create an instance of the analyzer
analyzer = AudioAnalyzer(frame_duration=0.05, threshold_ratio=0.37)

# Analyze the file using the method for high-hats
hit_windows, times, sr = analyzer.analyze_hh(audio_path)

# Print out some of the returned data
print(f"\nSample rate: {sr}")
print(f"Total hit windows detected: {len(hit_windows)}")
print("First few hit windows:")
for i, hit in enumerate(hit_windows[:3]):
    print(f"  Hit {i+1}: start={hit['start']:.2f}s, peak={hit['peak_amplitude']:.4f}, duration={hit['end'] - hit['start']:.2f}s")
