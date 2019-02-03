import class1

def factorial():
    factorial = 1
    i = 1
    n = int(input("Enter a number "))
    for i in range(1, n + 1):
        factorial = factorial * i
        print("Factorial ", i, " = ", factorial)
        i = i + 1

def timetable():
    a = int(input("begining = "))
    b = int(input("ending = "))
    for i in range(a, b + 1):
        for j in range(a, b + 1):
            print(i * j, end="\t")
        print("\n")

def information():
    person1 = Human()
    person1.name = input("Enter a name: ")
    person1.age = input("Enter a age: ")
    person1.hight = input("Enter a hight: ")
    print("Hello, I'm ", person1.name, "I'm", person1.age, "years old and", person1.hight, "in hight")

#############################

print("Begin")
print("for factorial press 'f'")
print("for times table press 't'")
print("for times table press 'inf'")
choice = " "
choice =(input())
if choice == "f":
    factorial()
if choice == "t":
    timetable()
if choice == "inf":
    information()
print("End!")