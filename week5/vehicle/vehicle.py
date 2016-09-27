class Vehicle:
    def __init__(self, max_pass, wheels):
        self.max_pass = max_pass
        self.wheels = wheels
        self._curspeed = 0

    def speedup(self):
        print('not implemented')

    def slowdown(self):
        print('not implemented')

    def printspeed(self):
        print('current speed',self._curspeed,'mph')
