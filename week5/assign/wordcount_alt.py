def genhist(fname):
    wordlst = []
    freqlst = []
    with open(fname,'rt',encoding='utf-8') as fd:
        for line in fd:
            for word in line.split():
                word = word.lower().strip('.,:!();"\'')
                if word not in wordlst:
                    wordlst.append(word)
                    freqlst.append(1)
                else:
                    freqlst[wordlst.index(word)] += 1

    return zip(freqlst,wordlst)

def printhist(hist):
    for freq, char in sorted(hist):
        print('{}: {}'.format(char,'+'*freq))
            

freqh = genhist('rfc.txt')
printhist(freqh)
