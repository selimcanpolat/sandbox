
def divisors(m):

    divisors = []

    for i in range(1,m+1):

        if m%i==0:

            divisors.append(i)

        else:

            continue

    print(divisors)


n = int(input())

divisors(n)









