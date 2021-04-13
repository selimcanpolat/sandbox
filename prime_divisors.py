number = int(input())

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

div_list = []
for i in range(2,number):
    if number%i==0 and isprime(i):
        div_list.append(i)

print(div_list)
