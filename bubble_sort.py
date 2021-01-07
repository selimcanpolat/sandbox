
list = []

import random

for i in range(random.randint(10,40)):

    list.append(random.randint(1,100))

print(list)

while list != sorted(list):

    for i in range(len(list)-1):

        if list[i] > list[i+1]:

            list[i], list[i+1] = list[i+1] , list[i]

        else:

            continue

print(list)







