class Point2D():
    def __init__(self, strcoord='0.0,0.0'):
        self.x, self.y = map(float, strcoord.split(','))

    def printxy(self):
        print('x coord:',self.x)
        print('y coord:',self.y)

ainst = Point2D('-200,900')
binst = Point2D()

ainst.printxy()
binst.printxy()
