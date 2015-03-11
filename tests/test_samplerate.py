import numpy as np
import scikits.samplerate as samplerate

def test_samplerate():

    y = np.random.randn(8000)

    y_out = samplerate.resample(y, 1.5, 'sinc_fastest')
