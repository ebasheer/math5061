""" Find the value and position of the largest number in a list.

    Implemented using enumerate() built-in.
"""

numlist = (10,0.22, 34, 4, -12, 13.01, 140.45, 111)

maxnum = numlist[0]
maxpos = 0
for idx, num in enumerate(numlist):
    if num > maxnum:
        maxnum = num
        maxpos = idx
print(maxnum,"at",maxpos)
