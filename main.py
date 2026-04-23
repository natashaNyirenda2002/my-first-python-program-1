#part 1: hello world program

print("hello world ")

print("hello, my name is Kaluba")

print("I am learning python")

print("=" * 30)

#part 2: user input

name = input("Enter your name: ")

age = input("Enter your age: ")

print("Welcome" + name + ", you are", age, "years old. ")

print("=" * 30)

#part 3: simple calculator

num1 = float(input("Enter first number: "))

num2 = float(input("Enter second number: "))

Sum_result = num1 + num2

Difference = num1 - num2

Product = num1 * num2

print("Sum:", Sum_result)
print("Difference:", Difference)
print("Product:", Product)

print("=" * 30)

#part 4: Even or Odd

number = input("Enter a number: ")
number = int(number)

if number % 2 == 0:
    print(number, "is Even")
else:
    print(number, "is Odd")

print("=" * 30)

#part 5: Grade checker

marks = int(input("Enter your marks: "))

if 80 <= marks <= 100:
    print("Grade: A")
elif 70 <= marks <= 79:
    print("Grade: B")
elif 60 <= marks <= 69:
    print("Grade: C")
elif 50 <= marks <= 59:
    print("Grade: D")
elif 0 <= marks <= 50:
    print("Grade: F")
else:
    print("Invalid marks entered")
print("=" * 30)





