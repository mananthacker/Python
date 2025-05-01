
#Largest and smallest of two numbers

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
if num1 > num2:
    print("Largest number is:" , num1)
else:
        print("largest number is.", num2)

#Largest and smallest of three numbers       
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
if num1 >= num2 and num1 >= num3:
 largest = num1
elif num2 >= num1 and num2 >= num3:
 largest = num2
else:
 largest = num3

if num1 <= num2 and num1 <= num3:
 smallest = num1
elif num2 <= num1 and num2 <= num3:
 smallest = num2
else:
 smallest = num3

print("Largest number is:", largest)
print("Smallest number is:", smallest)

#Check if a number is odd or even

number = int(input("Enter a number to check if it is odd or even: "))
if number % 2 == 0:
            print(f"{number} is even.")
else:
            print(f"{number} is odd.")

#Check if a number is divisible by 10
number = int(input("Enter a number to check if it is divisible by 10: "))
if number % 10 == 0:
            print(f"{number} is divisible by 10.")
else:
            print(f"{number} is not divisible by 10.")
        
#Age check
age = int(input("Enter your age: "))
if age < 18:
    print("You are minor.")
else:
    print("You are major.")

#Accept number from user
num = int(input("Enter a number: "))
count = 0
while num > 0:
    num = num // 10
    count = count + 1
print("Number of digits in the given number are:", count)
 

#Check if year is leap year

year = int(input("Enter a year to check if it is a leap year: "))
if  (year % 4 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

#Check if triangle exists
angle1 = float(input("Enter the first angle of the triangle: "))
angle2 = float(input("Enter the second angle of the triangle: "))
angle3 = float(input("Enter the third angle of the triangle: "))

if angle1 + angle2 + angle3 == 180:
    print("The triangle is valid.")
else:
    print("The triangle is not valid.")
#Absolute value of a number

number = float(input("Enter a number to find its absolute value: "))
absolute_value = abs(number)
print(f"The absolute value of {number} is {absolute_value}.")



#Length & breadth of a rectangle

length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))

area = length * breadth
perimeter = 2 * (length + breadth)

if area > perimeter:
    print("The area of the rectangle is greater than its perimeter.")
else:
    print("The area of the rectangle is not greater than its perimeter.")

#Check all points lie on straight line

x1, y1 = map(float, input("Enter the coordinates of the first point (x1 y1): ").split())
x2, y2 = map(float, input("Enter the coordinates of the second point (x2 y2): ").split())
x3, y3 = map(float, input("Enter the coordinates of the third point (x3 y3): ").split())

area = 0.5 * abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2))

if area == 0:
    print("The points lie on a straight line.")
else:
    print("The points do not lie on a straight line.")



#Point inside, outside or on the circle

xc, yc = map(float, input("Enter the coordinates of the center of the circle (xc yc): ").split())
radius = float(input("Enter the radius of the circle: "))
xp, yp = map(float, input("Enter the coordinates of the point (xp yp): ").split())

distance = ((xp - xc)**2 + (yp - yc)**2)**0.5

if distance < radius:
    print("The point lies inside the circle.")
elif distance == radius:
    print("The point lies on the circle.")
else:
    print("The point lies outside the circle.")


#Convert number into words

number = int(input("Enter a number between 0 and 19: "))

words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", 
             "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", 
             "seventeen", "eighteen", "nineteen"]

if 0 <= number <= 19:
        print(f"The number {number} in words is: {words[number]}")
else:
        print("Number out of range. Please enter a number between 0 and 19.")

#Accept marks & display grade

marks = []
subjects = ["first", "second", "third"]

for subject in subjects:
    mark = input(f"Enter the marks for the {subject} subject (or 'Absent' if not present): ")
    if mark.lower() == 'absent':
        marks.append('NA')
    else:
        marks.append(int(mark))

grades = []
total = 0
fail = False

for mark in marks:
    if mark == 'NA':
        grades.append('NA')
        fail = True
    elif mark <= 39:
        grades.append('F')
        fail = True
    elif mark <= 44:
        grades.append('P')
        total += mark
    elif mark <= 49:
        grades.append('C')
        total += mark
    elif mark <= 54:
        grades.append('B')
        total += mark
    elif mark <= 59:
        grades.append('B+')
        total += mark
    elif mark <= 69:
        grades.append('A')
        total += mark
    elif mark <= 79:
        grades.append('A+')
        total += mark 
    elif mark <= 100:
        grades.append('O')
        total += mark

if not fail:
    average = total / 3
    print(f"Total marks: {total}")
    print(f"Average marks: {average:.2f}")
    print("Result: Pass")
else:
    print("Result: Fail")

for i, grade in enumerate(grades):
    print(f"Grade for {subjects[i]} subject: {grade}")