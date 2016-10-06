import random as rand
import pprint
import timeit

def dot(a,b,c):
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(a[0])):
                c[i][j] += a[i][k] * b[k][j]

pp = pprint.PrettyPrinter(indent=2).pprint

a = [[rand.randint(-10,10) for i in range(5)] for j in range(5)]
b = [[rand.randint(-10,10) for i in range(5)] for j in range(5)]
c = [[0]*5 for i in range(5)]
print(timeit.timeit('dot(a,b,c)',globals=globals(),number=50000))
