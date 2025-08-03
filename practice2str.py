str = input("enter a string:")
if str.startswith ("hello"):
 print("yes its there")
else:
 print("no its not there")
 
 sen = input ("enter a sentence:")
s= sen.replace(" ","-")
print(s)

word = input("enetr a word:")
w= word[0]
x=word[-1]
print(w,x)

sen = input("enter a sentence:")
capital = sen.upper()
print(capital)