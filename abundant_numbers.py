
a = int(input())
b = int(input())

def abundant(num):

    sum_div = 0

    for i in range(2,num):

        if num%i==0:

            sum_div += i

    if sum_div > num:

        return True

for i in range(a,(b+1)):

    if abundant(i):

        print(i, end=" ")















