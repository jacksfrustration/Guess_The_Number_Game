import random as rand

loop=True
playing=True
while loop:
    #starts game unless user types no
    play=input("Do you want to play?\n"
               "Game will start unless you type 'no'\n").lower()
    if play=="n" or play=="no":
        playing=False
    #generate a number
    number = rand.randint(0, 101)
    #gets a difficulty input to determine amount of lives
    difficulty = input("What difficulty would you like to choose?\n"
                       "Type 'easy' or 'hard'\n").lower()

    if difficulty=="easy":
        lives=10
    elif difficulty=="hard":
        lives=5
    else:
        #if difficulty input is anything other than easy or hard it prints out an error message and breaks out of the loop
        print(f"{difficulty.title()} is not available as an option. Try again")
        continue
    while playing:
        #try to get a guess and check the number if it is too high too low or right.
        # if right it breaks out of the indented while loop and prints out an appropriate message
        try:
            guess=int(input("Make a guess:\n"))
            if guess >100:
                print(f"{guess} was not in a range from 1 to 100\n"
                      f"Try again!!\n"
                      f"No lives wasted\n")
                continue
            if guess>number:
                lives-=1
                print(f"{guess} was not correct!!\n"
                      f"The guess was too high!!\n"
                      f"You have {lives} lives left!!\n")
            elif guess<number:
                lives -= 1
                print(f"{guess} was not correct!!\n"
                      f"The guess was too low!!\n"
                      f"You have {lives} lives left!!\n")
            else:
                print(f"You got it right!!\n"
                      f"{guess} was the number\n"
                      f"You had {lives} lives left")
                break
        except ValueError:
            #if the guess the user inputted is not a number break out of the loop and print out an appropriate message
            print(f"Input is not a number. Restarting game")
            break