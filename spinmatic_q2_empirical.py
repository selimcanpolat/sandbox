die_1 = [2,3,5,7,11,13]
die_2 = [2,3,5,7,11,13]
import random

expected_sum = 0
test_cases = 100000
for i in range(test_cases):
    sum = 0
    throw = 0
    while sum < 37:
        first = die_1[random.randint(0,5)]
        second = die_2[random.randint(0,5)]
        throw += 1
        sum += first+second
    prize = 37*throw
    expected_sum += prize
expected_value = expected_sum/test_cases
print(expected_value)

