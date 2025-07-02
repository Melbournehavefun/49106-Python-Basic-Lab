i = 0 ; max = 0

while i < 3:
    num = int(input())
    if(num > max):
        max = num
    else:
        max = max
    i=i+1


print(max)