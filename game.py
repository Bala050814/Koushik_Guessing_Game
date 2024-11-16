import random as rs

def two_digit():
    computer_guess=rs.randint(10,100)
    attempts=0

    print("I am thinking number between 10 to 100.")

    while True:
        user_guess=int(input("Enter your guess:"))
        attempts+=1
         
        if user_guess < computer_guess:
               print("Too low!Try again")
        elif user_guess > computer_guess:
               print("Too high!Try again")
        elif user_guess == computer_guess:
               print("Congratulations! You've gussed the number {} in {} attempts.".format(computer_guess,attempts))
               break
        else:
            print("Please enter a valid number:")


def three_digit():
    computer_guess=rs.randint(100,1000)
    attempts=0

    print("I am thinking number between 100 to 1000.")

    while True:
        user_guess=int(input("Enter your guess:"))
        attempts+=1
       
        if user_guess < computer_guess:
               print("Too low!Try again")
        elif user_guess > computer_guess:
               print("Too high!Try again")
        elif user_guess == computer_guess:
               print("Congratulations! You've gussed the number {} in {} attempts.".format(computer_guess,attempts))
               break
        else:
            print("Please enter a valid number:")

def four_digit():
    computer_guess=rs.randint(1000,10000)
    attempts=0

    print("I am thinking number between 1000 to 10000.")

    while True:
        user_guess=int(input("Enter your guess:"))
        attempts+=1
       
        if user_guess < computer_guess:
               print("Too low!Try again")
        elif user_guess > computer_guess:
               print("Too high!Try again")
        elif user_guess == computer_guess:
               print("Congratulations! You've gussed the number {} in {} attempts.".format(computer_guess,attempts))
               break
        else:
            print("Please enter a valid number:")

def guessing_game():
    print("Welcome to guessing game!!")
    number_of_digit =(input("Enter the number of digits you are going to guess(two , three, four)"))
    if number_of_digit == "two":
        two_digit()
    elif number_of_digit == "three":
        three_digit()



if __name__ == "__main__":
    guessing_game()