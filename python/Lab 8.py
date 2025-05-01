#1.Write a program that converts words present in a list into uppercase and stores them in a set.
words=["apple","banana","orange","grapes","mango"]
words=set(words)
words={i.upper() for i in words}
print("Set containing words in uppercase is",words)
#2.Write a program to create a set containing 10 random numbers in the range 15 to 45. Count how many of these numbers are less than 30. Delete all numbers that are greater than 35.
import random
s=set()     
for i in range(10):
    s.add(random.randint(15,45))    
print("Set containing 10 random numbers in the range 15 to 45 is",s)
count=0
for i in s:
    if i<30:
        count+=1
print("Number of elements less than 30 is",count)
s={i for i in s if i<=35}
print("Set after deleting numbers greater than 35 is",s)

#3.Create an empty set. Write a program that adds five new names to this set, modifies one existing name and deletes two names from it.
s=set()
s.update(["john","jane","julie","james","jack"])
print("Set after adding five new names is",s)
s.remove("john")
s.remove("jane")
print("Set after deleting two names is",s)
s.add("jacob")
print("Set after modifying one existing name is",s)
list1=list(s)
list1[1]="jennifer"
s=set(list1)
print(s)

#4.A set contains names which begin either with A or with B. Write a program to separate out the names into two sets, one containing names beginning with A and another with B.
s={"apple","banana","orange","grapes","mango","apricot","blueberry","blackberry"}
s1={i for i in s if i[0].lower()=="a"}
s2={i for i in s if i[0].lower()=="b"}
print("Set containing names starting with A is",s1)
print("Set containing names starting with B is",s2)
