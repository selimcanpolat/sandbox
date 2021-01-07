list = []

import random

for i in range(random.randint(8,9)):

     list.append(random.randint(1,70))

print(list)
print(len(list))

list_test = []

count = 0

while list_test != sorted(list):

     count += 1

     for i in range(len(list)):

          a = random.randint(0,len(list)-1)

          list[i], list[a] = list[a], list[i]

          list_test = list[:]

     print(list_test)

print(count)



