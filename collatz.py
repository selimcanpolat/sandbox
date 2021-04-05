
def collatz(n):

    list = []

    while n!=1:

        if n%2==0:

            n = n/2

            list.append(int(n))

        else:

            n = 3*n + 1

            list.append(int(n))

    return list

list2 = []

for i in range(1,1000000):

    a = len(collatz(i))

    list2.append(a)

print(list2.index(max(list2)))



