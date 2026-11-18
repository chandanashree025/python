'''s='Good Morning good Afternoon'                 \\slicing of string
print(s[-17:-21-1:-2])
print(s[-13:-21-1:-2])
print(s[-1:-4-1:-1])
print(s[5:12])

s=input("enter a name:")                         \\data type of the input
print(type(s))

\\ CONDITIONAL STATEMENTS

s=int(input("enter the number:"))                 \\ odd or even
if s%2==0:
    print("even")
else:
    print("odd")

s=eval(input("enter the tuple:"))                  \\checking whether the input is a tuple or not 
if(type(s)==tuple):
    print("tuple")
else:
    print("not a tuple")

print(ord('z'))                                    \\ascii value of a character
print(ord('a'))
print(ord('D'))
print(ord('N'))

ch=input('enter ch:')                              \\checking whether the input is a uppercase letter or not
if'A'<=ch<='Z':
    print(True)
else:
    print(False)

num=int(input("enter a number:"))                   \\checking whether the input is a two-digit number or not
if 10<=num<=99:
    print("two-digit number")
else:
    print("is not a two-digit number")

num1=int(input('enter a number1:'))                  \\checking which number is greater
num2=int(input('enter a number2:'))
if num1==num2:
    print("both numbers are equal")
elif num1>num2:
    print("num1 is greater than num2")
elif num1<num2:
    print("num2 is greater than num1")
else:
    print("both numbers are not equal")
ch=input('enter ch:')                           \\checking whether the input is a upper case ,lower case, digit or special character
if'A'<=ch<='Z':
    print("upper case letter")
elif'a'<=ch<='z':
    print("lower case letter")
elif'0'<=int(ch)<='9':
    print("digit")
else:
    print("special character")

ch=input('enter ch:')       \\checking whether the input is a upper case ,lower case, digit or special character
if ch.isupper():                               
    print("upper case letter")
elif ch.islower():
    print("lower case letter")
elif ch.isdigit():
    print("digit")    
else:
    print("special character")

ch=input('ehter ch:')          \\checking whether the input is a vowel or consonant
if ch.isalpha():
    if ch in ['a','e','i','o','u','A','E','I','O','U']:
        print("vowel")
    else:
        print("consonant")
else:
    print("not an alphabet")

l=eval(input("enter a number:"))    \\checking whether the input is a list or not
if(type(l)==list):
    if len(l)%2==0:
        print("even")
    else:
        print("odd")
else:
    print("not a list")

\\loops

i=1                          \\while loop
while i<=10:
    print(i)
    i+=1

i=1                          \\printing 5 times Hello
while i<=5:
    print("Hello")
    i+=1

s=[1,3,4]
i=0
while i<len(s):
    print(s)
    i+=1

l=eval(input("enter the list:"))     
i=0
while i<len(l):
    print(l[i])
    i+=1

n=int(input("enter:"))   
rev=0
while n>0:
    ld=n%10
    n=n//10
    rev=rev*10+ld
print(rev)    

for i in range(1,11):    \\for loop
    print(i)

i='Hello'
for i in range(1,6):
    print("Hello")

s=input('enter')                 \\converting from upper case to lower case letter
out=''
for i in s:
    if 'A'<=i<='Z':
        out=out+chr(ord(i)+32)
    else:
        out+=i
print(out)       

s=input('enter')  
out=''              
for i in s:
    if 'a'<=i<='z':
        out=out+chr(ord(i)-32)
    elif'A'<=i<='Z':
        out=out+chr(ord(i)+32)
    else:
        out+=i
print(out)

s=[12,10,'hello','Good',5j,'Bye']
out={}
for i in s:
    if type(i)==str:
        out[i]=i[0]+i[-1]
print(out)

for i in range(1,6):
    for j in range(1,6):
        print('*',end=' ')
    print()

def convert(s):     \\with argument ,with return
    out=''              
    for i in s:
        if 'a'<=i<='z':
            out=out+chr(ord(i)-32)
        elif'A'<=i<='Z':
            out=out+chr(ord(i)+32)
        else:
            out+=i
    return(out)
print(convert(s=input('enter:')))

def convert():                             \\with arguments, without return
    s=input('enter:')  
    out=''                       
    for i in s:
        if 'a'<=i<='z':
            out=out+chr(ord(i)-32)
        elif'A'<=i<='Z':
            out=out+chr(ord(i)+32)
        else:
            out+=i
    print(out)
convert()

def convert():                     \\without argument,with return
    s=input('enter:')   
    out=''              
    for i in s:
        if 'a'<=i<='z':
            out=out+chr(ord(i)-32)
        elif'A'<=i<='Z':
            out=out+chr(ord(i)+32)
        else:
            out+=i
    return(out)
print(convert())

def convert():                      \\without argument,without return
    s=input('enter:')   
    out=''              
    for i in s:
        if 'a'<=i<='z':
            out=out+chr(ord(i)-32)
        elif'A'<=i<='Z':
            out=out+chr(ord(i)+32)
        else:
            out+=i
    print(out)
convert()'''


