print(int(5.9))
print(int("54"))
print(int(round(5.8)))

dataa = 5.4

dataa = str(5.4)

print(type(dataa))

# print("What is your name?")
# name=input()

# if name:
#     print(f"Hello {name}")
# else:
#     print("You did not give a name")

# print("What is your name?")

# name=input("   >   ")

# while not name:
#     print("Pelase enter a name")
#     name=input("   >   ")

# print(f"Hello {name}")

def add_up():
    num1 = input("What is the first number you'd like to add up? \n")
    num2 = input("What is the second number you'd like to add up? \n")
    try:
        print(f"{num1} + {num2} is {(int(num1) + int(num2))}!")
    except:
        print("\n ERROR: please input only numerical values. \n")
        print("**************************** \n")
        add_up()
add_up()

