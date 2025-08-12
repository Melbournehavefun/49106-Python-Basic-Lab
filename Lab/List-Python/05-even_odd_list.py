n = int(input())
even = []
odd = []
for i in range(n):
    num = int(input())
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print(f"เลขคู่: {even}")
print(f"เลขคี่: {odd}")
