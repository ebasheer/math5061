tender = [2000, 1000, 500, 100, 25, 10, 5, 1]
billcoins = []
amt = float(input('Enter dollar amount: '))  #example 125.36
amt = int(amt * 100)

for denom in tender:
    billcoins.append(int(amt / denom))
    amt = amt % denom

print('20 bill:', billcoins[0])
print('10 bill:', billcoins[1])
print('5 bill:', billcoins[2])
print('1 bill:', billcoins[3])
print('0.25 coin:', billcoins[4])
print('0.10 coin:', billcoins[5])
print('0.05 coin:', billcoins[6])
print('0.01 coin:', billcoins[7])
