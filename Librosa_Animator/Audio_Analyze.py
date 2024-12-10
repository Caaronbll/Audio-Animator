#!/usr/bin/env python3

import numpy as np 
import pandas as pd
import matplotlib.pylab as plt
import librosa
import librosa.display
print(librosa.__version__) # print version

audio_path = 'Pj.mp3'
y, sr = librosa.load(audio_path, sr=22050) # sr = sample rate(Hz)
print(y[:300])

