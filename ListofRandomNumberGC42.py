import random
list=[]
for x in range(50):
  number=random.randint(0,100)
  list.append(number)
print(list)
Min=101
for x in range(50):
  if list[x]<Min:
    Min=list[x]
print("Minimum is: ",Min)
Max=0
for x in range(50):
  if list[x]>Max:
    Max=list[x]
print("Maximum is: ",Max)
Total=0
for x in range(50):
  Total=Total+list[x]
Average=Total/50
print("Average is: ",Average)
