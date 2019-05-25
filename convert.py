# ANSWERS OF QUESTIONS (8,9,15,17,19,20,21,)
print("-----------------------%(ALL UNITS OF TIME INTO SECONDS)%---------------------------")
h = int(input("ENTER TIME IN HOURS : "))
m = int(input("ENTER TIME IN MINUTES : "))
time_h = h*60*60
time_m = m*60
time_second = (time_h + time_m)
print("TIME IN SECONDS : ",time_second)

print("-----------------------%(CONVERT  SECONDS TO DAY,HOURS,MINUTES AND SECONDS)%---------------------------")
s=float(input("ENTER TIME IN SECONDS: "))
print('SELECT CONVERSIONS;')
print("1: DAY\n2:Hours\n3: Minutes")
ch=int(input())
if  ch == 1:
    day=s/86400
    print("Time =",day,"day(s)")
if ch == 2:
    h=s/3600
    print("Time = ",h,"Hours")
if ch == 3:
     min=s/60
     print("Time =",min,"Minutes(m)")

print("------------------%(HEIGHT IN FEET AND INCHES TO CENTEMETERS(cm))%---------------------")
feet= int(input("ENTER HEIGHT IN FEET: "))
inches=int(input("ENTER HEIGHT IN INCHES: "))
cm = ((feet*12) + inches)* 2.54
print(feet,"ft", inches,"inches","=",cm,"cm")


print("------------------%(DISTANCE IN FEET TO INCHES,YARDS AND MILES)%---------------------")
# 1 FEET = 12 INCHES
# 1 FEET = 1/3 YARDS
# 1 FEET = 5280 MILES
distance = float(input("ENTER DISTANCE IN FEET(ft): "))
ft_inches = distance * 12
ft_yard = (1/3) * distance
ft_mile = (1/5280) * distance
print("Distance In Inches = ",ft_inches,".")
print("Distance In Yards = ",ft_yard,".")
print("Distance In Miles = ",ft_mile,".")


print("------------------%(string n (non negitive integers)copies of given string)%---------------------")
str=input("ENTER STRING VALUE: ")
n=int(input("ENTER NON NEGITIVE INTEGER NUMBER: "))
copies= (str)*n
print("No of Copies :",copies)

print("------------------%(GIVEN STRING WITH 'IS')%---------------------")
given_str= input("ENTER ANY STRING VALUE: ")
con = "is"
if(given_str[ :2] == con):
    print("Given string remains unchanged!")
else:
    n_str = con + " " + given_str
    print("New string Is = ",n_str,"!")


print("------------------%(COMPUTING INTREST RATE)%---------------------")
p_amount=float(input("ENTER PRINCIPAL AMOUNT(Rs): "))
r_year=float(input("ENTER RATE PER YEAR : "))
y=int(input("ENTER NO. OF YEARS: "))
I = p_amount*(1+r_year*y)
print("Total Amount(Rs) = ",I,)

