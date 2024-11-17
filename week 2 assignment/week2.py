#Create an empty list called my_list.
my_list=[]
print('The empty list is:',my_list)

#Append the following elements to my_list: 10, 20, 30, 40
my_list=[]
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print('My appended list is:', my_list)

#Insert the value 15 at the second position in the list
my_list=[10, 20, 30, 40]
my_list.insert(1, 15)
print('My inserted value at the second position:',my_list)

#Extend my_list with another list: [50, 60, 70].
my_list=[10, 20, 30, 40]
my_list.extend([50, 60, 70])
print('My extended list include:',my_list)

#Remove the last element from my_list.
my_list=[10, 20, 30, 40, 50, 60, 70]
my_list.pop()
print('My list after removal:',my_list)

#Sort my_list in ascending order
my_list=[10, 20, 30, 40, 50, 60, 70]
my_list.sort()
print('My list arranged in ascending order:',my_list)

#Find and print the index of the value 30 in my_list.
my_list=[10, 20, 30, 40, 50, 60]
index_of_30=my_list.index(30)
print(index_of_30)

