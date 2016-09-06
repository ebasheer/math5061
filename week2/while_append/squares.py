n = 12

# Create a list of squares of integers < n
squares = []
for i in range(n):
    squares.append(i**2)
print(squares)

# Same algorithm written using a List Comprehension
squares_c = [i**2 for i in range(n)]
print(squares_c)
