number=1
for x in range(2,22):
  if number%3==0 and number%5==0:
    print("FizzBuzz")
  elif number%3==0:
    print("Fizz")
  elif number%5==0:
    print("Buzz")
  else:
    print(number)
  number=number+1
