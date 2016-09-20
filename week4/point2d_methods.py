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

ainst = Point2D('-200,900')
binst = Point2D()    # 0.0,0.0

if __name__ == '__main__':
    print(ainst.isleftof(binst))
    print(ainst.isrightof(binst))
    print(binst.isabove(ainst))
    print(binst.isbelow(ainst))
