#Data structures-allow you to organize and arrange your data to perform operations in them-
# Types-Built in data structures and User designed data structures
#Built in data structures- dictionaries,tuples,lists,set
#User designed data structures-linked lists,tree,stack,queue,graph,Hashmaps
#Mutabilities-data inside a data structure and can be modified and immutabilities data- data structure will not allow modifications ie tuple
 
#ceation of lists
numbers=[1,3,78]
print(numbers[2])

#slicing of lists
my_list=['p','d','k','e','j','n','g']
print(my_list)

#use index 0
my_list=['p','d','k','e','j','n','g']
print(my_list[-1])

#use slicing from index 2 to index 4
my_list=['p','d','k','e','j','n','g']
print(my_list[2:4])

#use slicing from index beginning to index 4
my_list=['p','d','k','e','j','n','g']
print(my_list[:4])

#use slicing from index beginning to end
my_list=['p','d','k','e','j','n','g']
print(my_list[:])

#adding elements to a list
#1.Using the append() method
#before appending
numbers=[12, 22, 82, 736]
print("Before append:",numbers)
#after appending
numbers=[12, 22, 82, 736]
numbers.append(366677)
print("After append:",numbers)

#using the extend()- to add all items of onel list to the other
prime_numbers=[2, 3, 5]
print("List1:",prime_numbers)

even_numbers=[4, 6, 8]
print("List1:",even_numbers)

prime_numbers.extend(even_numbers)
print("list after extend:", prime_numbers)

#change a list of items
languages=['python', 'java', 'C++']
languages[2]='dart'
print(languages)

#deleting items
languages=['python', 'java', 'C++']
del languages[2]
print(languages)

#deleting items
languages=['python', 'java', 'C++']
languages.remove('java')
print(languages)

#iterating through a list
languages=['python', 'java', 'C++']
for languages in languages:
    print(languages)

#python list comprehension
numbers=[number*number for number in range(1,6)]
print(numbers)

#dictionaries
numbers={1:'one',2:'two', 3:'three'}
print(numbers)

#membership for keys in dictionaries
squares={1:1, 2:4, 3:9, 4:16}
print(squares)

#membership test
squares={1:1, 2:4, 3:9, 4:16}
print(1 in squares)
print(2 in squares)
print(5 in squares)

#create a set of data
student_id={123, 135, 5757, 8484}
print('Student id are ', student_id)

#creating an empty set
empty_set=set()
empty_dic={}
print('the empty set is made up of', empty_set)
print('the empty dictionaries are made up of', empty_dic)
print('the empty set is made up of', type(empty_set))
print('the empty dictionaries are made up of', type(empty_dic))

#removing a value from a set
languages={'java', 'html','python'}
print('Programming languages initially:',languages)

languages={'java', 'html','python'}
print('Programming languages initially:',languages)
removedValue=languages.discard('java')
print('Programming languages after:',languages)

#iterate over a set
fruits={'mango', 'orange', 'apple', 'bananas'}
for fruits in fruits:
    print(fruits)

#union sets
A={1, 2 , 3}
B={5, 9, 5}
print('The union of the two sets using |:', A|B)
print('The union of the two sets using union():', A.union(B))

#intersection
A={1, 2 , 3,9}
B={5, 3, 9, 5}
print('The intersection of the two sets using |:', A&B)
print('The intersection of the two sets using union():', A.intersection(B))

#difference
A={1, 2 , 3,9}
B={5, 3, 9, 7}
print('The difference of the two sets using |:', A-B)
print('The difference of the two sets using union():', A.difference(B))

#check if two sets are equal
#difference
A={1, 2 , 3,9}
B={5, 3, 9, 7}
if A == B:
    print('Set A and B are equal')
else:
    print('Set A and B are not equal ')

#escaping sequences in python
example="He said, \"what's the problem\""
print(example)

#python f string formatting
name='Reginald'
location='United states'
print(f'my name is {name} and i live in the {location} with my extended family')

#Write a program that accepts user input to create a list of integers. Then, compute the sum of all the integers in the list.
integers=input('Create a list of integers:')
print('The list includes:',integers)

#Create a tuple containing the names of five of your favorite books. Then, use a for loop to print each book name on a separate line.
favourite_books=['thermo', 'dynamics', 'vibrations','fluids', 'design']
for favourite_books in favourite_books:
    print(favourite_books)


personal_details=input({'name', 'age', 'favourite_colour'})
print(personal_details)

#using dictionaries to come up with the user inputs
person_info={}
name=input('What is your name?')
age=int(input('What is your age?'))
favourite_colour=input('What is your favourite_colour?')

person_info['Name']=name
person_info['Age']=age
person_info['Favourite_colour']=favourite_colour
print('\nstored information:')
print(person_info)