# print (int(round(5.3)))
# print (int("54"))

# print (float(54))

# print (type(str(54)))
# print (type(str(5.4)))

# print ("what is your name?")
# name=input()

# if name:
#     print(f"Hello {name}")
# else:
#     print("You did not provide a name")

# bool = True
# if not bool:
#     print(False)
# else:
#     print(True)

# def add_up():
#     num1 = input("What is the first number?")
#     num2 = input("What is the second number?")

#     try:
#         print(f"{num1} + {num2} is {int(num1) + int(num2)}")

#     except:
#         print("Error!")
#         print("********************")
#         add_up()

# add_up()


# light = False

# def light_switch():
#     global light 
#     if light:
#         print("Whoa! It's bright in here") 
#         light = False
#     else:
#         print("Who turned out the lights?")
#         light = True
# light_switch()
# light_switch()

# balance = 100     # a global variable

# def cash_withdraw(amount): 
#     global balance
#     print(f"Your balance is {balance}")
#     print(f"You are withdrawing {amount}")
#     balance -=amount
#     print(f"your new balance is {balance}")

# cash_withdraw(int(input("amount")))
# cash_withdraw(20)
# cash_withdraw(20)
# cash_withdraw(20)



                ################################################
                #                                              #
                #              Activity 1                      #
                #                                              #
                ################################################

def num_check():         # a function called num_check - it doesn't take any parameters in this case
    num=input("Please type in a number")      # take an input from the user

    try:     # the program will attempt to do this line WITHOUT any fatal errors
        num=int(num) # casting - changing the data type to an int, because input is always a string
        print(f"The number you picked is {num} and it is a {type(num)}") #type prints the type of the data - this was asked for in the brief!
    except:  # if a fatal error does occur - this will happen instead
        print("This is not an integer - try again") # try again message
        num_check()   # self-recursive to give the user the chance to try again

num_check() #calling the function