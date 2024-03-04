import random
import pyttsx3 

engine = pyttsx3.init() 


letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
           'n','o','p','q','r','s','t','u','v','w','x','y','z',
           'A','B','C','D','E','F','G','H','I','J','K','L','M',
           'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
symbols = ['#','!','@','$','%','*','_','^','&']
numbers = ['1','2','3','4','5','6','7','8','9','0']
password_list = []


print("WELCOME TO PASSWORD GENERATOR ")
engine.say("WELCOME TO PASSWORD GENERATOR ")
engine.runAndWait()

print("YOU CAN GENERATE PASSWORDS  HERE ...")
engine.say("YOU CAN GENERATE PASSWORDS  HERE ...")
engine.runAndWait()

engine.say("Enter no of letters: ")
engine.runAndWait()
n_letters = int(input("Enter no of letters: "))

engine.say("Enter no of symbols: ")
engine.runAndWait()
n_symbols = int(input("Enter no of symbols: "))

engine.say("Enter no of numbers: ")
engine.runAndWait()
n_numbers = int(input("Enter no of numbers: "))


for i in range(1,n_letters+1):
    char = random.choice(letters)
    password_list += char

for i in range(1,n_symbols+1):
    char = random.choice(symbols)
    password_list += char 

for i in range(1,n_numbers+1):
    char = random.choice(numbers)
    password_list += char

random.shuffle(password_list)
password = ""
for char in password_list:
    password += char 

engine.say("Here your password is....")
engine.runAndWait()
print(password)