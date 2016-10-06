from operator import add, mul, floordiv, sub

class InvalidCharError(Exception):
    pass

def op(stack, oper):
    b = stack.pop()
    a = stack.pop()
    if oper == '+':
        stack.append(add(a,b))
    if oper == '-':
        stack.append(sub(a,b))
    if oper == '*':
        stack.append(mul(a,b))
    if oper == '/':
        stack.append(floordiv(a,b))

def pushnum(stack, expr, pos):
    endpos = pos + 1 
    while expr[endpos].isnumeric():
        endpos += 1
    stack.append(int(expr[pos:endpos]))
    return endpos - pos

def evaluate(expr):
    stack = []
    pos = 0
    while pos < len(expr):
        if expr[pos].isnumeric():
            pos += pushnum(stack, expr, pos)
        elif expr[pos] == '-' and pos+1<len(expr)and expr[pos+1].isnumeric():
            pos += pushnum(stack, expr, pos) 
        elif expr[pos] in '+-*/':
            op(stack, expr[pos])
            pos += 1
        elif expr[pos] == ' ':
            pos += 1
        else:
            raise InvalidCharError("found a strange character")
            pos += 1
    print(stack.pop())


if __name__ == '__main__':
    expr = input("enter expr: ")
    evaluate(expr)
    
