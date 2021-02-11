import random
import string


class TrackIdGenerator(object):
    def __init__(self, chars=None, random_generator=None):
        self.chars = chars or string.ascii_uppercase + string.ascii_lowercase + string.digits
        self.random_generator = random_generator or random.SystemRandom()

    def make_trackid(self, n=20):
        return ''.join(self.random_generator.choice(self.chars) for _ in range(n))


TrackId_generator = TrackIdGenerator()
