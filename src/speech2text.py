import deepspeech
import numpy as np
import wave
import pyaudio

# Load the pre-trained DeepSpeech model
model_file_path = 'deepspeech-0.9.3-models.pbmm'
model = deepspeech.Model(model_file_path)

def record_and_transcribe():
    chunk_size = 1024
    audio = pyaudio.PyAudio()

    stream = audio.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=chunk_size)
    print("Listening...")

    stream.start_stream()
    while True:
        audio_data = stream.read(chunk_size)
        np_audio = np.frombuffer(audio_data, np.int16)
        text = model.stt(np_audio)
        print(f"Transcription: {text}")

    stream.stop_stream()
    stream.close()
    audio.terminate()

record_and_transcribe()