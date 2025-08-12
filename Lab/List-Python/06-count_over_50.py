n = int(input())
count = 0
for i in range(n):
    num = int(input())
    if num > 50:
        count = count+1
    else:
        count = count

print(f"จำนวนที่มากกว่า 50:{count}")