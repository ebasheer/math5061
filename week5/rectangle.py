import point2d as pt

class Rectangle:
    def __init__(self, pt1='0.0,0.0', pt2='1.0,1.0'):
        self.tl = pt.Point2D(pt1)
        self.br = pt.Point2D(pt2)


    def overlap(self, other):
        return not ( self.br.isleftof(other.tl) or self.tl.isrightof(other.br) or 
                     self.br.isabove(other.tl) or self.tl.isbelow(other.br)) 

    def area(self):
        return self.tl.xdist(self.br) * self.tl.ydist(self.br)
 
