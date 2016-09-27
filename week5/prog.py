from rectangle import Rectangle

a = Rectangle('-3,-9','0.0,0.0')
b = Rectangle('1,1','10,-10')
print(a.overlap(b))
print(a.area())
print(b.overlap(b))
print(b.area())
