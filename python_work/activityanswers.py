
# test_string = "Welcome to Code Nation"
# string_len=len(test_string)

# def phrase_checker():
#     if string_len%2==0:
#         print(f"The length of the string \"{test_string}\" is {string_len} and it is even")
#     else:
#         print(f"The length of the string \"{test_string}\" is {string_len} and it is odd")

# phrase_checker()

alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u", "v", "w","x","y","z"]

for letter in alpha:
    print(letter)

def letter_num():
    user_num=input("please enter a number between 1 and 26:    >")
    user_num=int(user_num)
    user_num -=1
    if user_num >=0 and user_num <=26:
        print(alpha[user_num])
    else:
        print("Invalid entry please try again")
        letter_num()

letter_num()