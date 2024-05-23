height = int(input('Whats your height?'))
age = int(input('Whats your age?'))

if height > 120:
    if age > 18:
        print("It's $12")
    elif age >= 12 and age <= 18:
        print("It's $7")
    else:
        print("It's $5")
    print('You can ride!')
else:
    print("You can't ride!")