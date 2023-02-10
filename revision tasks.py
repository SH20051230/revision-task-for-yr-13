# task 6
# sandwich maker
sandwich = input("Wlecome to sandwich maker, press X to exit or continue with any keys: ")
while sandwich != "x":
    Meat_choice = []
    Meat = input("what's your choice of meat: "
                "avaliable choices are Chiken, Beef, Salammi "
                "and Vegan slice")
    if sandwich == "x":
        break
    else:
     Meat_choice.append(Meat)
     Meat = input("do you want add or making any changes? :"
                 "press Y to add or make changes"
                 "Press N to continue on next ingradient")
    if Meat == "N":
        break
    else:
        Meat = input(" do you want to add or change?: "
                     "press A to add "
                     "Press C to change")
        if Meat == "A":
            Meat_added = input("what do you want to add?: ")
            Meat_choice.append(Meat_added)
            print(Meat_choice)
        elif Meat == "C":
            print(Meat_choice)
            Meat_changed = input("what do you want to change?: "
                                 "Please enter which option above you are changing"
                                 "by enter the number of that in the list")

            if Meat_changed == "1":
                Meat = input("what do you want to swap to?: ")
                Meat_choice.pop(0)
                Meat_choice.append(Meat)
                print(Meat_choice)
                Meat = input("do you want add or making any changes? :"
                 "press Y to add or make changes"
                 "Press N to continue on nexy ingradient")

            elif Meat_changed == "2":
                Meat = input("what do you want to swap")
                Meat_choice.pop(1)
                Meat_choice.append(Meat_changed)
            else:
                Meat = input("what do you want to swap")
                Meat_choice.pop(2)

Bread = input("what's your choice of Bread:"
            "avaliable choices are: "
              "Wholemeal")


