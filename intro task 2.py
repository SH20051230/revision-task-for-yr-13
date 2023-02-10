# Intro task 2

fish = ["flouder", "sole", "blue cod", "snapper", "terakihi", "john dory",
        "red cod"]
print("a. First letter of each fish name on a new line: ")
for item in fish:
    print(item[0])

print("b. First three letters of each fish name: ")
for item in fish:
    print(item[0:3])

print("c. The longest fish name is: ")
largest = ""
for item in fish:
    if len(item) > len(largest):
        largest = item
print(largest)

print("d. fish name that's more than 1 word are: ")
for item in fish:
    if " " in item:
        print(item)

print("e. the fish name contain cod are: ")
for item in fish:
    if "cod" in item:
        print(item)

