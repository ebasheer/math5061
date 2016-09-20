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

def overlap(A_tl, A_br, B_tl, B_br):
    return not ( A_br.isleftof(B_tl) or A_tl.isrightof(B_br) or 
                 A_br.isabove(B_tl) or A_tl.isbelow(B_br)) 

if __name__ == '__main__':
    A_tl = Point2D(input('Top-Left of A: '))
    A_br = Point2D(input('Bottom-Right of A: '))
    B_tl = Point2D(input('Top-Left of B: '))
    B_br = Point2D(input('Bottom-Right of A: '))

    if overlap(A_tl, A_br, B_tl, B_br):
        print('Rectangles overlap')
    else:
        print('No Overlap')
