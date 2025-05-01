#1. Write a program to create three dictionaries and concatenate them to create fourth dictionary.
dict1={1:"john",2:"jane",3:"julie"}
dict2={4:"james",5:"jack",6:"jacob"}
dict3={7:"jill",8:"jennifer",9:"jessica"}
dict4={}
dict4.update(dict1)
dict4.update(dict2)
dict4.update(dict3)
print("Fourth dictionary after concatenating the three dictionaries is",dict4)
#2.	Write a program to check whether a dictionary is empty or not.
dict1={}
if not dict1:
    print("Dictionary is empty")
else:
    print("Dictionary is not empty")

#3.Create a dictionary with dept no, employee roll no. and salary. Find out department wise min and maximum of salary.
dict1={1:(101,102,103),2:(201,202,203),3:(301,302,303)}
dict2={101:10000,102:20000,103:30000,201:15000,202:25000,203:35000,301:12000,302:22000,303:32000}
dept_sal={}
for i in dict1:
    dept_sal[i]=(min(dict2[j] for j in dict1[i]),max(dict2[j] for j in dict1[i]))
print("Department wise minimum and maximum salary is",dept_sal)

#4.Write a program that reads a string from the keyboard and creates dictionary containing frequency of each character occurring in the string
string=input("Enter a string:")
dict1={}
for i in string:
    dict1[i]=dict1.get(i,0)+1   
print("Dictionary containing frequency of each character occurring in the string is",dict1)

#5.Create two dictionaries – one containing grocery items and their prices and another containing grocery items and quantity purchased. By using the values from these two dictionaries compute the total bill.
grocery_price={"apple":50,"banana":30,"orange":40,"grapes":60,"mango":70}
grocery_quantity={"apple":2,"banana":3,"orange":4,"grapes":5,"mango":6}
total_bill=0        
for i in grocery_price:
    total_bill+=grocery_price[i]*grocery_quantity[i]
print("Total bill is",total_bill)
 