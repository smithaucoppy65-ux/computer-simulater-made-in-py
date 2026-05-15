import os
import time
import math


print("="*40)
print("Welcom to the computer simulater!")
print("="*40)
print("Slect a option below:")
print("1. Print pi")
print("2. More info")
print("3. cookies")
print("4. print in %")
print("5. prints 67")
print("6. <coming soon>")
print("="*40)

while True:

    cookie = "Cookies are the best! "*9999

    choice = input("Option: ")


    if choice == "1":
        print(math.pi)
    
    elif choice == "2":
       print("="*50)
       print("More info:")
       print("This was built By Smith.")
       print("This is 100% independent.")
       print("I'am a cookie lover.")
       print("="*50)
 
    elif choice == "3":
       print(cookie)
       
    elif choice == "4":
        for i in range(1, 101):
            print(f"{i}%")
            time.sleep(99.99)
    
    elif choice == "5":
        print("67 "*67)

    elif choice == "6":
        print("This optioon is still in development.")
        print("check back later incase this option is")
        print("availible.")
                                                                                                                                                                    
    else:
       print("That option is not availile or hasn't been added!")