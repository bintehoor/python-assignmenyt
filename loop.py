# word assignment answers of question (24 to 43)
print("-------------------------%((24)FIRST 10 POSITIVE INTEGERS )%-------------------------------------")
n = int(input("Enter a Number : "))
f = 0
for i in range(n+1):
    print(i)
    f += i
print("Sum of the First",n," Positive Integers are :",f)

print("-------------------------%((25)SUM OF THE DIGITS IN AN INTEGERS )%-------------------------------------")
num = input("ENTER ANY INTEGERS NUMBERS :")
try:
    v = int(num)
except ValueError:
    print("that's not an int!")
    quit()
num = str(abs(int(num)))
s=0
for f in num:
    s += int(f)
print("Sum of the Digits are :",s)

print("-------------------------%((26)CONVERT INTEGER TO BINARY,OCTAL,HEXADECIMAL)%-------------------------------------")
number = input(" Enter any Integer Number : ")
try:
    k = int(number)
except ValueError:
    print("That's Not An Int! ")
    quit()
print("Binary : ",bin(k))
print("Octal : ",oct(k))
print("Hexadecimal : ",hex(k))

print("-------------------------%((27)CONVERT BINARY TO DECIMAL)%-------------------------------------")
b = input("Enter Binary Number : ")
d = 0
p = len(b) - 1
for i in b:
    d += int(i)*2**p
    p = p-1
print("Decimal number is :",d)

print("-------------------------%((28)CONVERT OCTAL TO DECIMAL)%-------------------------------------")
o = input("Enter Any Octal Number : ")
d = 0
p = len(o) - 1
for i in o:
    d += int(i)*8**p
    p = p-1
print("Decimal number is :",d)

print("-------------------------%((29)CONVERT HEXADESIMAL TO DECIMAL)%-------------------------------------")
hd = input("Enter Any Hexadecimal  Number : ")
d = 0
p = len(hd) - 1
for i in range(len(hd)):
    if hd[i] == 'A':
        d = d + 10 * 16 ** p
    elif  hd[i] == 'B':
        d = d + 11 * 16 ** p
    elif hd[i] == 'C':
        d = d + 12 * 16 ** p
    elif hd[i] == 'D':
        d = d + 13 * 16 ** p
    elif hd[i] == 'E':
        d = d + 14 * 16 ** p
    elif hd[i] == 'F':
        d = d + 15 * 16 ** p
    else:
        d = d+int(hd[i])*16**p

    p = p-1
print("Decimal number is :",d)

print("-------------------------%((30)NUMBER OF ACCURRENCE OF CHARACTER IN STRING)%-------------------------------------")
st = input("Enter a String :")
ch = input('Enter a Chracter : ')
cnt = 0
for chch in st:
    if chch == ch:
        cnt += 1
print("NUMBER ACCURRENCE IS : ",cnt)

print("-------------------------%((31)GREATEST COMMON DEVISER(GCD))%-------------------------------------")
n1 = int(input("Enter first Integer Number : "))
n2 = int(input("Enter second Integer Number : "))
while True:
    if n1 == 0 or n2 == 0:
        print("GCD Is :",abs(n1 - n2))
        break
    if n1 < n2:
        n1,n2 = n2,n1
    n1 = n1 % n2

print("-------------------------%((32)LEAST COMMON MULTIPAL(LCM))%-------------------------------------")
num1 = int(input("Enter first Integer Number : "))
num2 = int(input("Enter second Integer Number : "))
x = num1
y = num2
while(y):
    x , y = y, x % y
    lcm = ((num1 * num2)/ x)
print("LCM Is : ",lcm)
print("-------------------------%((33)NAME IN REVERSE ORDER)%-------------------------------------")
name = input("Enter 1st and last Name : ")
f , l = name.split()
print(l, f)

print("-------------------------%((34)THE OCCURRENCE OF VOWELS & CONSONANT)%-------------------------------------")
t = input(" INPUT TEXT : ")
v=0
c=0
for k in t:
    if k.upper() in 'AEIOU':
        v += 1
    if k.upper() in 'BCDFGHJKLMNPQRSTVWXYZ':
        c += 1
print("No.of Vowels : ",v)
print("No.of Consonant : ",c)

print("-------------------------%((35)NUMBER OF  NOTES CURRENCY)%-------------------------------------")
a = int(input("Enter Amount ; "))
note =[1000,500,100,50,20,10]
for i in note:
    print(i, ":",a // i)
    while a >= i:
        a -= i

print("-------------------------%((36)TO CHECK INPUT IS PALINDROME OR NOT)%-------------------------------------")
t = input("Enter Text : ")
l = len(t)
p = ""
for i in range (l): # for palindrom
    p += t[l-i-1]
if t.upper() == p.upper():
    print("YES! This is Palindrom.")
else:
    print("NO! This is Not a palindrome. ")

print("-------------------------%((37)REVERSE THE DIGIT OF A GIVEN NUMBER)%-------------------------------------")
d = int(input("Enter Digit : "))
while True:
    i = str(d)
    if i == i[::-1]:
        break
    else:
        m = int(i[::-1])
        d += m
print(d)

print("-------------------------%((38)FIBONICCI SERIES(0 T0 50)%-------------------------------------")
x = 0
y = 1
while x <= 50:
    print(x)
    x,y = y,x + y

print("-------------------------%((39)MULTIPLICATION TABLE(FRON 1 TO 10)%-------------------------------------")
number = int(input("Enter Number From 1 to 10 : "))
for t in range(10):
    s = number*(t+1)
    print(number,"x",t+1,"=",s)

print("-------------------------%((40)NUMBER OF DIGITS AND LETTERS IN SIMPLE DATA)%-------------------------------------")
s = input("Input string or Text : ")
m = 0
n = 0
for i in s:
    if i.upper() in "0123456789":
        m += 1
    if i.upper() in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        n += 1
print("No.of Letters : ",n)
print("No.of Digits : ",m)

print("-------------------------%((41)PATTERN : 1)%-------------------------------------")

a =int(input("Enter Number of Rows: "))
for i in range(1,a+1):
    print(' '*(a-i))
    for j in range(1,i+1):
        print("*",end=" ")
    print()
for i in range((a-1),0,-1):
    print(' '*(a-i))
    for j in range(1,i+1):
        print("*",end=" ")
    print()

print("-------------------------%((42)PATTERN : 2)%-------------------------------------")

a =int(input("Enter Number of Rows: "))
for i in range(1,a+1):
    print(' '*(a-i))
    for j in range(1,i+1):
        print(j,end=" ")
    print()
for i in range((a-1),0,-1):
    print(' '*(a-i))
    for j in range(1,i+1):
        print(j,end=" ")
    print()

print("-------------------------%((43)PATTERN : 3)%-------------------------------------")
n =int(input("Enter Number of Rows: "))
for row in range(1,n+1):
    for col in range(1,row+1):
        print(row,end="")
    print()





