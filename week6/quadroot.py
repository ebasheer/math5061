import math

def quadroot(a, b, c):
    discr = (b * b) - (4 * a * c)
    discr_sqrt = math.sqrt(discr)
    root1 = (-b + discr_sqrt) / (2 * a)
    root2 = (-b - discr_sqrt) / (2 * a)
    return root1, root2

if __name__ == '__main__':
    r1, r2 = quadroot(1, 3, -10)
    print(r1, r2)
