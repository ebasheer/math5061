"""Print fibonacci numbers less that input value"""

n = input('enter number:')
n = int(n)

a, b = 0, 1
while b < n:
    print(b)
    a, b = b, a+b
