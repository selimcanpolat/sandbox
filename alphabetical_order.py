
# take a string and reorder it according to its ascii values. THIS IS ALPHABETICAL ORDER OMG...



n = input("\nplease enter a string\n")

list = list(n)

list2 = []

for i in range(len(n)):

    list2.append(ord(list[i]))

list2 = sorted(list2)

for i in range(len(list2)):

    print(chr(list2[i]), end="")








