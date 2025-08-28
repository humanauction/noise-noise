import numpy as np
import soundfile as sf
from scipy import signal

def _colored_noise(beta, n, sample_rate)
    """ 
    generate colored noise with Proportional Spectral Density ~ 1/F^beta via FFT
    beta=0: white | beta=1: pink | beta=2: brown (red)
    beta=-1: blue | beta=-2: purple (violet)
    """
    # 1: white noise
    x = np.random.randn(n)
    # 2: FFT
    xf = np.fft.rfft(x)
    # 3: build filter for 1/f^beta
    freqs = np.fft.rfftfreq(n, d=1./sample_rate)
    # avoid divide-by-zero at DC
    f = np.where(freqs == 0, freqs[1], freqs)
    S = 1 / (f ** (beta / 2.0))
    # 4. apply, inverse FFT
    y = np.fft.irfft(xf * S, n)
    # 5. normalize
    y -= y.mean()
    y /= np.max(np.abs(y))
    return y

def _bandpass_noise(low_hz, high_hz, n, sample_rate, order=4):
    """ generate bandpass filtered white noise """
    # 1: white noise
    x = np.random.randn(n)
    # 2: bandpass filter
    nyq = sample_rate / 2.0  # nyquist frequency
    b, a = signal.butter(order, [low_hz/nyq, high_hz/nyq], btype='band')
    y = signal.lfilter(b, a, x)
    # 3: normalize
    y -= y.mean()
    y /= np.max(np.abs(y))
    return y

def generate_noise(color:str, duration=10.0, sample_rate=44100):
    """ generate colored noise """
    n = int(duration * sample_rate)

    generators = {
        'white': lambda: np.random.randn(n),
        'pink': lambda: _colored_noise(1, n, sample_rate),
        'red': lambda: _colored_noise(2, n, sample_rate),
        'blue': lambda: _colored_noise(-1, n, sample_rate),
        'purple': lambda: _colored_noise(-2, n, sample_rate),
        'yellow': lambda: (_colored_noise(1, n, sample_rate) + np.random.rand(n)) / 2,
        'brown': lambda: _bandpass_noise(80, 400, n, sample_rate),
        'green': lambda: _bandpass_noise(300, 700, n, sample_rate),
    }

    try:
        data = generators[color.lower()]()
    except KeyError:
        raise ValueError(f'unknown colour: {color}. Please choose from: {", ".join(generators.keys())}')
