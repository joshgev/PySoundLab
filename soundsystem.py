__author__ = 'jgevirtz'


class SoundSystem:
    rate = 44100

    def __init__(self):
        self.tracks = []

    def add(self, track):
        self.tracks.append(track)


