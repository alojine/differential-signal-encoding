import numpy as np
from utils import differential_encoding

def should_decode_mono_signal():
    mono_signal = np.array([100, 105, 110, 108, 107])
    encoded_mono_signal = differential_encoding(mono_signal)
    print("Encoded Mono Signal:", encoded_mono_signal)

def should_decode_stereo_signal():
    stereo_signal = np.array([[100, 200], [105, 205], [110, 210], [108, 208], [107, 207]])
    encoded_stereo_signal = differential_encoding(stereo_signal)
    print("Encoded Stereo Signal:\n", encoded_stereo_signal)

should_decode_mono_signal()
should_decode_stereo_signal()