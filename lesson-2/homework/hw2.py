##1
from datetime import datetime 

name = input("what is your name?")
DOB = int(input("When were you born?"))
current_year = datetime.now().year
age = (current_year - DOB)

print("User's name is", name)
print("User's age is", age)

##2

txt = 'LMaasleitbtui'
first_car = print(txt[1::2])
second_car = print(txt[0::2])

##3.
txt = 'MsaatmiazD'

first_car = print(f"{txt[0:-1:2]}")
second_car = print(txt[::-1][0:-1:2])

##4. 
txt = "I'am John. I am from London"

splitting = (txt.split())
print(splitting[-1])

##5.
inputt = input("Enter any word you want to reverse")
print(inputt[::-1])

##6. 
 word = input("Enter any word you want to count its voewl letters!")

count = 0 

 for char in word.lower():
     if char in "auioe":

         count +=1

 print("your word contains", count, "voewls")

##7.
numbers = input("Enter your numbers:").split()
if numbers.count(numbers) == 1:
    print(numbers)
else:
nums = [int(n) for n in numbers]

print(max(nums))

##8.
word = input("Enter your word")
    
if word == word[::-1]:
    print("Palindrome!")
else:
    print("This word is not Palindrome")



##9

print("Domain Extractor")


Email = input("Enter your Email address").strip()

if "@" in Email:
    domain = (Email[Email.find("@")+1:])

    if len(domain) >= 2:
        print('Domain:', domain)

    else:
        print("Invalid Email Address, Your email is too short")
else:
    print("Invalid Email Address, '@' not found. ")

##10.
import string 
import random 

length = int(input("Enter password length:"))

letters = string.ascii_letters
digits = string.digits 
string = string.punctuation 

all_chars = letters + digits + string

password = "".join(random.choice(all_chars) for i in range(length))

print("Password:", password)





