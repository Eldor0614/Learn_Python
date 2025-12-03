##1.
d3= {1:1, 3:9, 4:16, 5:25}

my_dictDesc = sorted(d3.items(), reverse = True)
my_dictAsc = sorted(d3.items(), reverse = False)
print(my_dictDesc)
print(my_dictAsc)


##2. 

numbers = {2:4, 3:9, 4:16}

numbers[5] = 25

print(numbers)



#3. 
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}



d4 = dic1 | dic2 | dic3
print(d4)



##4.
d = {x: x*x for x in range(1,10)}

print(d)


##5.
d = {x: x*x for x in range(1, 16)}
print(d)



##6
set1 = {1, 1, 2, 3, 4, 4}
print(set1)



##7.
set1 = {1, 1, 2, 3, 4, 4}

for s1 in set1:
    print(s1)


##8
set1 = {1, 1, 2, 3, 4, 4}

addings = 7, 9

set1.add(addings)
print(set1)



##9.
set1 = {1, 1, 2, 3, 4, 4}

set1.difference_update({2, 3})
print(set1)

set1.discard(1)
print(set1)


##10.
set1 = {1, 1, 2, 3, 4, 4}
set1.discard(int(input("Enter ypur number")))


print(set1)
