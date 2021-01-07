
def label_encoder(string):

    init = ""

    for char in string:

       init += str(ord(char))

    init = int(init)

    def base_2(num):

        list = []

        while True:

            q = num // 2

            r = num % 2

            num = num // 2

            list.append(r)

            if q == 1 :

                list.append(q)

                break

        sum = 0

        for i in range(len(list)):

            sum += list[i]*(10**i)

        return sum

    result = base_2(init)

    return result
