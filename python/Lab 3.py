#Count Vowels from string

string = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0
for i in string:
    if i in vowels:
        count += 1

#Accept two strings

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

if string1 in string2 or string2 in string1:
    print("One string is present in the other.")
else:
    print("No string is present in the other.")
print("Number of vowels in the string: ", count)
print("Number of vowels in the string: ", count)

 # Write program to covert all characters in a string to uppercase, lowercase and toggle case.without using inbuilt functions.
string = input("Enter a string: ")
upper = ""
lower = ""
toggle = ""
for i in string:
    if i.isupper():
        upper += i
        lower += i.lower()
    else:
        lower += i
        upper += i.upper()
    if i.isalpha():
        if i.islower():
            toggle += i.upper()
        else:
            toggle += i.lower()
    else:
        toggle += i
print("Uppercase: ", upper)
print("Lowercase: ", lower)
print("Toggle case: ",toggle)

#Write a function that removes one string from another string, if present using replace function

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
if string2 in string1:
    string1 = string1.replace(string2, '')
    print("The first string is removed from the second string: ", string1)
else:
    print("The first string is not present in the second string.")


