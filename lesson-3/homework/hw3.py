##1
fruits = ["Apple", "Orange", "Peach", "Cherry", "Banana"]
print(fruits[3])


##2.
numset1 = [1, 2, 4, 12, 18]
numset2 = [23, 43, 2, 65, 9]

numset1.extend(numset2)

print(numset1)


##3.

numbers = [1, 3, 15, 16, 19, 13, 12]
first_letter = numbers.pop(0)
middle = numbers.pop(3)
last_letter = numbers.pop()

allRemoved = ([first_letter, middle, last_letter])
print(allRemoved)


##4.
FavouriteMovies = ['Intersteller', 'Erasehead', 'Pulp Fiction', 'The Godfather', 'Come and See']
print(FavouriteMovies)

movies = tuple(FavouriteMovies)
print(movies)
print(type(movies))


##5.
city = input("Enter city name!").lower()
Cities = ["Toshkent", "Paris", "London", "Mascow"]
CitiesLowerCased = [item.lower() for item in Cities]


if city in CitiesLowerCased:
    print(city,"is found")
else:
    print("There is no such city name in the list")


##6.
numbers = [12, 13, 14]
Creating_duplicates = numbers * 3
print(Creating_duplicates)



##7.
numbers = [12, 13, 14, 15, 16]
temp = numbers[0]
numbers[0] = numbers[-1]
numbers[-1] = temp

print(numbers)


##8.
numbers = tuple(range(1,11))
print(numbers[3:7])


##9. 
colors = ["blue", "red", "orange", "black", "white", "purple", "blue"]
colors.count("blue")



##10.

animals = ("Ant", "Lion" ,"Zebra", "Giraffe", "Monkey")
index = animals.index("Lion")

print(index)



##11.
a = (1, 2, 3, 4)
b = (5, 6, 7, 8)

Merging = (a+b)
print(Merging)


##12
t = (1, 2, 3, 4, "David")
l = ["Airbus", "Centrum", "UzAirways", 23, 25]

print(len(t))
print(len(l))


##!3.
a = (1, 2, 3, 4, 5)
print(list(a))


##14.
numbers = input("enter numbers:").split()
t = tuple(numbers)
print(t)
print(max(t))
print(min(t))


##15. 
l = input("Enter your word").split()
t = tuple(l)

print(t)
print(t[::-1])
