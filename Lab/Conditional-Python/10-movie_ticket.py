age = int(input())
days = int(input())

if(age < 13):
    price = 100
elif(age >=13 and age < 60):
    price = 180
else:
    price = 120

if(days > 5):
    price = price + 50
    print(price)
else:
    price = price
    print(price)

