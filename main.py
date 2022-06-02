import random
ewords = {"R": "Rock", "P": "Paper", "S": "Scissors"}
elements = ["R", "P", "S"]
usertick = 5
userchoice = ""
cpuchoice = ""
def confirm():
    print (usertick)
    if usertick == 1: 
        solve()
    else:
        print("ERROR! You failed to select one of the options. Please try again.")
        play()
def play():
    global userchoice
    global cpuchoice
    global usertick
    userchoice = input("Select one of the following: R, P, S\nR for Rock\nP for Paper\nS for Scissors\n")
    cpuchoice = random.choice(elements)
    for e in elements:
        if e == userchoice:
            usertick = 1
    confirm()
def final():
    if userchoice == "P" and cpuchoice == "R":
        print ("Paper covers rock. Player Wins!")
    elif userchoice == "S" and cpuchoice == "P":
        print ("Scissors cuts paper. Player Wins!")
    elif userchoice == "R" and cpuchoice == "S":
        print ("Rock crushes scissors. Player Wins!")
    elif userchoice == "R" and cpuchoice == "P":
        print ("Paper covers rock. CPU Wins!")
    elif userchoice == "P" and cpuchoice == "S":
        print ("Scissors cuts paper. CPU Wins!")
    else:
        print ("Rock crushes scissors. CPU Wins!")
 
def solve():
    print("Player (" + ewords[userchoice] + ") : CPU (" + ewords[cpuchoice] + ")")
    if userchoice == cpuchoice:
        print("There was a tie. Please play again.")
        play()
    else:
        final()
play()