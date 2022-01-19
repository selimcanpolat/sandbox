import random 
import time
random_integers = []
while True:
    lower_bound = random.randint(-1000,1000)
    upper_bound = random.randint(-1000,1000)
    if lower_bound<upper_bound:
        random_element = random.randint(lower_bound,upper_bound)
    elif lower_bound>upper_bound:
        random_element = random.randint(upper_bound,lower_bound)
    else:
        random_element = random.randint(-1000,1000)
    random_integers.append(random_element)
    moving_ave = sum(random_integers)/len(random_integers)
    time.sleep(0.2)
    print(moving_ave)
