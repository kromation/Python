import xlwings as xw
#We are importing a library in python

#Lets create a new excel book
new_book = xw.Book()

#how about creating a new worksheet?
inputs = new_book.sheets.add('inputs')

#why am I getting index zero? -> sheets method returns a list and the first element is put inputs sheet
worksheet = new_book.sheets[0]

#shows total sheets in my workspace
print(new_book.sheets)

#whenever I want to do something to my worksheet I simply call the variable I named 
#I want to write down something in my excel sheet range is used to locate the cell
worksheet.range('A1').value = "Hello, how are you?"

#lets do some formatting to our excel worksheet
worksheet.range('A1').color = (0,100,0)
worksheet.range('A1').column_width = 50

# worksheet.range('A1').clear_contents()
#instead of above code 'clear contents' you can also do clear
#clears both the contents and the formating
worksheet.range('A1').clear()
#so far we were messing with excel from python 
#can we use python to read the contents in excel?

#Next lines of codes are being performed assuming someone has prefed data in the excel which is saved on your system already
############################
#open the workbook
wb = xw.Book('C:\Users\khull\Downloads\Python Demo.xlsx')
name = wb.range('c3').value
print(name)
