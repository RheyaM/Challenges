import random
playagain="yes"
while playagain=="yes":
  A=0
  print("1:stay silent, 2:confess")
  while A!=1 and A!=2:
    try:
      A=(int(input("Input Prisoner A's choice")))
    except:
      print("Input 1 or 2 based on your choice")
  B=random.randint(1,2)
  if A==B:
    if A==1:
      print("prisoner 2 also chose to stay silent, both are in prison for 1 year")
    else:
      print("prisoner 2 also chose to confess, both are in prison for 5 years")
  else:
    if A==1:
      print("prisoner 2 chose to confess, you stay in prison for 20 years, and prisoner 2 goes free")
    else:
      print("prisoner 2 chose to stay silent, prisoner 2 is in prison for 20 years, and you go free")
  playagain=input("play again? Input 'yes' for yes and 'no' for no")
