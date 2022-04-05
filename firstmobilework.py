apple_price = 5
money_available = 50

prompt = input("How many apples do you want to buy?  ")

no_apple  = eval(prompt)
total_price = no_apple * apple_price

print('You want to buy', no_apple, 'apples')
print('Your total bill is',total_price, 'dollars')

#add flow control to the code
if total_price < money_available:
    print('You have bought', no_apple, 'apples')
    print('You have', money_available - total_price,'dollars left with you')
elif total_price == money_available:
    print('You have bought', no_apple, 'apples')
    print('You have no money available')
else:
    print('You cannot buy', no_apple, 'apples')
    print('You do not have enough money to buy that quantity')