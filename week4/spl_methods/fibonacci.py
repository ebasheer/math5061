"""Generate list of n fibonacci numbers"""

n = int(input('number:'))

a, b = 0, 1
for i in range(n):
    a, b = b, a+b

print(b)
