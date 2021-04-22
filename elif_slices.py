slices=int(input("Enter the slices:"))
amount=0
if slices%2==0:
    amount=slices*120.00
else:
    amount=slices*123.00
print(amount)