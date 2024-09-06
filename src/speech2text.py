import deepspeech
import numpy as np
import wave
import pyaudio

# Load the pre-trained DeepSpeech model
model_file_path = 'deepspeech-0.9.3-models.pbmm'
model = deepspeech.Model(model_file_path)
