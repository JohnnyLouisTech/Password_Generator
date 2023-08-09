# ---Password Genarator start here----//
import string
import random

print("Hello, welcome to password generator!")
length = int(input("Enter the lenght of your password: "))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

all = lower + upper + num + symbols

sample = random.sample(all, length)
password = "".join(sample)
print(password)
