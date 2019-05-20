# ANSWERS OF QUESTIONS [2,3,5,7,10,11,23]
print("-------------------------%(POSITIVE/NEGITIVE/ZERO NUMBERS)%----------------------------")
num = int(input("ENTER NUMBER TO CHECK (positive/negitive) : "))
if num < 0:
    print(num,"is Negitive Number")
elif num > 0:
    print(num,"is Positive Number")
else:
    print("Zero '0'")

print("-------------------------%( DIVISIBLE NUMBERS)%----------------------------")
num_1 = int(input("ENTER ANY NUMBER : "))
num_2 = int(input("ENTER ANY NUMBER : "))
if num_1 % num_2 == 0:
    print("NUMBERS ARE COMPLETELY DIVISIBLE")
else:
    print("NUMBERS ARE NOT COMPLETELY DIVISIBLE")

print("-------------------------%( DIFRENCE B/T USER GIVEN NUMBER AND 17)%----------------------------")
x = int(input("ENTER GRATER NUMBER FROM 17 : "))
if x >= 17:
     c = x-17
     print("DIFFERENCE = ",c)
else:
    print("ENTER GRATER NUMBER  FROM '17'")

print("-------------------------%(EVEN/ODD NUMBERS)%----------------------------")
y = int(input("ENTER NUMBER WETHER TO CHECK EVEN/ODD : "))
if y%2 == 0:
    print(y,"is Even Number")
else:
    print(y,"is Odd Number")

print("-------------------------%(vowel letters)%----------------------------")
char = input('ENTER ANY LETTER OR ALPHABET : ')


if ((char =='a')|(char =='e')|(char =='i')|(char =='o')|(char =='u')|(char =='A')|(char =='E')|(char =='I')|(char =='O')|(char =='U')):
    print(char,"is Vowil Letter")
else:
    print(char,"Is Consonant")

print("-------------------------%(NUMBER OF DAYS BETWEEN TWO DATES)%----------------------------")
from datetime import date
first_date = date(2019 , 5 ,9)
second_date = date(2003 , 5 ,9)
d = first_date - second_date
print("NUMBER OF DAYS = ",d)

print("-------------------------%(TEMPRATURE CONVERSION)%----------------------------")
print("1 .  FOR CONVERT CELSIUS TO FEHRENHEIT")
print("2 .  FOR CONVERT FEHRENHEIT TO CELSIOUS")
ch=int(input("ENTER YOUR CHOICE : "))
if ch == 1:
    c=int(input("ENTER TEPRATURE IN CELSIOUS : "))
    f=(c*9/5)+32
    print("FEHRENHEIT Temp = ",f)
if ch == 2:
    x = int(input("ENTER TEPRATURE IN FEHRENHEIT : "))
    cel = (x-32)*5/9
    print("CELSIUS Temp = ",cel)

