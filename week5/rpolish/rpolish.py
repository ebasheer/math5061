def pushnum(stack, expr, pos):
    endpos = pos + 1 
    while expr[endpos].isnumeric():
        endpos += 1
    stack.append(expr[pos:endpos])
    return endpos - pos

def evaluate(expr):
    stack = []
    pos = 0
    while pos < len(expr):
        if expr[pos].isnumeric():
            pos += pushnum(stack, expr, pos)
        elif expr[pos] == '-' and pos+1<len(expr)and expr[pos+1].isnumeric():
            pos += pushnum(stack, expr, pos) 
        else:
            pos += 1
    print(stack)


if __name__ == '__main__':
    evaluate('20 3 4 * -')
    
