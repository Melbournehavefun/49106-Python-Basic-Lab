work = int(input())
midterm = int(input())
final = int(input())

sum = work + midterm + final

while work <= 30 and midterm <= 30 and final <=40:
    if sum >= 80:
        print('A')
        break
    elif sum >= 75 and sum < 80:
        print('B+')
        break
    elif sum >= 70 and sum < 75:
        print('B')
        break
    elif sum >= 65 and sum < 70:
        print('C+')
        break
    elif sum >= 60 and sum < 65:
        print('C')
        break
    elif sum >= 55 and sum < 65:
        print('D+')
        break
    elif sum >= 50 and sum < 55:
        print('D')
        break
    else:
        print('F')
        break
    
    End

