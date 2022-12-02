name = input("Type your name: ")
print("Welcome,", name, "to this adventure!")

answer = input(
    "You are on a dirt road, it has come to an end and you can go left or right.\n Which way would you like to go? ").lower()

if answer == "left":
    answer = input(
        "You come to river, ypu can walk around it or swim across? \n Type walk to walk around or swim to swim across: ").lower()
    if answer == "swim":
        print("You swam across and were eaten by an alligator.")
    elif answer == "walk":
        print("You walked for many kilometers, ran out of food and then died. You lost!")
    else:
        print("Not a valid input, you lose!")

elif answer == "right":
    answer = input(
        "You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back): ").lower()

    if answer == "cross":
        answer = input(
            "You cross the bridge and meet a stranger, do you wish to talk to them? (yes/no): ").lower()
        if answer == "yes":
            print("You talk to the stranger, they give you gold. You win!")
        elif answer == "no":
            print("You ignore the stranger, they get offended and you lose!")
        else:
            print("Not a valid input, you lose!")

    elif answer == "back":
        print("You go back to the main road and die. You lose!")

    else:
        print("Not a valid option. You lose!")

else:
    print("Not a valid option. You lose!")
