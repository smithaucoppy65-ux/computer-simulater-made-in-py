import os
import time
import math
import sys


print("="*50)
print("Welcom to the computer simulater!")
print("="*50)
print("Slect a option below:")
print("1. Print pi")
print("2. More info")
print("3. cookies")
print("4. print in %")
print("5. prints 67 67 times")
print("6. loading...")
print("7. please dont use this option, just don't.")
print("8. 7 applyes to me as well")
print("9. <coming soon>")
print("="*50)

while True:

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
       print("I'am a cookie lover.")
       time.sleep(1.6)
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
        for i in range(1, 1388):
            print(f"\rLoading: {i}%", end="", flush=True)
            time.sleep(1.7e+3)
            print()
            print("An ERROR occurred while deleting important system files!")

    
    elif choice == "7":
        print("why??????????????????????????????")
        time.sleep(1.0)
        print("I hate you")
        time.sleep(1.0)
        print("i told you not to!!!!!!! >:((((((")
        time.sleep(1.0)
        print("i told you not to i wish you cold lisen >>>:((((((((((((((((")
        print("since chose this option time to let you wait about 99.99 seconds then you get the main menue again")
        time.sleep(99.99)
        #LOL to however uses it they wont see the main menue in about 99.99 seconds

    elif choice == "8":
        print("loding option_8.exe...")
        time.sleep(5.0)
        print("please wait...")
        time.sleep(9.9)
        print(r"Can't find /localhost/pc:99856/conection/user/geust/99/acsec/true/edit=false\Desktop\pc simu\options\8\option_8.exe")

    elif choice == "9":
        print("This optioon is still in development.")
        print("check back later incase this option is")
        print("availible.")


                                                                                                                                                                    
    else:
       print("That option is not availile or hasn't been added!")
