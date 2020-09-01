Items=["","1. Juice","2. Oreos","3. Milo","4. Nuts","5. Ice Cream","6. Sandwich"]
Prices=["",5,4.5,6,12,4,13]
for x in range(7):
  print(Items[x],Prices[x])
Choice=int(input("Input the number of your choice"))
Payment=0
while Payment<Prices[Choice]:
  Payment=float(input("Input how much money you entered"))
print("Item chosen:",Items[Choice])
print("Money entered:",Payment)
print("Change: ",Payment-Prices[Choice])
