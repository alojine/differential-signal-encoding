import numpy as np
from scipy.io import wavfile
import tkinter as tk
from tkinter import filedialog
import os

def differential_encoding(signal):
    encoded_signal = np.diff(signal, prepend=0)
    return encoded_signal

def encode_audio_file(input_path):
    sample_rate, signal = wavfile.read(input_path)
    
    if signal.ndim > 1:
        signal = signal[:, 0]
    
    encoded_signal = differential_encoding(signal)
    
    output_path = os.path.splitext(input_path)[0] + "_encoded.npy"
    np.save(output_path, encoded_signal)
    return output_path

def select_file_and_encode():
    file_path = filedialog.askopenfilename(
        title="Select an Audio File",
        filetypes=[("WAV files", "*.wav")]
    )
    
    if file_path:
        encoded_file_path = encode_audio_file(file_path)
        print(f"Encoded signal saved to {encoded_file_path}")

root = tk.Tk()
root.title("Audio Differential Encoder")
root.geometry("300x150")

select_button = tk.Button(root, text="Select Audio File", command=select_file_and_encode)
select_button.pack(expand=True)

root.mainloop()
