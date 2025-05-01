#hours to min
hours = float(input("Enter hours: "))
print(f"{hours} hours is {hours * 60} minutes.")

#min to hours
min = float(input("Enter min: "))
print(f"{min} min is {min/60} hourse.") 

#dollar to rupees
dollar = float(input("enter dollar: "))
print(f"{dollar} $ is {dollar/48} rupees.")

#rupees to dollar
rupees = float(input("enter rupees: "))
print(f"{rupees} rupees is {rupees*48} dollar.")

#dollar to pound through rupees
dollar = float(input("enter dollar: "))
print(f"{dollar} $ is {dollar*48/70} pounds .") #short code

#dollar to rupees through rupees
dollar = float(input("enter dollar: "))
rupees = dollar*48
print(f"{dollar} $ is {rupees/70} pound.")

#gram to kg
gram = float(input("enter gram: "))
print(f"{gram} g is {gram/1000} kg.")

#kg to gram
kg = float(input("enter kg: "))
print(f"{kg} kg is {kg*1000} g.")

#bytes to kb,mg,gb
bytes = float(input("enter bytes: "))
print(f"{bytes} bytes is {bytes*0.0009765625} kb.\n")
print(f"{bytes} bytes is {bytes*0.00000095367431640625} mb.\n")
print(f"{bytes} bytes is {bytes*0.00000000095367431640625} gb.")

#celcius to fahrenheit
celcius = float(input("enter celcius:"))
print(f"{celcius} celcius is {(9/5*celcius)+32} Fahrenheit")


#fahrenheit to celcius
F= float(input("enter F:"))
print(f"{F} fahrenheit is {5/9*(F-32)}")

#calculation of interest
P = float(input("Enter the principal amount: "))
R = float(input("Enter the rate of interest: "))
N = float(input("Enter the time in years: "))
I = (P * R * N) / 100
print("The simple interest is:", I)

#area of square
L = float(input("enter the lenght of one side: "))
A = L*L
print("Area of square is: ",A)

#perimeter of square
L = float(input("enter the lenght of one side: "))
P = 4*L
print("Perimeter of square is: ",P)

#area of rectangular
L = float(input("enter the lenght of one side: "))
B = float(input("enter the breadth of one side: "))
A = L*B
print("Area of square is: ",A)

#perimeter of rectangular
L = float(input("enter the lenght of one side: "))
B = float(input("enter the breadth of one side: "))
P = 2*(L+B)
print("Area of square is: ",P)

#area of circle
R = float(input("enter the radius of circle: "))
A = 22/7 * R * R
print("the area of circle is: ",A)

#area of triangle
L = float(input("enter the lenght: "))
H = float(input("enter the height: "))
A = L*H/2
print("Area of square is: ",A)

#net salary
gross_salary = float(input("Enter the gross salary: "))
allowances = gross_salary * 10/100
deductions = gross_salary * 3/100
net_salary = gross_salary + allowances - deductions
print("Gross Salary:", gross_salary)
print("Allowances (10%):", allowances)
print("Deductions (3%):", deductions)
print("Net Salary:", net_salary)

#net sales
gross_sales = float(input("Enter the gross sales: "))
discount = gross_sales * 0.10
net_sales = gross_sales - discount
print("Gross Sales:", gross_sales)
print("Discount (10%):", discount)
print("Net Sales:", net_sales)

#average and total of three subjects
maths = float(input("enter maths marks: "))
physics = float(input("enter physics marks: "))
chemistry = float(input("enter chemistry marks: "))
A = (maths+physics+chemistry)/3
T = maths+physics+chemistry
print("the average of three subjects is: ",A )
print("the total of three subject is: ",T)

#swaping of two values
num1 = float(input("enter A : "))
num2 = float(input("enter B : "))
print("A is: ", num1)
print("B is: ", num2)
T = num1
num1 = num2
num2 = T
print("after swaping A is : ",num1)
print("after swaping B is : ",num2)
