import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

createList = [rock, paper, scissors]

userInput = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissor.\n"))

if userInput > 2 or userInput < 0:
    print("Invalid Input range. Please type the correct input number ex(0, 1, 2)")
else:
    print(createList[userInput])

    randomInput = random.randint(0, (len(createList) - 1))

    print(f"Computer chose:\n{createList[randomInput]}")

    if userInput == 0 and randomInput == 1:
        print("You Lose")
    elif userInput == 0 and randomInput == 2:
        print("You Win")
    elif userInput == 1 and randomInput == 0:
        print("You win")
    elif userInput == 1 and randomInput == 2:
        print("You Lose")
    elif userInput == 2 and randomInput == 0:
        print("You Lose")
    elif userInput == 2 and randomInput == 1:
        print("You Win")
    elif userInput == randomInput:
        print("Draw")
    elif userInput > 2:
        print("Input Error. Input is out of range")
    else:
        print("Nothing Here")

