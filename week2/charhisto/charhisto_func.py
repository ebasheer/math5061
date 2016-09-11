""" Program to count number of occurrences of characters"""

def charhisto(s):
    hist = {}
    for char in s.lower():
        if char.isalpha():
            if char not in hist:
                hist[char] = 1
            else:
                hist[char] += 1
    return hist

def printhist(d):
    for char, num in d.items():
        print(char,': ', '+'*num)
    
instr = "Twas the night before start-up and all through the net "\
        "not a packet was moving; no bit nor octet. "\
        "The engineers rattled their cards in despair "\
        "hoping a bad chip would blow with a flare. "

mystr = "This is another shorter sentence for which "\
        "we want to count the number of occurrences of"\
        "each character"

hist_dict = charhisto(instr)
printhist(hist_dict)
print('\n')
hist_dict = charhisto(mystr)
printhist(hist_dict)
