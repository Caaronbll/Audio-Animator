# ----- IMPORTS -----
from analyzer import AudioAnalyzer
from generate import Generate


# ----- AUDIO FILES (STEMS) -----
audio_path_hh = './audio_files/hh_audio.wav'              # high-hats
audio_path_piano = './audio_files/piano_test.wav'         # piano


# ----- FRAME DURATION (FPS) -----
fd = 0.01667 # 60fps


# ----- ANALYZERS -----
hh_analyzer = AudioAnalyzer(audio_path_hh, fd, threshold_ratio=0.15)
piano_analyzer = AudioAnalyzer(audio_path_piano, fd, threshold_ratio=0.15)

# ----- VIDEO GENERATION ----- 
generate = Generate(audio_path_piano, fd)

if hh_analyzer and piano_analyzer and generate:
    print('Classes created')

# Analyze high-hat hits
hit_data = piano_analyzer.get_hits()
hits_amp_data, times = hit_data

generate.draw_hh(hits_amp_data)

 
