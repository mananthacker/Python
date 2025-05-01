
#1.A list contains names of boys and girls as its elements. Boys’ names are stored as tuples. Write a program to find out number of boys and girls in the list. (Hint: use isinstance(ele,tuple))
names =[("john"),"jane","julie",("james","jack"),"jill"]
boys=0
girls=0
for i in names:
    if isinstance(i,tuple):
        boys+=len(i)
    else:
        girls+=1
print("Number of boys in the list is",boys)
print("Number of girls in the list is",girls)

#2.A list contains tuples containing roll no., name and age of student. Write a python program to create three lists separately for roll no., name and age
students=[(1,2,3,4,5),("john","jane","julie","james","jack"),(20,21,22,23,24)]
roll_no=[]
name=[]
age=[]
for i in range(len(students[0])):
    roll_no.append(students[0][i])
    name.append(students[1][i])
    age.append(students[2][i])
print("Roll numbers of students are",roll_no)
print("Names of students are",name)
print("Ages of students are",age)

#3.Suppose a date is represented as a tuple (d, m, y). Create two date tuples and find the number of days between the two dates
date1=(1,1,2020)
date2=(30,1,2020)
days=0
days+=(date2[0]-date1[0])
days+=(date2[1]-date1[1])*30
days+=(date2[2]-date1[2])*365
print("Number of days between the two dates is",days)

#4.Create a list of tuples containing a food item and its price. Sort the tuples in descending order by price
food=[("apple",50),("banana",30),("orange",40),("grapes",60),("mango",70)]
food.sort(key=lambda x:x[1],reverse=True) 
print("List of food items in descending order of price is",food)

#5.Remove empty tuple(s) from the list of tuples.
tuples=[(),("john","jane"),(),("julie","james"),()]
for i in tuples:
    if i==():
        tuples.remove(i)        
print("List after removing empty tuples is",tuples)

#6.Modify an element of a tuple.
tuples=(1,2,3,4,5)
tuples=list(tuples)
tuples[2]=6
tuples=tuple(tuples)
print("Tuple after modifying an element is",tuples)

#7. delete an element of a tuple
tuples=(1,2,3,4,55,6)
print("tuple before removing :",tuples)
tuples=list(tuples)
tuples.remove(tuples[4])
tuples=tuple(tuples)
print("tuples after removing :",tuples)




