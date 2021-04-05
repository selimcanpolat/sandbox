
def isprime(n):

    if n == 1:

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

num = int(input())

for i in range(2,1000000000000000):

    while num%i==0:

        print(i)

        num = num/i


