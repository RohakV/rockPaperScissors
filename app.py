from random import randint

def route():
    behindTheScenes()
    start()


def behindTheScenes():
    randomize = randint(1, 3)
    if randomize == 1:
        global aiChoose
        aiChoose = "rock"
    elif randomize == 2:
        aiChoose = "paper"
    elif randomize == 3:
        aiChoose == "scissors"




def start():
    print("Welcome to Rock Paper Scissors")
    temp = input("Do you want to start (y or n)?")
    if temp.lower() == "y":
        print("You said yes")
        game()
    elif temp.lower() == "n":
        print("You said no")
        quit()


def game():
    user_input = input("Rock, Paper or Scissors?: ")
    if user_input.lower() == "rock":
        print("You chose rock")
        print("waiting for AI to choose")
        print(".")
        print(".")
        print(".")
        if aiChoose == "rock":
            print("AI chose rock, you chose rock, it is a duel!")
            route()
        elif aiChoose == "paper":
            print("AI chose paper, you chose rock, paper wraps around rock, you lose!")
            route()
        elif aiChoose == "scissors":
            print("AI chose scissors, you chose rock, rock smashes scissors, you win!")
            route()
    elif user_input.lower() == "scissors":
        print("You chose scissors")
        print("waiting for AI to choose")
        print(".")
        print(".")
        print(".")
        if aiChoose == "rock":
            print("AI chose rock, you chose scissors, rock smashes scissors, you lose!")
            route()
        elif aiChoose == "paper":
            print("AI chose paper, you chose scissors, scissors cuts through paper, you win!")
            route()
        elif aiChoose == "scissors":
            print("AI chose scissors, you chose scissors, it is a duel!")
            route()
    elif user_input.lower() == "paper":
        print("You chose scissors")
        print("waiting for AI to choose")
        print(".")
        print(".")
        print(".")
        if aiChoose == "rock":
            print("AI chose rock, you chose paper, paper wraps around rock, you win!")
            route()
        elif aiChoose == "paper":
            print("AI chose paper, you chose paper, it is a duel!")
            route()
        elif aiChoose == "scissors":
            print("AI chose scissors, you chose paper, scissors cuts through paper, you lose!")
            route()


route()