
txt = input("Enter a word;")
char_to_insert = "_"
result = ""
vowels = ("u", "a", "i", "o", "e")


for char in range(0, len(txt), 3):
    third = txt[char:char+3]
    if third.endswith(vowels):
       result += txt[char:char+3+1] + char_to_insert 
    else:
        result += txt[char:char+3] + char_to_insert 
   
print(result.rstrip("_"))



##2.

numbers = int(input("Enter number(1/20)"))

count = 0

while count <= numbers:
    print(count, count**2)
    count +=1



##3.
# count = 1
# while count <=10:
#     print(count)
#     count +=1



# for x in range(1, 6):
#     for y in range(1, x+1):
#         print(y, end = " ")
#     print()

##


number = int(input("Create a number!"))
count = 0
listt = []

while count <= number:
    print(count)
    listt.append(count)
    count+=1
print(sum(listt))



##4.
number = int(input("Enter a number!"))

for i in range(1, 11):
    print(number * i)




##6.

numbers = input("Enter your number!")
Digitcount = len(numbers)
print(Digitcount)



##7.
for i in range(5, 0, -1): # 5 dan boshlab 1 gacha ketma ket reverse likni chiqaradi
    for y in range (i, 0, -1): # i dan boshlab 1 gacha sonlar ni oladi 
        print(y, end = " ") # bu y dan chiqgan natijani oladi
    print() # har bir qator iteration bo'lganida bitta qator tashlaydi




##8.
list1 = [10, 20, 30, 40, 50]

for n in reversed(list1):
    print(n)


  ##9
count = -10

while count < -1:
    print(count)
    count += 1
print(count)


##10
  count = 0 

while count <= 4:
    print(count)
    count += 1
print("Done!")



  ##11.
 number = int(input("Enter the number you want to check:"))

for i in range(2, number):
    if number % i == 0:
        print("This is not a prime number!")
        break
else:
    print("This is a Prime number!") 
  





##12  
def fibanc(n):
    if n == 1 or n == 2:
        return 1
    return fibanc(n - 1) + fibanc(n -2)
print(fibanc(8))



  ##13
number = int(input("Enter a number"))
f = 1

for i in range(1, number+1):
    f = f * i
print(f)



  ## 14

# # list1 = [1, 1, 2]
# # list2 = [2, 3, 4]

# # uncommonlist = []

# # un1 = [x for x in list1 if x not in list2]
# # unc2 = [x for x in list2 if x not in list1]

# # print(un1 + unc2)


# ##

# list1 = [1, 2, 3]
# list2 = [4, 5, 6]

# common = set(list1) & set(list2)
# uncommon_list = []

# # 1- list uchun uncommmon larini ajratib oldik
# for x in list1:
#     if x not in common:
#         uncommon_list.append(x)

# ## 2-lsit uchun uncommon one lari
# for y in list2:
#     if y not in common:
#         uncommon_list.append(y)

# print(uncommon_list)


###


ist1 = [1, 1, 2, 3, 4, 2]
list2 = [1, 3, 4, 5]

common = set(ist1) & set(list2)

unc_list = []

for x in ist1:
    if x not in common:
        unc_list.append(x)

for y in  list2:
    if y not in common:
        unc_list.append(y)

print(unc_list)
