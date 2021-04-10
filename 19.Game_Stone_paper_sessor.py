while(True):
    import random
    computer_score=0
    user_score=0
    round=0
    print("::Welcome to stone paper sessor game::_Developed by Protik Acharjay")
    print("you have 11 chances")
    choice=["s","p","r"]

    for i in range(11):
        print(11-round," chances left..")
        round=round+1
        computer_turn=random.choice(choice)
        user_turn= input("your options: \n's' for stone\n'p' for paper\n'r' for sessor\n")
        if user_turn== "s" or user_turn== "S":
            if computer_turn=="s":
                print("computer choice: s")
                print("Owh it's a tie...")
            elif computer_turn=="p":
                computer_score=computer_score+1
                print("computer choice: p")
                print("Haha I win,,You lose")
            else:
                user_score=user_score+1
                print("computer choice: r")
                print("Ohw you win, nevermind")
        elif user_turn== "p" or user_turn== "P":
            if computer_turn=="s":
                user_score = user_score + 1
                print("computer choice: s")
                print("Ohw you win, nevermind")

            elif computer_turn=="p":
                print("computer choice: p")
                print("Owh it's a tie...")

            else:
                computer_score = computer_score + 1
                print("computer choice: r")
                print("Haha I win,,You lose")
        elif user_turn=="r" or user_turn=="R":
            if computer_turn=="s":
                computer_score=computer_score+1
                print("computer choice: s")
                print("Haha I win,,You lose")
            elif computer_turn=="p":
                user_score=user_score+1
                print("computer choice: p")
                print("Ohw you win, nevermind")
            else:
                print("computer choice: r")
                print("Owh it's a tie...")
        else:
            print("you have entered something wrong. choice from the option you have.")
    print("*"*20)
    print("*"*20)
    if computer_score>user_score:
        print("Yeaaah I win...you loooser,,\nBetter luck next time buddy")
    elif computer_score<user_score:
        print("Owhh you win.. \nyou was lucky")
    else:
        print("What?? How? It's a tie..")
    print("*" * 20)
    print("*" * 20)
