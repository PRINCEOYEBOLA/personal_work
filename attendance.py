def Average_Attend():
    for user in range(1, 11):
        print("Attendance" ,user)
        worship_attend = input('\nEnter attendance for each week separated by space')
        attendance= worship_attend.split()
        print('Worship: ', attendance)
        for num in range(len(attendance)):
            attendance [num] = eval(attendance [num])
        print(len(attendance))
        print('Total = ', sum(attendance))
        print('Average = ', sum(attendance)/len(attendance))
         
Average_Attend()