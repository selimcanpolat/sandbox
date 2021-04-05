

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

while True:

    num = int(input())

    b = str(num)

    if str(num)==b[::-1] and isprime(num):

        print("palindromic prime")

    else:

        print(":(")

