#Print all alphabets in upper case and in lower case.
for i in range(65,91):
    print(chr(i),end=" ")   
print()
for i in range(97,123):
    print(chr(i),end=" ")   
print()


#Print a multiplication table of a given number.
num = int(input("Enter a number: "))
for i in range(1,11):
    print(num,"x",i,"=",num*i)
print()


#Count no. of alphabets and no. of digits in any given string
str = input("Enter a string: ")
alpha = 0
digit = 0
for i in str:
    if i.isalpha():
        alpha += 1
    elif i.isdigit():
        digit += 1
print("No. of alphabets:",alpha)
print("No. of digits:",digit)
print()

#Check whether a given number is prime, is perfect, is Armstrong, is palindrome, is automorphic.
num = int(input("Enter a number: "))
#Prime
flag = 0
for i in range(2,num):
    if num%i == 0:
        flag = 1
        break
if flag == 0:
    print(num,"is a prime number.")
else:
    print(num,"is not a prime number.")

#Perfect
sum = 0
for i in range(1,num):
    if num%i == 0:
        sum += i
if sum == num:
    print(num,"is a perfect number.")
else:
    print(num,"is not a perfect number.")

#Armstrong
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
if num == sum:
    print(num,"is an Armstrong number.")
else:
    print(num,"is not an Armstrong number.")

#Palindrome
temp = num
rev = 0
while temp > 0:
    digit = temp % 10
    rev = rev*10 + digit
    temp //= 10
if num == rev:
    print(num,"is a palindrome number.")
else:
    print(num,"is not a palindrome number.")

#Automorphic
sq = num ** 2
temp = num
flag = 0
while temp > 0:
    if temp % 10 != sq % 10:
        flag = 1
        break
    temp //= 10
    sq //= 10
if flag == 0:
    print(num,"is an automorphic number.")
else:
    print(num,"is not an automorphic number.")
print()


#Generate all Pythagorean Triplets with side length <= 30
for a in range(1,31):
    for b in range(a,31):
        for c in range(b,31):
            if a**2 + b**2 == c**2:
                print(a,b,c)
print()

#Print 24 hours of day with suitable suffixes like AM, PM, Noon and Midnight.
for i in range(1,13):
    print(i,"AM")   
print("Noon")
for i in range(1,13):
    print(i,"PM")
print("Midnight")
print()


# Print nCr and nPr.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

n = int(input("Enter value of n: "))
r = int(input("Enter value of r: "))

nCr = factorial(n) // (factorial(r) * factorial(n - r))
nPr = factorial(n) // factorial(n - r)

print(f"{n}C{r} = {nCr}")
print(f"{n}P{r} = {nPr}")
print()

#Print factorial of a given number.

num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"The factorial of {num} is {factorial}")
print()

#Print N natural nos. in reverse.
n = int(input("Enter a number: "))
for i in range(n,0,-1):
    print(i,end=" ")
print()

#Print Fibonacci series upto n terms.
n = int(input("Enter a number: "))
a = 0
b = 1
print(a,b,end=" ")
for i in range(2,n):
    c = a + b
    print(c,end=" ")
    a = b
    b = c
print()

#11) Calculate sin(x); x is a radian value. The formula is as under:
# sin(x) = x - x^3/3! + x^5/5! - x^7/7! + x^9/9! - x^11/11! + ...

def fact(n):
    f = 1
    for i in range(n,1,-1):
        f *= i
    return f
x = float(input("Enter x: "))
sin_x=0
step = 0
while True:
    sin_x = sin_x + (-1)(step%2)* x**(2*step+1)/fact(2*step+1)
    if(step == 20):
        break
    step+=1

print("sin(",x,") = ",sin_x)
     





  