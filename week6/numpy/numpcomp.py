import random as rand
import pprint
import timeit
import numpy as np

pp = pprint.PrettyPrinter(indent=2).pprint

a = [[rand.randint(-10,10) for i in range(5)] for j in range(5)]
b = [[rand.randint(-10,10) for i in range(5)] for j in range(5)]
c = [[0]*5 for i in range(5)]
pp(a)
pp(b)
pp(c)
a = np.array(a)
b = np.array(b)
c = np.zeros((5,5),dtype=np.int)
print(timeit.timeit('np.dot(a,b,c)',globals=globals(),number=50000))
