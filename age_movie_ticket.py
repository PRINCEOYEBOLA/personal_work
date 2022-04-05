#Design an app for movie ticket based on age

print('Welcome to the Movie Night, follow instructions below')

for user in range(1,6):
    print('User', user, 'welcome!')
    user_age = input('\nEnter your age to determine your ticket fare:  ')
    print('\n')
    age = eval(user_age)
    print('\n')
    if age <= 8 or age >= 65:
        print('Your movie ticket is free')
    elif age <= 10:
        print('Your movie ticket is ' + '$' + str(5))
    elif age <= 18:
        print('Your movie ticket is ' + '$' + str(10))
    elif age <= 25:
         print('Your movie ticket is ' + '$' + str(15))
    else:
         print('Your movie ticket is ' + '$' + str(20))
    