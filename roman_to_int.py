dict = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

s = input()
sum = 0
n = -1
for i in s:
    n+=1
    if n+1 == len(s):
        sum += dict[s[n]]
    elif dict[s[n+1]]>dict[s[n]]:
        sum += -dict[s[n]]
    else:
        sum += dict[s[n]]

print(sum)

