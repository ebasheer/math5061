""" Program to count number of occurrences of characters"""

instr = "Twas the night before start-up and all through the net "\
        "not a packet was moving; no bit nor octet. "\
        "The engineers rattled their cards in despair "\
        "hoping a bad chip would blow with a flare. "\
        "The salesmen were nestled all snug in their beds, "\
        "while visions of data nets danced in their heads. "\
        "And I with my datascope tracings and dumps "\
        "prepared for some pretty bad bruises and lumps. "\
        "When out in the hall there arose such a clatter, "\
        "I sprang from my desk to see what was the matter"


hist = {}
for char in instr.lower():
    if char.isalpha():
        if char not in hist:
            hist[char] = 0
        else:
            hist[char] += 1

for char, num in hist.items():
    print(char,': ', '+'*num)
