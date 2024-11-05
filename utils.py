import numpy as np
from scipy.io import wavfile
import os

PROJECT_FOLDER = "audio_samples"

if not os.path.exists(PROJECT_FOLDER):
    os.makedirs(PROJECT_FOLDER)

def differential_encoding(signal):
    if signal.ndim == 1:
        # For mono audio, initialize with the first sample
        encoded_signal = [signal[0]]
        for i in range(1, len(signal)):
            diff = signal[i] - signal[i - 1]
            encoded_signal.append(diff)
    elif signal.ndim == 2:
        # For stereo audio, initialize an array to hold encoded values
        encoded_signal = np.zeros_like(signal)
        for channel in range(signal.shape[1]):
            encoded_signal[0, channel] = signal[0, channel]  # Store first sample for each channel
            for i in range(1, signal.shape[0]):
                diff = signal[i, channel] - signal[i - 1, channel]
                encoded_signal[i, channel] = diff
    else:
        raise ValueError("Signal should be either 1D or 2D.")
    
    return np.array(encoded_signal)

def encode_audio_file(input_path):
    sample_rate, signal = wavfile.read(input_path)
    encoded_signal = differential_encoding(signal)
    output_path = os.path.join(PROJECT_FOLDER, os.path.basename(input_path).replace(".wav", "_encoded.npy"))
    np.save(output_path, encoded_signal)

    return sample_rate, signal, encoded_signal, output_path

def differential_decoding(encoded_signal):
    """ Decode the encoded signal back to the original signal using cumulative sum. """
    return np.cumsum(encoded_signal)

def decode_audio_data(encoded_signal):
    decoded_signal = differential_decoding(encoded_signal)
    decoded_signal = decoded_signal.astype(np.int16)
    return decoded_signal

def play_audio_data(sample_rate, audio_data):
    import sounddevice as sd
    sd.play(audio_data, sample_rate)
    sd.wait()