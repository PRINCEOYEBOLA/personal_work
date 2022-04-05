heart_kind = []
for user in range(1,5):
    soil_type = input('Enter the type of soil:  ')
    heart_kind.append(soil_type)
    print(heart_kind)
for heart in heart_kind:
    for user in range(1,5):
        print('\nWelcome Applicant', user)
        soil_num = eval(input('Enter a number from 0 to 3:  '))
        if soil_num == 0:
            print('The' ,heart_kind[0], 'is selected. Your heart is by the way,  birds of the air picked the seed sown on it')
        elif soil_num == 1:
            print('The' ,heart_kind[1], 'is selected. Your heart is rocky, seed planted made effor to grow but dies because it has no root')
        elif soil_num == 2:
            print('The' ,heart_kind[2], 'is selected. Your heart is full of thorns, seed planted grew but the thorns around it shocked it to death')
        elif soil_num == 3:
            print('The' ,heart_kind[3], 'is selected. Your heart is good and fertile, seed planted grew and brought forth much fruits')
        else:
            print("select one of the types of soil")