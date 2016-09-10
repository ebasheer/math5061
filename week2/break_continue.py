"""Program demonstrating break and continue statements."""

while True:
    inp = input('Enter a word: ')
    if inp == 'end' or inp == 'End':
        break
    elif inp == 'skip' or inp == 'Skip':
        continue
    else:
        print(inp)
