price = float(input())


if(price >= 2000):
    discount = price * 15 / 100

elif(price >= 1000 and price < 2000):
    discount = price * 10 / 100

elif(price >=500 and price < 1000):
    discount = price * 5 / 100

else:
    discount = 0

print(price - discount)