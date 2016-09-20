amount = input("enter amount")
amount = int(amount.translate(''.maketrans('','', '.')))
print(amount)

for i in [2000, 1000, 500, 100, 25, 10, 5, 1]:
    print(amount, ' number of ',i/100, ' bills', amount//i)
    amount = amount % i
