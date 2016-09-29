class Engine:
    def __init__(self, tech='gas'):
        self.tech = tech
        if self.tech == 'gas':
            self._rpm = 500
        elif self.tech == 'electric':
            self._rpm = 0

    def inc_speed(self):
        if self.tech == 'gas':
            print('engine goes vroom...')
        elif self.tech == 'electric':
            print('engine goes ssshh...')
        self._rpm += 100

    def dec_speed(self):
        self._rpm -= 100
         
