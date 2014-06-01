from soundsystem import SoundSystem


class Time:
    def __init__(self, _time):
        self._time = _time

    @staticmethod
    def from_seconds(time):
        return Time(time * SoundSystem.rate)

    @staticmethod
    def from_samples(time):
        return Time(time)

    def to_seconds(self):
        return int(float(self._time) / SoundSystem.rate)

    def to_samples(self):
        return self._time


class Range:
    def __init__(self, _start, _end):
        self.start = _start
        self.end = _end

    @staticmethod
    def from_seconds(start, end):
        return Range(Time.from_seconds(start), Time.from_seconds(end))

    @staticmethod
    def from_samples(start, end):
        return Range(Time.from_samples(start), Time.from_samples(end))

    def intersection(self, other):
        times = [[self.start, self],
                 [self.end, self],
                 [other.start, other],
                 [other.end, other]]
        times.sort(key=lambda x: x[0].to_samples())
        #Second range starts after first range
        if times[0][1] == times[1][1]:
            return None
        else:
            end = min(times[2][0], times[3][0], key=lambda x: x.to_samples())
            return Range(times[1][0], end)

    def union(self, other):
        pass

    def difference(self, other):
        pass

    def contains(self, time):
        return self.start.to_samples() <= time.to_samples() <= self.end.to_samples()

    def __str__(self):
        return "[" + str(self.start.to_seconds()) + ", " + str(self.end.to_seconds()) + "]"


if __name__ == "__main__":
    a = Range.from_seconds(0, 4)
    b = Range.from_seconds(1, 3)

    print str(a.intersection(b))