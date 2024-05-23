print('Welcome to the tip calculator')
total_bill = float(input('What was the total bill? '))
split = int(input('How many people to split bill? '))
percentage = int(input('What percentage tip would you like to give? 10, 12 or 15? '))

splitted_bill = total_bill / split
pay_each = splitted_bill / 100 * percentage
print(round(pay_each + splitted_bill, 2))