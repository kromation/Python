List = [1,3,4]
print(List.append(23))
#data inside print is executed at the runtime
#its return type is none
# popped_element = List.pop()[1]  
# ##wrong way of writing the code in py V3 nut was semantically correct in py V2 .pop(0) is valid
# print(popped_element)

# TypeError: 'int' object is not subscriptable
# this error tells that you are mixing up the types. eg concatenating string with integer
# this is only allowed while using tkinter
# print(list.pop()[0])

str = "Sudden jerk"
##print(str += '!')
#gives syntax error as its immutable during runtime

str += '!'
print(str)
# this is permissible

#####################################

#another way of extracting data from the lists
lists = [['apple',['orange']], ['lemon'],['kiwi']] 
listss = [['apple','orange'], ['lemon','kiwi']] 
print(lists.pop([0][0])) #apple #orange 
#next I am trying to remove only orange
## print(listss.pop([ ][0])) #apple 
# ATTEMPT 1 lists index out of range
##print(listss.pop([0[0]])) #apple 
# ATTEMPT2 TypeError: 'int' object is not subscriptable
##print(listss.pop([0]:[0])) #apple 
# this sign : is used to split and splice list

print(listss[0].pop(1)) #orange 

print(lists)
print(listss)

## print(listss.pop(0)[0]) #lemon
# semantically incorrect

