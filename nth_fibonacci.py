
def nth_fibonacci(n):

    if n == 0:

        return 0

    elif n == 1:

        return 1

    elif n<0:

        return "invalid input"

    else:

        i0 = 0

        i1 = 1

        for j in range(n-1):

            i2 = i1 + i0

            i0 = i1

            i1 = i2

        return i2

while True:

    a = int(input())

    print(nth_fibonacci(a))

