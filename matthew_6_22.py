for user in range(5):
    user_input = input("\nYour name:  ")
    print('You are welcome' , user_input)
    lamp = input("Enter a value: ('Good' or 'Bad'):  ")
    if lamp == 'Good':
        print("Your eye is good and body full of light")
    elif lamp == 'Bad':
        print("Your eyes is bad and body full of darkness")
    else:
        print("Enter a value between ('Good' or 'Bad')")
      