class Temperature:
    def __init__(self, temp, unit):
        if unit == 'C':
            self._degc = temp
            self._degf = self.ctof(temp)
        elif unit == 'F':
            self._degf = temp
            self._degc = self.ftoc(temp)
        else:
            raise ValueError

    def ctof(self, temp):
        return (temp * (9/5)) + 32

    def ftoc(self, temp):
        return (temp - 32) * (5 / 9)

    @property
    def degf(self):
        return self._degf

    @degf.setter
    def degf(self, temp):
        self._degc = self.ftoc(temp)

    @property
    def degc(self):
        return self._degc

    @degc.setter
    def degc(self, temp):
        self._degf = self.ctof(temp)




