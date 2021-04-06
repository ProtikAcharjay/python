n=11
guess=1
print("Welcome to guessing game", "Here you have to guess the number bitween 1 to 20")
print("You have 9 guesses")
while(guess<10):
    inp= int(input("your choice: "))
    if inp==n:
        print("Contrats you guessed right")
        break
    elif 0<inp<11:
        print("Lesser than expected number")
    elif 11<inp<=20:
        print("Greater than expected number")
    else:
        print("Invalid Input")
    print(9-guess,"No of guesses left")
    guess=guess+1
if guess>9:
    print("Game Over")