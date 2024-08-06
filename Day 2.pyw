#All variables hold reference. Every reference is object in Python. Reference Values are according to the functions. Value of reference cannot be changed. Value of object can be changed if mutable

a = [1,2,3]
print(id(a))
b = [3,1,2]
print(id(a))

#https://stackoverflow.com/questions/41960288/why-mutable-objects-having-same-value-have-different-id-in-python
# The id value is different in each id(a) in a code written 7 years ago as it was created usin v2 and I am trying it on v3

#################################################

#Every variable in Python holds and instance of an object.Whenever an object is instantiated, its assigned a unique object id . The type of the object id is defined at the runtime and it can't be changed afterward. However, its state can be changed if it is a mutable object.
# Hash value of the Imutable objects remain constant
# In multi-threaded environment, immutable objects are inherently thread-safe 
#Immutable objects are of built in datatypes (int, float, bool, string, Unicode and tuple). 
# # #
# an immutable object cant be changed after it is created.

tuple1 = (0,1,2,3)
##tuple[0] =4
print(tuple1)
# TypeError: 'type' object does not support item assignment for line tuple[0] = 4

message = "Welcome to Coding Experience"
##message[0] = 'py'
print(message)
# TypeError: 'str' object does not support item assignment

# # #

#Mutable Objects are Python list, Python dict, or Python set.

#Example 1 - add or remove LISTS 
my_list = [1,2,3]
my_list.append(4)
my_list.append(50)
#adds the value mentioned 
print(my_list)

my_list.insert(1,5)
#inserts the value in second attribute at place BEFORE first attribute of function insert()
my_list.insert(-1,7)
#inserts the value in second attribute at place AFTER first attribute of function insert() Starts counting from last element
my_list.insert(10,7)
#inserts the value in second attribute at place AFTER first attribute of function insert() Even though mentioned 10th index it will add the value at the immediate next location of the index
print(my_list)

my_list.remove(2)
## my_list.remove(20)
# ValueError: list.remove(x): x not in list
##my_list.remove(10)
# ValueError: list.remove(x): x not in list
#element at 8th and 9th 10th location will throw error if tried to remove as it does not exist.
print(my_list)

popped_element = my_list.pop(0)
##popped_element = my_list.pop(10)
#IndexError: pop index out of range
print(my_list)
print(popped_element)

# Example2 modify item in DICTIONARY

my_dict = {"name": "Ram", "age":25}
print(id(my_dict))
print(my_dict)
new_dict = my_dict
#same id for new_dict and my_dict. This means that the reference is copied using assignment operator
new_dict["age"] = 37

print(id(my_dict))
print(my_dict)
print(id(new_dict))
print(new_dict)

#Example3 Modify item from a set in python

my_set = {1,2,3}
new_set = my_set 
#same id for both new_set and my_set thus it concludes that reference is copied again
new_set.add(4)

print(my_set)
print(id(my_set))
print(new_set)
print(id(new_set))

#MUTABLE OBJECTS ARE THOSE WHOSE REFERENCE IS COPIED (CALL BY REFERENCE) RATHER THAN ACTUAL VALUE BEING ASSIGNED TO A NEW VARIABLE AT NEW MEMORY LOCATION

#Immutable objects are quicker to access and expensive to change because it involves the creation of a copy. Whereas mutable objects are easy to change
#the use of mutable objects is recommended when there is a need to change the size or content of the object.
#Exception: However there is and exception in immutability as well. We know that tuple in Python is immutable. But the tuple consists of a sequence of names with unchangeable bindings to objects.

tup = ([3,4,5], 'myname')
print(tup)
print(tup[1])

#tuple consists of string and a list. Strings are immutable so we cant change their value. But the contents of the list can change. "The tuple itself isn't mutable but contains items that are Mutable"

#As a rule of thumb, generally, Primitive-like types are probably immutablem and Customised Container-like types are mostly mutable

a=10
b=10
print(id(a), id(b))

##########################

thisdict = {
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}
print(thisdict)
print(len(thisdict))
#dict length starts from 0

#as of python 3.7 dictionaries are ordered
#We say dictionaries are ordered, it means that the items have a defined order, and that the order will not change.

#Dictionaries are changeable, meaning that we can change, add or remove the items after the dictionary has been created



thisdict = {
    "brand":"Ford",
    "model":"Mustang",
    "model":"Mitsubishi",
    "year":1964,
    "year":2020
}
#Duplicates are not allowed in dictionaries and the first one will  be considered but the second duplicate or vice versa (in an online code comiler). Duplicate entry will neither be registered nor error would be thrown.

print(type(thisdict))
#the type of dictionary is dict

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)
#above is an example for the constructor dict()