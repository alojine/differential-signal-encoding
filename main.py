import tkinter as tk
from tkinter import filedialog
import os
import numpy as np
from scipy.io import wavfile
from utils import encode_audio_file, decode_audio_file, play_audio

def select_and_encode_file():
    file_path = filedialog.askopenfilename(
        title="Select an Audio File",
        filetypes=[("WAV files", "*.wav")]
    )
    
    if file_path:
        encoded_file_path = encode_audio_file(file_path)
        print(f"Encoded signal saved to {encoded_file_path}")

def play_original_audio():
    file_path = filedialog.askopenfilename(
        title="Select an Audio File",
        filetypes=[("WAV files", "*.wav")]
    )
    
    if file_path:
        play_audio(file_path)

def decode_and_play():
    encoded_file_path = filedialog.askopenfilename(
        title="Select an Encoded File",
        filetypes=[("NumPy files", "*.npy")]
    )
    
    if encoded_file_path:
        decoded_file_path = decode_audio_file(encoded_file_path)
        print(f"Decoded audio saved to {decoded_file_path}")
        play_audio(decoded_file_path)


root = tk.Tk()
root.title("Audio Differential Encoder/Decoder")
root.geometry("300x200")

select_encode_button = tk.Button(root, text="Select and Encode File", command=select_and_encode_file)
select_encode_button.pack(pady=10)

play_original_button = tk.Button(root, text="Play Original File", command=play_original_audio)
play_original_button.pack(pady=10)

decode_play_button = tk.Button(root, text="Decode and Play", command=decode_and_play)
decode_play_button.pack(pady=10)

root.mainloop()
