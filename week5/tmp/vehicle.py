class Vehicle:
    def __init__(self, nwheels, max_pass):
        self.nwheels = nwheels
        self.max_pass = max_pass
        self._currspeed = 0

    def speedup(self):
        print('accelerate but how?')

    def slowdown(self):
        print('decelerate but how?')

    def printspeed(self):
        print('Current speed is',self._currspeed)
        

class Car(Vehicle):
    def __init__(self, manuf, top_speed, ndoors):
        Vehicle.__init__(self, 4, 5)
        self.manuf = manuf
        self.top_speed = top_speed
        self.ndoors = ndoors

    def speedup(self):
        print('depress accelerator pedal')
        self._currspeed += 1

    def slowdown(self):
        print('depress brake pedal')
        self._currspeed -= 1










