
# take an input n. print the nth prime.

def isprime(var):

    if var == 1:

        return False

    elif var == 2:

        return True

    else:

        for i in range(2,var):

            if var%i==0:

                return False

            else:

                continue

        return True

n = int(input())

primes_list = []

i = 0

while True:

    if len(primes_list)==n:

        break

    i += 1

    if isprime(i):

        primes_list.append(i)

    else:

        continue

print(primes_list[n-1])















