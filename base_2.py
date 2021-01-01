
def base_2(num):

    list = []

    while True:

        q = num // 2

        r = num % 2

        num = num // 2

        list.append(r)

        if q == 1 :

            list.append(q)

            break

    sum = 0

    for i in range(len(list)):

        sum += list[i]*(10**i)

    return sum

n = int(input())

print(base_2(n))

