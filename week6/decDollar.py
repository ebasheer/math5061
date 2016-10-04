import decimal
D = decimal.Decimal

amount = D(input("enter amount: "))
print(amount)

for i in map(D,['20', '10', '5', '1', '0.25', '0.1', '0.05', '0.01']):
    print(' {} ${:.2f} bill/coin'.format(amount//i, i))
    amount = amount % i
