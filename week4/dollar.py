amount = input("enter amount")
amount = int(amount.translate(''.maketrans('','', '.')))
print(amount)

for i in [2000, 1000, 500, 100, 25, 10, 5, 1]:
    print(' {} ${:.2f} bill/coin'.format(amount//i, i/100))
    amount = amount % i
