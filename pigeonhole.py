from itertools import combinations

numbers = [1,2,3,4,5,6,7,8,9,10]
y = combinations(numbers,7)

dict_list = []
for i in y:
    x = combinations(i,2)
    list = []
    for j in x:
        if sum(j)==11:
            list.append(j)
            if len(list)==2:
                break
    dict = {i:list}
    dict_list.append(dict)
for i in dict_list:
    print(i)
    print()







