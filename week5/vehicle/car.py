from vehicle import Vehicle
from engine import Engine

class Car(Vehicle):
    def __init__(self, manuf, top_speed, ndoors, etype='gas'):
        super().__init__(max_pass=5, wheels=4)
        self.manuf = manuf
        self.top_speed = top_speed
        self.ndoors = ndoors 
        self.engine = Engine(etype)

    def speedup(self):
        print('speedup by 1 mph. Depress gas pedal')
        self.engine.inc_speed()
        if self._curspeed < self.top_speed:
            self._curspeed += 1
        else:
           print('top speed!')

    def slowdown(self):
        print('slowdown by 1 mph. Depress brake pedal')
        if self._curspeed > 0:
            self._curspeed -= 1

class SportsCar(Car):
    def __init__(self,manuf, top_speed):
        super().__init__(manuf, top_speed, 2)
        self.manuf = manuf
        self.top_speed = top_speed

    def speedup(self):
        print('speedup by 5mph')
        self._curspeed += 5
