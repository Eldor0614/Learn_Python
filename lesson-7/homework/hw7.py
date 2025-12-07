##1.

def is_prime(num):
    if num <=1:
        return False # prime number 1 yoki undan kichik songa teng bo'lmaydi
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False 
    return True

numbers = int(input("Enter your number!")) # user input

is_prime(numbers)



##2.
def digit_sum(k):
    total = 0     # har bir int 0 ga qoshilib boriladi 
    for i in str(k):  # kirgizilgan k value str ga o'tkaziladi
        total += int(i)  # i dagi har bir qiymat int ga aylantirib total ga qo'shiladi
    return total

print(digit_sum(24))



##3.


N = int(input("Enter your number!"))  #user input

def square_calculator():
     result = []     # natijalar uchun list
     for i in range(1, N+1):
          Square = 2 ** i   
          if Square < N:    # loop qayergacha t=dovom etishiligini ko'rsatish
               result.append(Square)
     return result
print(square_calculator())
