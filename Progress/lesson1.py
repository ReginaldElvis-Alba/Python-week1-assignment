#assigning values to the site_name
site_name= "Regianld Elvis"
print(site_name)

#assigning a new value
site_name='melanie'
print(site_name)

#assigning multiple values
a,b,c = 4.8, 100000,'success'
print(a)
print(b)
print(c)

#python is case sensitive
num=12
Num= 54
print(num)
print(Num)

#numeric data types
num1=1
print(num1, 'is of type',type(num1))

num2=787.877
print(num1, 'is of type',type(num2))

num3=3+5j
print(num1, 'is of type',type(num3))

#lists
languages=['english','kiswahili','french','spanish']
print(languages)

#accessing contents in a list
print(languages[2]) 

#tuples- lists that cannot be modified
activities=('football','rughby',233443)
print(activities)

print(activities[2])

#set- is unordered collection of unique items in curly brackets
student_id={112,123,3221,8383}
print(student_id)
print(type(student_id))

#dictionaries- set of ordered lists containing key value pairs
capital_cities={'Kenya:Nairobi','Uganda:Kampala','Tanzania:Dodoma'}
print(capital_cities)

#arithmetic operations
a=9
b=4
#addition
print('sum:',a + b)

#floor division
print('floor division:',a // b) #when you want to avoid decimals in your final output

#modulo- returns the remainder aftre division
print('Modulo'[a % b])

#PYTHON ASSIGNMENT OPERATORS
a = 13
b = 62

#Addition assignment
a+=10
print(a)

#multiplication
a=13
a*=128
print(a)

#exponenent assignment
a=13
a**=12
print(a)

#logical oprators AND,OR and NOT
a=38787
b=1
print((a>1) and (b>2))
#OR
a=38787
b=1
print((a>1) or (b>2))

#membership operators
x='Hello World'
y={1:a, 2:b}
print('Hello' in x)
print(1 in y)
print('a' in y)

#personalized greeting 
name= input("What is your name?")
vehicle=input("What is your favourite German machine?")

print(f"Hello {name}!Your favourite German Machin{vehicle} ")
