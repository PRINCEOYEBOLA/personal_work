#KODE CAMP PYTHON BEGINNER ASSIGNMENT
#OYEBOLA ODELEYE

"""Ask user for a Temperature.Then ask them what units. 
Celsius or Fahrenheit, the temperature is in. 
Your program should convert the temperature to 
the other unit. 
The coversions are F=9/5C + 32 and C=5/9(F-32)."""

#Initiate a user range
for user in range(1,3):
    print("\nUser",user, "welcome!")
    user_prompt = eval(input("Enter your temperature(number):  "))
    user_temp = input("Choose the unit of your temperature: ('Celsius' or  'Fahrenheit'):  ")
    print('\n')
    #converting the Temperature Fahrenheit to Celsius
    if user_temp == 'Fahrenheit':
        print("Your temperature is", user_prompt, user_temp)
        print('Conversion from Fahrenheit to Celsius')
        F = user_prompt
        Celsius = 5 / 9 * (F - 32)
        print(Celsius, 'Celsius')

        print('\n')
    #converting the Temperature from Celsius to Fahrenheit
    elif user_temp == 'Celsius':
        print("Your temperature is", user_prompt, user_temp)
        print('Conversion from Celsius to Fahrenheit')
        C = user_prompt
        Fahrenheit = 9 / 5 * C + 32
        print(Fahrenheit, 'Fahrenheit') 
    else:
         print("Enter valid value unit")
    
