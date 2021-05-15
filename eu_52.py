from itertools import permutations
i = 0
while True:
    i += 1
    i = str(i)
    p = permutations(i,len(i))
    perm_list = []
    for j in p:
        num_str = ""
        for k in j:
            num_str += k
        num_str = int(num_str)
        perm_list.append(num_str)
    perm_list = set(perm_list)
    i = int(i)
    bool_list = []
    for k in range(2,7):
        if i*k in perm_list:
            bool_list.append(1)
    if bool_list.count(1) == 5:
        print(i)
        break