import os
import time
import math
import sys
import random


print("="*50)
print("Welcome to the computer simulator!")
print("="*50)
print("Select an option below:")
print("1. Print pi")
print("2. More info")
print("3. cookies")
print("4. print in %")
print("5. prints 67 67 times")
print("6. loading...")
print("7. please dont use this option, just don't.")
print("8. 7 applies to me as well")
print("9. Rock, Paper, Scissors")
print("10. <coming soon>")
print("="*50)

choices = ["rock", "paper", "scissors"]

while True:

    computer = random.choice(choices)

    cookie = "Cookies are the best! "*9990

    choice = input("Option: ")


    if choice == "1":
        print(math.pi)
    
    elif choice == "2":
       print("="*50)
       print("More info:")
       time.sleep(1.3)
       print("This was built By Smith.")
       time.sleep(1.4)
       print("This is 100% independent.")
       time.sleep(1.5)
       print("I'm a cookie lover.")
       time.sleep(1.6)
       print("="*50)
  
    elif choice == "3":
       print(cookie)
        
    elif choice == "4":
         for i in range(1, 101):
             print(f"{i}%")
             time.sleep(0.1)
     
    elif choice == "5":
         print("67 "*67)

    elif choice == "6":
         for i in range(1, 101):
             print(f"\rLoading: {i}%", end="", flush=True)
             time.sleep(0.05)
         print()
         print("Loading complete!")

    
    elif choice == "7":
         print("why??????????????????????????????")
         time.sleep(1.0)
         print("I hate you")
         time.sleep(1.0)
         print("i told you not to!!!!!!! >:((((((")
         time.sleep(1.0)
         print("i told you not to i wish you could listen >>>:((((((((((((((((")
         print("since you chose this option time to let you wait about 2 seconds then you get the main menu again")
         time.sleep(2.0)

    elif choice == "8":
         print("loading option_8.exe...")
         time.sleep(5.0)
         print("please wait...")
         time.sleep(9.9)
         print(r"Can't find /localhost/pc:99856/connection/user/guest/99/access/true/edit=false\Desktop\pc simu\options\8\option_8.exe")

    elif choice == "9":
         print("="*50)
         print("Rock, Paper, Scissors!")
         print("="*50)
         print("Choose: (R)ock, (P)aper, or (S)cissors")
         player = input("Your choice: ").lower()
         
         if player == "r":
             player = "rock"
         elif player == "p":
             player = "paper"
         elif player == "s":
             player = "scissors"
         else:
             print("Invalid choice! Please enter r, p, or s.")
             continue
         
         print(f"Computer chose: {computer}")
         
         if player == computer:
             print("It's a tie!")
         elif (player == "rock" and computer == "scissors") or \
              (player == "paper" and computer == "rock") or \
              (player == "scissors" and computer == "paper"):
             print("You win!")
         else:
             print("You lose!")
         print("="*50)

    elif choice == "10":
         print("This option is still in development.")
         print("check back later in case this option is")
         print("available.")

    else:
       print("That option is not available or hasn't been added!")
