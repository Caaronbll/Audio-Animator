
from analyzer import AudioAnalyzer

# Set path to your high-hat audio file
audio_path = './audio_files/hh_audio.wav'

# Create an instance of the analyzer (60fps)
analyzer = AudioAnalyzer(frame_duration=0.05, threshold_ratio=0.15)

# Analyze high-hat hits
hit_data = analyzer.get_hits(audio_path)
hits = hit_data[0]
print(hits)
for hit in hits:
    print(hit['amp'])


 
