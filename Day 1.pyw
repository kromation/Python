a = 100
a = 125
print(a)
#All variables hold reference. Every reference is object in Python. Reference Values are according to the functions. Value of reference cannot be changed. Value of object can be changed if mutable

my_list = [i for i in range(1,10)]
# This is known as alist comprehension

#for loop written as 'for x in y'
#above code is searching i with the placeholder itself as i written in the beginning
##ranges = range(aa,z)
#throws error as it only accepts integer values

# SET: unordered collection of Data Types: Iterable, mutable and no duplication
#DICTIONARY: Ordered collection of Data Values: Stores data values like map

set_eg = set(my_list)
##set_eg.__and__(,200,/) 
#Whats right way to write this code need to check.
#__and__ is a magic operator that acts as bitwise AND. it is used to join two different sets by writing common values in them

my_set2 = ['this', 'too', 'shall', 'pass']

## set_eg2 = set_eg.__and__(my_set2)
#shows not implemented. MAKE IT WORK

set_eg2 = my_list.__and__(my_set2)
#this too did not work because my_list is a list and my_set is a set
print(set_eg2)