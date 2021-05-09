a, b = [int(a) for a in input().split()]
a, b = max(a,b), min(a,b)
while True:
    q = a//b
    r = a%b
    if r == 0:
        print(b)
        break
    a,b = b,r


