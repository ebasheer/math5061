def genhist(fname):
    hist = {}
    with open(fname,'rt',encoding='utf-8') as fd:
        for line in fd:
            for word in line.split():
                word = word.lower().strip('.,:!();"\'')
                if word not in hist:
                    hist[word] = 1
                else:
                    hist[word] += 1

    return hist

def printhist(hist):
    def item1(s):
        return s[1]

    for char, freq in sorted(hist.items(), key=item1):
        print('{}: {}'.format(char,'+'*freq))
            

freqh = genhist('rfc.txt')
printhist(freqh)
