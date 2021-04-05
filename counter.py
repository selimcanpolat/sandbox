with open(r"C:\Users\Selim Can\Desktop\New Text Document.txt") as file:
    dict_list = []
    for line in file:
        pol_score = int(line[::-1][:3][::-1])
        index = len(line)-len(str(pol_score))
        word = line[:(index-1)].strip()
        dictionary = {"word":word,"polarity score":pol_score}
        dict_list.append(dictionary)
sentence = "If you don't apologize, I will not accept any more calls."
word_list = sentence.split(" ")
punctuations = list("!\"#$%&'()*+,.-/:;<=>?@[\]^_`{|}~")
new_word_list = []
for i in word_list:
    i = i.lower()
    i = list(i)
    for j in punctuations:
        if j in i:
            i.remove(j)
    new_word = ""
    for k in i:
        new_word += k
    new_word_list.append(new_word)
negations = ["not", "no", "don't", "didn't", "wasn't", "weren't", "can't",
             "couldn't", "isn't", "aren't", "haven't", "hasn't", "hadn't"]
words_list = []
for j in dict_list:
    words_list.append(j["word"])
def polarity_score(sentence):
    final_score = 0
    for i in word_list:
        if "-" in i or "'" in i:
            punctuations = list("!\"#$%&()*+,./:;<=>?@[\]^_`{|}~")
            i = list(i)
            new_i = ""
            for k in punctuations:
                if k in i:
                    i.remove(k)
            for m in i:
                new_i += m
            i = new_i
            for j in dict_list:
                if i == j["word"]:
                    final_score += j["polarity score"]
        else:
            ind = word_list.index(i)
            for j in dict_list:
                if new_word_list[ind] == j["word"]:
                    index = word_list.index(i)
                    if word_list[index-1] in negations:
                        j["polarity score"] = j["polarity score"]*(-1)
                    final_score += j["polarity score"]
    return final_score
def capitalizer(sentence):
    new_sent = ""
    sentence = str(sentence)
    sentence = sentence.split(" ")
    for i in sentence:
        index = sentence.index(i)
        if new_word_list[index] not in words_list:
            if i not in negations:
                new_sent += i + " "
            else:
                if new_word_list[index+1] not in words_list:
                    new_sent += i + " "
                else:
                    i = i.upper()
                    new_sent += i + " "
        else:
            i = i.upper()
            new_sent += i + " "
    return new_sent
output_sentence = capitalizer(sentence)
total_polarity = polarity_score(sentence)
print(output_sentence)
print(total_polarity)

