n = int(input())
numbers = []
for i in range(n):
    num = int(input())
    if num >= 10 and num <= 50:
        numbers.append(num)
    else:
        numbers = numbers

print(f"ค่าที่อยู่ในช่วง 10-50:{numbers}")