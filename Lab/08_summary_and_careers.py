bill_amount = float(input())
tip_percent = float(input())
people = int(input())


tip_amount = bill_amount * (tip_percent / 100)
total_amount = bill_amount + tip_amount
amount_per_person = total_amount / people



print(f"Each person pay:{amount_per_person}")
