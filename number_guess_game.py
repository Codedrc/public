player = input("type a your name = " )
import random

top_of_range = input("type a number= " )
 
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
      print("please type the numbuer larger than 0 next time ")
    else:
       print("please type a number next time")

random_number = random.randint(0,top_of_range)
guess = 0 

while True:
    guess += 1 
    user_guess = input("make a guess = " )
    if user_guess.isdigit():
      user_guess = int(user_guess)
    else:
      print("type a number next time.")
      continue
   
    if user_guess == random_number:
      print("nice you got it  :)")
    elif user_guess > random_number:
     print("you are above the number!")
    else:
     print("youy are below the number!")
    break


