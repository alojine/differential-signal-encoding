import numpy as np
from scipy.io import wavfile
import sounddevice as sd
import os

# Define the project folder for storing encoded and decoded files
PROJECT_FOLDER = "audio_samples"

if not os.path.exists(PROJECT_FOLDER):
    os.makedirs(PROJECT_FOLDER)

def differential_encoding(signal):
    return np.diff(signal, prepend=0)

def differential_decoding(encoded_signal):
    return np.cumsum(encoded_signal)

def encode_audio_file(input_path):
    sample_rate, signal = wavfile.read(input_path)
    
    if signal.ndim > 1:
        signal = signal[:, 0]
    
    encoded_signal = differential_encoding(signal)
    
    output_path = os.path.join(PROJECT_FOLDER, os.path.basename(input_path).replace(".wav", "_encoded.npy"))
    np.save(output_path, encoded_signal)
    return output_path

def decode_audio_file(encoded_path):
    encoded_signal = np.load(encoded_path)
    
    decoded_signal = differential_decoding(encoded_signal)
    
    output_path = os.path.join(PROJECT_FOLDER, os.path.basename(encoded_path).replace("_encoded.npy", "_decoded.wav"))
    sample_rate = 44100  # Default to 44100 Hz; adjust if necessary
    wavfile.write(output_path, sample_rate, decoded_signal.astype(np.int16))
    return output_path

def play_audio(file_path):
    sample_rate, signal = wavfile.read(file_path)
    
    if signal.ndim > 1:
        signal = signal[:, 0]
    
    sd.play(signal, sample_rate)
    sd.wait()
