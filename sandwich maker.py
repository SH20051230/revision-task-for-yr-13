def price_calculator():
    total_price = 0
    bread_price = 0
    wholemeal = ["wholemeal"]
    white = ["white"]
    chessy_white = ["chessy white"]
    choice = input("what do you want for bread: ")
    if choice in wholemeal:
        bread_price += 1
    elif choice in white:
        bread_price += 0.8
    elif choice in chessy_white:
        bread_price += 1.2
    else:
        bread_price += 1.4
    total_price += bread_price





    meat_price = 0
    chiken = ["chiken"]
    beef = ["beef"]
    salami = ["salami"]
    vegan_slice = ["vegan slice"]
    meat_choice = input("what do you want for meat: ")
    if meat_choice in chiken:
        meat_price += 2.69
    elif meat_choice in beef:
        meat_price += 3
    elif meat_choice in salami:
        meat_price += 4
    else:
        meat_price += 3.3
    total_price += meat_price



    garnish_price = 0
    onion = ["onion"]
    tomato = ["tomato"]
    lettuce = ["lettuce"]
    chesse = ["chesse"]
    garnish_choice = input("what's your choice of garnish: ")
    if garnish_choice in onion:
        garnish_price += 1.69
    elif garnish_choice in tomato:
        garnish_price += 1
    elif garnish_choice in lettuce:
        garnish_price += 2
    else:
        garnish_price += 2.5
    total_price += garnish_price

    print(f"your sandwich total cost is {total_price}")




price_calculator()
answer = ""
while not answer:
 changes = input("do you want to make change to your order:"
                "press Y for yes N for no")
 if changes == "Y":
    price_calculator()
 else:
     break
