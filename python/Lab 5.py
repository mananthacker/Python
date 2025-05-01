#1. Create a list of 5 odd integers using random nos. Similarly create a list of 4 even integers using random nos. Replace the third element of odd integers with a list of 4 even integers. Flattern, sort and print the list. Provide appropriate message at each stage
odd=[1,9,11,15,17]
even=[2,4,6,8]
odd[2]=even
print("List after replacing 3rd element of odd list with even list new list is:",odd)
odd=[1,9,*even,15,17]
print("List after flattening the list is:",odd)
odd.sort()
print("List after sorting the list is:",odd)


#2.Generate 20 random integers and store them in a list. Accept a number from the user and print position of all occurrences of that number in the list
import random
list1=[]
for i in range(20):
    list1.append(random.randint(1,100))
print("List of 20 random integers is:",list1)
# we can also have rendom numbers in list using :- list1=[random.randint(1,100) for i in range(20)]
num=int(input("Enter a number to search in the list:"))
for i in range(len(list1)):
    if list1[i]==num:
        print("Number found at position:",i+1)
else:
            print("Number not found in the list")  



#3.Generate 50 random numbers in the range 1 and 30. Remove all duplicate values from the list.   
import random
list1=[]
for i in range(50):
    list1.append(random.randint(1,30))
print("List of 50 random numbers is:",list1)
list1.sort()
print("List after sorting is:",list1)
for i in list1:
    if i==list1[i+1]:
        list1.remove(list1[i])
        if i==list1[i+1]:
           print("List after removing duplicate values is:",list1)
print("Length of the list after removing duplicates is:",len(list1))


#4. Generate 30 random numbers and put them in a list. Create two more lists – one containing only +ve numbers and another with –ve nos
import random
list1=[]
for i in range(30):
    list1.append(random.randint(-30,30))
print("List of 30 random numbers is:",list1)
positive=[]
negative=[]
for i in list1:
    if i>0:
        positive.append(i)
    elif i<0:
        negative.append(i)
print("List of positive numbers is:",positive)
print("List of negative numbers is:",negative)
print("Length of positive list is:",len(positive))
print("Length of negative list is:",len(negative))
print("Length of original list is:",len(list1))
 

#5. A list contains 5 strings. Convert all these strings to uppercase.
list1=['hello','world','python','java','c++']
print("List before converting to uppercase is:",list1)
for i in range(len(list1)):
    list1[i]=list1[i].upper()
print("List after converting to uppercase is:",list1)
print("Length of the list is:",len(list1))
print("Length of each string in the list is:")
for i in list1:
    print(len(i))
print("List after sorting is:",sorted(list1))
print("List after reversing is:",list1[::-1])
print("List after removing last element is:",list1[:-1])
print("List after removing first element is:",list1[1:])
print("List after removing first and last element is:",list1[1:-1])
print("List after removing 2nd element is:",list1[:1]+list1[2:])
print("List after removing 3rd element is:",list1[:2]+list1[3:])
print("List after removing 4th element is:",list1[:3]+list1[4:])
print("List after removing 5th element is:",list1[:4])
print("List after removing 1st and 2nd element is:",list1[2:])
print("List after removing 4th and 5th element is:",list1[:3])
print("List after removing 3rd and 4th element is:",list1[:2]+list1[4:])
print("List after removing 2nd and 3rd element is:",list1[:1]+list1[3:])
print("List after removing 1st and 2nd element is:",list1[2:])
print("List after removing 4th and 5th element is:",list1[:3])
print("List after removing 3rd and 4th element is:",list1[:2]+list1[4:])
print("List after removing 2nd and 3rd element is:",list1[:1]+list1[3:])
print("List after removing 1st and 2nd element is:",list1[2:])


#6.Convert list of temperatures in Fahrenheit degrees to equivalent Celsius degrees.
fahrenheit=[32,45,78,98,102]
print("List of temperatures in Fahrenheit is:",fahrenheit)
celsius=[]
for i in fahrenheit:
    celsius.append((i-32)*(5/9))
print("List of temperatures in Celsius is:",celsius)

#7. Write a menu-driven program to implement the stack data structure.
stack=[]
while True:
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        item=int(input("Enter the item to be pushed:"))
        stack.append(item)
    elif choice==2:
        if len(stack)==0:
            print("Stack is empty")
        else:
            print("Popped item is:",stack.pop())
    elif choice==3:
        if len(stack)==0:
            print("Stack is empty")
        else:
            print("Stack is:",stack)
    elif choice==4:
        break
    else:
        print("Invalid choice")

#9. Take two lists of numbers. Create third list of numbers for only those numbers from first list which are not there in 2nd list (use list comprehension).
list1=[1,2,3,4,5,6,7,8,9,10]
list2=[2,4,6,8,10]
list3=[i for i in list1 if i not in list2]  
print("List1 is:",list1)
print("List2 is:",list2)
print("List3 is:",list3)  #output is: [1, 3, 5, 7, 9]
print("Length of list3 is:",len(list3))  #output is: 5
print("Length of list1 is:",len(list1))  #output is: 10
print("Length of list2 is:",len(list2))  #output is: 5

#8. Write a menu-driven program to implement the Queue data structure.
queue=[]
while True:
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        item=int(input("Enter the item to be enqueued:"))
        queue.append(item)
    elif choice==2:
        if len(queue)==0:
            print("Queue is empty")
        else:
            print("Dequeued item is:",queue.pop(0))
    elif choice==3:
        if len(queue)==0:
            print("Queue is empty")
        else:
            print("Queue is:",queue)
    elif choice==4:
        break
    else:
        print("Invalid choice")