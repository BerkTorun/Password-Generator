import random
import string

def randomLetter():
    str1 = random.choice(string.ascii_letters)
    return str1

def randomNumber():
    str2 = str(random.randint(0, 10))
    return str2

password = ''
password_length = int(input("Please enter the passwod length : "))


for _ in range(password_length):
    func_choice = random.randint(1,2)
    if func_choice == 1:
        password = password.__add__(randomLetter())
    else:
        password = password.__add__(randomNumber())

print("Password --> ",password)
