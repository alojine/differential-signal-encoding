import numpy as np

def differential_encoding(signal):
    """
    Perform differential encoding on a given audio signal.
    
    Parameters:
    signal (array-like): Original audio signal as an array of sample values.
    
    Returns:
    np.ndarray: Differentially encoded signal where each value is the difference
                between successive samples.
    """
    # Calculate the differences between consecutive samples
    encoded_signal = np.diff(signal, prepend=0)  # prepend=0 assumes the first difference is from 0
    return encoded_signal

# Example signal (simulating a short audio sequence)
original_signal = np.array([100, 105, 110, 108, 107, 115, 120, 125, 130, 128])

# Apply differential encoding
encoded_signal = differential_encoding(original_signal)

original_signal, encoded_signal
