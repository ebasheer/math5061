class Point2D():

    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __str__(self):
        return '{},{}'.format(self.x,self.y)

ainst = Point2D(2.2,-3.3)
print(ainst)
print(ainst.__str__())
