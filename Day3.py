List = [1,3,4]
print(List.append(23))
#data inside print is executed at the runtime
#its return type is none
# popped_element = List.pop()[1]  
# ##wrong way of writing the code .pop(0) is valid
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