from random import randint
pchp = 3
myhp = 3
z = 0
# available weapons => store this in an array
choices = ["Rock", "Paper", "Scissors"]

player = False



# make the computer pick one item at random
computer = choices[randint(0, 2)]


while player is False:
    print("")
    print("=======================")
    print("| CHOOSE YOUR WEAPON  |")
    print("=======================")
    print("Your Health: " + str(myhp))
    print("Computers Health: " + str(pchp))


    player = input("Rock, Paper, Scissors?\n")
    print("Player chooses:", player)

    if (player == computer):
        print("Computer chooses:", computer)
        print("Tie! Live to shoot another day")

    elif player == "Rock":
        if computer == "Paper":
            print("Computer chooses:", computer)
            print("You lose the round,", computer, "covers", player)
            myhp = myhp - 1
        else:
            print("Computer chooses:", computer)
            print("You win the round,", player, "smashes", computer)
            pchp = pchp - 1

    elif player == "Paper":
        if computer == "Scissors":
            print("Computer chooses:", computer)
            print("You lose the round,", computer, "cuts", player)
            myhp = myhp - 1

        else:
            print("Computer chooses:", computer)
            print("You win the round,", player, "covers", computer)
            pchp = pchp - 1

    elif player == "Scissors":
        if computer == "Rock":
            print("Computer chooses:", computer)
            print("You lose the round,", computer, "smashes", player)
            myhp = myhp - 1

        else:
            print("Computer chooses:", computer)
            print("You win the round,", player, "cuts", computer)
            pchp = pchp - 1

    elif player == "Quit":
        exit()

    else:
        print("Not a valid option. Check again, and check your spelling!\n")

    player = False
    computer = choices[randint(0, 2)]

    if pchp is z:
        print(" ______________")
        print("|              |")
        print("|   WINNER!    |")
        print("|______________|")
        print("")
        player = input("Would you like to play again? y / n\n")
        pchp = pchp + 3
        myhp = pchp
        if player == "y":
            player = False
        if player == "n":
            break

    if myhp is z:
        print(" ______________")
        print("|              |")
        print("|   LOSER!     |")
        print("|______________|")
        print("")
        player = input("Would you like to play again? y / n\n")
        myhp = myhp + 3
        pchp = myhp
        if player == "y":
            player = False
        if player == "n":
            break
