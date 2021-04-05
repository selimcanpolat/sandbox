

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

i = 0

palindromic_primes = []

while True:

    i += 1

    j = str(i)

    if isprime(i) and j == j[::-1]:

        palindromic_primes.append(i)

        print(palindromic_primes)

    else:

        continue
