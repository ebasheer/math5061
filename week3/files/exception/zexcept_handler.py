while True:
    try:
        a = int(input('Enter first integer:'))
        b = int(input('Enter second integer:'))
        q = a / b
        print('a/b is: ',q)
    except ZeroDivisionError:
        print("Can't divide by zero. Try again")
    except ValueError:
        print("invalid input")
