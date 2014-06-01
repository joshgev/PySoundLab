import wave
from itertools import izip
from itertools import imap
# import matplotlib.pyplot as plt
import math
import struct
import numpy
import matplotlib.pyplot as plt
from soundsystem import SoundSystem
from time import *


def play(Sound):
    wav = wave.open("josh.wav", "w")
    wav.setparams((1, 2, 44100, 44100,"NONE", "not compressed"))
    for s in Sound.generate():

        wav.writeframes(struct.pack('h', int(s * (2**16 - 1) / 2)))
    wav.close()


def create_pitch_sampler(frequency):

    s = SoundSystem.rate
    gf = lambda t: math.sin(2 * math.pi * frequency * t / s)

    return gf


class Pitch:

    def __init__(self, frequency):
        self._frequency = frequency


class MixedSound:
    def __init__(self, *ranges_and_sounds):
        self._ranges_and_sounds = ranges_and_sounds

    def _sample(self, s):
        return sum([sound._sample(s) for r, sound in self._ranges_and_sounds if r.contains(Time.from_samples(s))])


class Sound:
    def __init__(self, sampler, duration, vol=1):
        self._sampler = sampler
        self._duration = duration
        self._vol = vol

    def _sample(self, s):
        return self._sampler(s)

    def generate(self):
        for s in range(self._duration.to_samples):
            yield self._sampler(s)