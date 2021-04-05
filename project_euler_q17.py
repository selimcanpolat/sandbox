import inflect
p = inflect.engine()
letters = ""
for i in range(1,1001):
    a = p.number_to_words(i)
    letters+=a
letters_list=[]
for i in letters:
    if i != " " and i != "-":
        letters_list.append(i)
print(len(letters_list))

