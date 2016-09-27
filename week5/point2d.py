class Point2D():

    def __init__(self, strcoord='0.0,0.0'):
        self.x, self.y = map(float, strcoord.split(','))

    def printxy(self):
        print('x coord:',self.x)
        print('y coord:',self.y)

    def isleftof(self, other):
        return self.x < other.x

    def isrightof(self, other):
        return self.x > other.x

    def isabove(self, other):
        return self.y > other.y

    def isbelow(self, other):
        return self.y < other.y

    def xdist(self, other):
        return abs(self.x - other.x)

    def ydist(self, other):
        return abs(self.y - other.y)

