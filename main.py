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
list1 = [rock, paper, scissors]
user_input = int(input("What do you choose? Type 0 for Rock 1 for Paper 2 for Scissors \n"))
comp_input = random.randint(0, 2)
if user_input > 2 or user_input < 0:
    print("You entered an invalid no.You Lose!")
else:
    print(list1[user_input])
    print(f"Computer Choose:\n {list1[comp_input]}")
    if user_input == comp_input:
        print("It's a Draw")
    elif user_input == 0 and comp_input == 2:
        print("You Won")
    elif user_input == 2 and comp_input == 0:
        print("You Lose")
    elif comp_input > user_input:
        print("You Lose")
    elif user_input > comp_input:
        print("You Win")
