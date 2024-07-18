import random

counter = 0
sum = 0
random_number = 0
while counter<10:
  random_number = random.randint(1,20)
  sum += random_number
  counter += 1
print(sum/10)



