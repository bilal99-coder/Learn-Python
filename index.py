failed_subjects= "2" 
name='John'
print('Dear Mrs Badger')
print('Your son ' + name + ' is failing ' + failed_subjects + ' subjects.')
print(name + '  will need to redo ' + failed_subjects + '  courses.')
name="Eric"
print(name + '  is doing well in geography.')

# This how you get the type of a variable

print(type(5))
print(type('hello'))
print(type(1))
print(type(1.64))
print(type(True))

print('Variables & Datatypes - Exercise')
#Create appropriate Variables for Item name, the price 
#and how many you have in stock

item_name = 'widget'
price = 23.5
inventory = 100
is_in_inventory = True
print(item_name, price, inventory)


a=6
b=2
print('Addition : ', a + b)
print('Subtraction : ', a - b)
print('Multiplication : ', a * b)
print('Division (float) : ', a / b)
print('Division (floor) : ', a // b)
print('Modulus : ', a % b)
print('Exponent : ', a ** b)


msg='welcome to it\'s Python 101: Strings'
print(msg)
print(msg.upper())
print(msg.lower())
print(msg.capitalize())
print(msg.title())


msg='welcome to Python 101: Strings'
print(msg)
print(len(msg))   #prints the length of the string 
print(msg.count('Python')) #counts the instances of the word python 


msg='welcome to Python 101: Strings'
    #012345678
print(msg)
#slicing : get an element inside the string by its index 
# if the index is negative, then python starts counting from the end of the # string 
# if you use the index n: (i.e. msg[2:], python will grab all the elements # after 2)
print(msg[0])



msg="""Dear Terry,,
You must cut down the mightiest 
tree in the forest with…
a herring! <3"""
print(msg)  #This will print the message on different lines, must use """ in the beginning and the end 

# the replace function 
msg='Welcome to Python 101: Strings'
print(msg.replace('Python','C'))
msg1=msg.replace('Python','C')  #Welcome to C 101: Strings
print(msg1)  #Welcome to C 101: Strings

# does a word exists on the string??
msg='Welcome to Python 101: Strings'
print('Python' in msg) #true 
print('Python' not in msg) #false 