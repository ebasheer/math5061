from vehicle import Vehicle

class Motorcycle(Vehicle):
    def __init__(self, manuf, top_speed):
        super().__init__(max_pass=2, wheels=2)
        self.manuf = manuf
        self.top_speed = top_speed

    def speedup(self):
        print('speedup by 1 mph. twist throttle')
        if self._curspeed < self.top_speed:
            self._curspeed += 1
        else:
           print('top speed!')

    def slowdown(self):
        print('slowdown by 1 mph. press brake lever')
        if self._curspeed > 0:
            self._curspeed -= 1

