def one():
    try:
        two()
    except ZeroDivisionError:
        print('ZeroDivisionError Handler in one()')

def two():
    three()

def three():
    four()

def four():
    try:
        1/0
    except ValueError:
        print('ValueError Handler in four()')

if __name__ == '__main__':
    one()
