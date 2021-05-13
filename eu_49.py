def isprime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2,n):
            if n%i==0:
                return False
            else:
                continue
        return True

list = []
from itertools import permutations,combinations

for i in range(1000,10000):
    if isprime(i):
        i = str(i)
        p = permutations(i, 4)
        p_list = []
        for j in p:
            num = ""
            for k in j:
                num += k
            p_list.append(num)
        p_list.append(i)
        new_p = []
        for j in p_list:
            if int(j)>=1000 and  isprime(int(j)):
                new_p.append(j)
        new_p = set(new_p)
        new_p = sorted(new_p)
        if len(new_p)>2:
            c = combinations(new_p,3)
            for k in c:
                diff_1 = int(k[1]) - int(k[0])
                diff_2 = int(k[2]) - int(k[1])

                if diff_2==diff_1:
                    print(k)
                    break
