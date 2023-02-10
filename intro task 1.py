# Intro task 1
# Secret pin program

secret_pin = ""
while not secret_pin:
    secret_pin = input("enter your secret 4-digit PIN: ")
    if secret_pin == "0456":
        print(f"Your secret pin is {secret_pin}")
        break
    else:
        secret_pin == ""
        print("Wrong")
