# Intro task 4
# Chracter founder
def charcater_founder(e, sentence):
    e_number = 0
    sentence_check = []
    sentence = input("Enter sentence you want to use: ")
    sentence_check.append(sentence)
    for e in sentence:
        if "e" in e:
            e_number += 1
        else:
            e_number += 0
    return e
charcater_founder()




