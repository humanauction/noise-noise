import numpy as np
import soundfile as sf
from scipy import signal


def _colored_noise(beta, n, sample_rate):
    """
    generate colored noise with Proportional Spectral Density
    ~ 1/F^beta via FFT
    beta=0: white | beta=1: pink | beta=2: red
    beta=-1: blue | beta=-2: purple
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
    b_a = signal.butter(order, [low_hz/nyq, high_hz/nyq], btype='band')
    if b_a is None or not isinstance(b_a, (tuple, list)) or len(b_a) != 2:
        raise ValueError("Filter design failed; check frequency parameters.")
    b, a = b_a
    y = signal.lfilter(b, a, x)
    # If lfilter returns a tuple (output, state), extract output
    if isinstance(y, tuple):
        y = y[0]
    # 3: normalize
    y -= y.mean()
    y /= np.max(np.abs(y))
    return y


def apply_envelope(data, envelope_type='linear'):
    """ apply an envelope for manipulating noise data """
    # fade in-out
    n = len(data)
    if envelope_type == 'linear':
        env = np.linspace(0, 1, n//2)
        env = np.concatenate([env, env[::-1]])
        return data * env[:n]
    return data


def generate_noise(
        color: str, duration=10.0, sample_rate=44100, envelope=None
        ):
    """ generate colored noise """
    n = int(duration * sample_rate)

    generators = {
        'white': lambda: np.random.randn(n),
        'pink': lambda: _colored_noise(1, n, sample_rate),
        'red': lambda: _colored_noise(2, n, sample_rate),
        'blue': lambda: _colored_noise(-1, n, sample_rate),
        'purple': lambda: _colored_noise(-2, n, sample_rate),
        'yellow': lambda: (
            _colored_noise(1, n, sample_rate) + np.random.rand(n)
        ) / 2,
        'brown': lambda: _bandpass_noise(80, 400, n, sample_rate),
        'green': lambda: _bandpass_noise(300, 700, n, sample_rate),
    }

    try:
        data = generators[color.lower()]()
        if envelope:
            data = apply_envelope(data, envelope)
    except KeyError:
        raise ValueError(
            f'unknown colour: {color}. Please choose from: '
            f'{", ".join(generators.keys())}'
        )
    return data


def save_noise(color, filename, duration=10.0, sample_rate=44100):
    data = generate_noise(color, duration, sample_rate)
    sf.write(filename, data, sample_rate)
