#1 Print numbers from 1 to 5
for i in range(1,6):
    print(i)

#2 Print a message 3 times
for i in range(3):
    print("Hello")

#3 Print numbers from 1 to 10
for i in range(1,11):
    print(i)

#4 Print even numbers from 1 to 20
for i in range(1,21):
    if i%2==0:
        print(i)

#5 Print odd numbers from 1 to 15
for i in range(1,16):
    if i%2!=0:
        print(i)

#6 Print table of 5
for i in range(1,11):
    print("5 x",i,"=",5*i)

#7 Print characters of a string
name="Atmiya"
for letter in name:
    print(letter)

#8 Sum of number from 1 to 5
total=0
for i in range(1,6):
    total=total + i
    print("Sum is:",total)

#9 Print list elements 
numbers=[10,20,30,40] 
for n in numbers:
    print(n) 