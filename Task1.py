# Simple Interest Calculation 1
principal=float(input("Enter the principal amount: ")) 
rate=float(input("Enter the rate of interest (in %): ")) 
time=float(input("Enter the time (in years): ")) 
simple_interest=(principal*rate*time) / 100
print("Simple Interest is:", simple_interest) 

a=int(input("Enter first number: "))
b=int(input("Enter second number: ")) 
if a > b:
    print("Maximum number is:",a)
else:
    print("Maximum number is:",b)
    
for i in range(1,6):
    print(i)


# Using a variable
my_string="Hello, World!"
print(len(my_string))

name="Neel"
print("Welcome.", name)

text = "Neel"
print(text[0])

text = "Neel"
print(text[-1])

num = 10

if num > 0:
    print("This is a positive number")
elif num < 0:
    print("This is a Negative number")
else:
    print("The number is Zero")

numbers=[10, 20, 30]
print(sum(numbers))

variable = input("prompt message:")