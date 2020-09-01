import random
Name=input("Input name")
Insults=[(Name,"You’re a grey sprinkle on a rainbow cupcake."),(Name,"is more disappointing than an unsalted pretzel"),("Light travels faster than sound which is why",Name, "seemed bright until they spoke"),(Name,"has so many gaps in their teeth it looks like their tongue is in jail."),("It’s impossible to underestimate",Name),(Name,"brings everyone so much joy, when they leave the room")]
ChoiceInsult=random.choice(Insults)
print(ChoiceInsult)
