# Intro task 3
# letter couter
e_times = 0
sentence = []
sentence_entered = input("Enter any sentence you like: ")
sentence.append(sentence_entered)
for item in sentence:
    if "e" in item:
        e_times += 1
    else:
        e_times += 0
print(e_times)

