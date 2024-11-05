import tkinter as tk
from tkinter import filedialog
import numpy as np
from utils import encode_audio_file, decode_audio_data, play_audio_data

original_sample_rate = None
original_audio_data = None
encoded_audio_data = None

def select_and_encode_file():
    global original_sample_rate, original_audio_data, encoded_audio_data

    file_path = filedialog.askopenfilename(
        title="Select an Audio File",
        filetypes=[("WAV files", "*.wav")]
    )
    
    if file_path:
        # Load and encode the audio file, keeping data in memory
        original_sample_rate, original_audio_data, encoded_audio_data, encoded_file_path = encode_audio_file(file_path)
        print(f"Encoded signal saved to {encoded_file_path}")

def play_original_audio():
    if original_audio_data is not None:
        play_audio_data(original_sample_rate, original_audio_data)
    else:
        print("No audio file loaded. Please select and encode a file first.")

def decode_and_play():
    global encoded_audio_data, original_sample_rate
    
    if encoded_audio_data is not None:
        decoded_audio_data = decode_audio_data(encoded_audio_data)
        play_audio_data(original_sample_rate, decoded_audio_data)
    else:
        print("No encoded data found. Please select and encode a file first.")

def dashboard():
    root = tk.Tk()
    root.title("Audio Differential Encoder/Decoder")
    root.geometry("450x200")

    select_encode_button = tk.Button(root, text="Select and Encode File", command=select_and_encode_file)
    select_encode_button.pack(pady=10)

    play_original_button = tk.Button(root, text="Play Original File", command=play_original_audio)
    play_original_button.pack(pady=10)

    decode_play_button = tk.Button(root, text="Decode and Play", command=decode_and_play)
    decode_play_button.pack(pady=10)

    root.mainloop()

dashboard()