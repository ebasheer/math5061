import time

class StopWatch():
    def __init__(self):
        self._seconds = 0
        self._running = False
        self._splittime = []

    def start(self):
        if not self._running:
            self._running = True
            self._starttime = time.time()

    def stop(self):
        if self._running:
            curtime = time.time()
            self._seconds += curtime - self._starttime
            self._running = False

    def reset(self):
        if not self._running:
            self._seconds = 0

    def _sec_to_hms(self):
        minutes, seconds = divmod(self._seconds, 60)
        hours, minutes = divmod(minutes, 60)
        return hours, minutes, seconds

    def gettime(self):
        ttuple = self._sec_to_hms()
        return '{} : {} : {}'.format(*ttuple)

    def __str__(self):
        ttuple = self._sec_to_hms()
        return 'hours: {} minutes: {} seconds: {}'.format(*ttuple)

        
