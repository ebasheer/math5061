""" Print a list of squares using various loops"""
n = 12

# using a for loop and list method append()
squares = []
for i in range(n):
    squares.append(i**2)
print(squares)

# Same algorithm written using a List Comprehension
squares_c = [i**2 for i in range(n)]
print(squares_c)
