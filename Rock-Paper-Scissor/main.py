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

game_images = [rock, paper, scissors]
user_points=0
computer_points=0
game_on=True


def score_table(user_points,computer_points):
    points_table=f"""
    |-------------|-----------------|
    |User Points  |Computer Points  |
    |             |                 |
    |{user_points} \t\t\t  |{computer_points} \t\t\t\t|
    |-------------|-----------------|
    
    """
    print(points_table)

def game_check(user_choice,computer_choice):
    global game_on
    global user_points
    global computer_points


    if user_choice >= 3 or user_choice < 0:
        print("You typed an invalid number, you lose!")
    elif user_choice == 0 and computer_choice == 2:
        user_points += 1
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        computer_points +=1
        print("You lose")
    elif computer_choice > user_choice:
        computer_points +=1
        print("You lose")
    elif user_choice > computer_choice:
        user_points +=1
        print("You win!")
    elif computer_choice == user_choice:
        print("It's a draw")

    if user_points >= 10:
        print("Congratulations you achieved it....")
        game_on=False
    elif computer_points >= 10:
        print("Sorry Better Luck Next Time....")
        game_on=False

while game_on:
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors:\n"))
    try:
        print(game_images[user_choice])

        computer_choice = random.randint(0, 2)
        print("Computer chose:")
        print(game_images[computer_choice])
        game_check(user_choice, computer_choice)
        score_table(user_points, computer_points)
    except:
        print("Invalid Input....")








