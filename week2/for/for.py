""" Find the value and position of the largest number in a list.

    Implemented using range() and len() built-ins.
"""

numlist = (1000,0.22, 34, 4, -12, 13.01, 140.45, 111)

maxnum = numlist[0]
maxpos = 0
for idx in range(len(numlist)):
    if numlist[idx] > maxnum:
        maxnum = numlist[idx]
        maxpos = idx
print(maxnum,"at",maxpos)
