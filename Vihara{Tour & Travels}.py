print("Welcome to Vihara Tour and Travels - A trip to your dream places...")
for i in range(0,1):
    print(" ")
print("Let's move to Booking Session")
for i in range(0,1):
    print(" ")
#Trip selection
print("Please select the type of your trip:")
content=[]
expense=[]
a1=" 1-Religious Trip-Rs.20000"
a2="2-Peaceful Place Trip-Rs.18000"
a3="3-Holiday Trip-Rs.25000"
a4="4-Adventurous Trip-Rs.22000"
print(a1,"\n",a2,"\n",a3,"\n",a4)
for i in range(0,1):
    print(" ")
a=input("Please select the type of Trip:")
if a=="":
    print("you missed to fill a column...")
    a=input("Please select the type of Trip:")
if a=="1":
    content.append("Religious Trip")
elif a=="2":
    content.append("Peaceful Place Trip")
elif a=="3":
    content.append("Holiday Trip")
elif a=="4":
      content.append("Adventurous Trip")
else:
    print("Please enter a valid choice")
    a=input("Please select the type of Trip:")
for i in range(0,1):
    print(" ")
print("Please select the desired place:")
if a=="1":
    a5=" 1A- Kedarnath"
    a6="1B-Ayodhya"
    a7="1C-Jagannath Puri"
    a8="1D-Vaishno Devi"
    print(a5,"\n",a6,"\n",a7,"\n",a8)
    expense.append(20000)
elif a=="2":
    a9=" 2A-Bodh Gaya"
    a10="2B-Cheerapunji"
    a11="2C-Himachal Pradesh"
    a12="2D-Madhya Pradesh"
    print(a9,"\n",a10,"\n",a11,"\n",a12)
    expense.append(18000)
elif a=="3":
    a13=" 3A-Kerala"
    a14="3B-Goa"
    a15="3C-Karnataka"
    a16="3D-Agra"
    print(a13,"\n",a14,"\n",a15,"\n",a16)
    expense.append(25000)
elif a=="4":
    a17=" 4A-Shimla"
    a18="4B-Manali"
    a19="4C-Masoorie"
    a20="4D-Nainital"
    print(a17,"\n",a18,"\n",a19,"\n",a20)
    expense.append(22000)
else:
    print("Invalid Choice")
for i in range(0,1):
    print(" ")
b=input("Please enter your desired Place:")
if b=="":
    print("you missed to fill a column...")
    b=input("Please enter your desired Place:")
if b=="1A" or b=="1a":
    content.append("Kedarnath")
elif b=="1B" or b=="1b":
    content.append("Ayodhya")
elif b=="1C" or b=="1c":
    content.append("Jagannath Puri")
elif b=="1D" or b=="1d":
      content.append("Vaishno Devi")
elif b=="2A" or b=="2a":
    content.append("Bodh Gaya")
elif b=="2B" or b=="2b":
    content.append("Cheerapunji")
elif b=="2C" or b=="2c":
    content.append("Himachal Pradesh")
elif b=="2D" or b=="2d":
      content.append("Madhya Pradesh")
elif b=="3A" or b=="3a":
    content.append("Kerala")
elif b=="3B" or b=="3b":
    content.append("Goa")
elif b=="3C" or b=="3c":
    content.append("Karnataka")
elif b=="3D" or b=="3d":
      content.append("Agra")
elif b=="4A" or b=="4a":
    content.append("Shimla")
elif b=="4B" or b=="4b":
    content.append("Manali")
elif b=="4C" or b=="4c":
    content.append("Masoorie")
elif b=="4D" or b=="4d":
      content.append("Nainital")
else:
    print("Please enter a valid choice")
    b=input("Please enter your desired Place:")
#Hotel Booking
for i in range(0,1):
    print(" ")
print("Lets move to Hotel Booking session")
for i in range(0,1):
    print(" ")
print("Please select the desired hotel")
print("We provide the such kind of hotel facilities:\n 1-7*star Hotel-Rs.8000\n 2-5*star Hotel-Rs.6000\n 3-3*star Hotel-Rs.5000\n 4-budget friendly Hotel-Rs.2000")
for i in range(0,1):
    print(" ")
c=input("Please enter the hotel choice:")
if c=="":
    print("you missed to fill a column...")
    c=input("Please enter the hotel choice:")
if c=="1":
     content.append("7*star Hotel")
elif c=="2":
    content.append("5*star Hotel")
elif c=="3":
    content.append("3*star Hotel")
elif c=="4":
    content.append("Budget friendly Hotel")
else:
    print("Please enter a valid choice")
    c=input("Please enter the hotel choice:")
for i in range(0,1):
    print(" ")
if c=="1":
    w1=" 1A-Hotel wavewalker"
    w2="1B-Hotel Mapleleaf"
    w3="1C-Hotel Mountmourancy"
    print(w1,"\n",w2,"\n",w3)
    expense.append(8000)
elif c=="2":
    x1=" 2A-Hotel Rajvanshi"
    x2="2B-Hotel Rajdoot"
    x3="2C-Hotel Blue Spoon"
    print(x1,"\n",x2,"\n",x3)
    expense.append(6000)
elif c=="3":
    y1=" 3A-Hotel Raj Darbar"
    y2="3B-Hotel Redison Green"
    y3="3C-Hotel South city Inn"
    print(y1,"\n",y2,"\n",y3)
    expense.append(5000)
elif c=="4":
    z1=" 4A-Hotel Prabhat"
    z2="4B-Hotel Himalya"
    z3="4C-Hotel Jingle Town"
    print(z1,"\n",z2,"\n",z3)
    expense.append(2000)
else:
    print("Invalid choice,Try Again!!")
for i in range(0,1):
    print(" ")
d=input("Please enter your desired hotel:")
if d=="":
    print("you missed to fill a column...")
    d=input("Please enter your desired hotel:")
if d=="1A" or d=="1a":
     content.append("Hotel wavewalker")
elif d=="1B" or d=="1b":
    content.append("Hotel Mapleleaf")
elif d=="1C" or d=="1c":
    content.append("Hotel Mountmourancy")
elif d=="2A" or d=="2a":
    content.append("Hotel Rajvanshi")
elif d=="2B" or d=="2b":
    content.append("Hotel Rajdoot")
elif d=="2C" or d=="2c":
    content.append("Hotel Blue Spoon")
elif d=="3A" or d=="3a":
    content.append("Hotel Raj Darbar")
elif d=="3B" or d=="3b":
    content.append("Hotel Redison Green")
elif d=="3C" or d=="3c":
    content.append("Hotel South city Inn")
elif d=="4A" or d=="4a":
    content.append("Hotel Prabhat")
elif d=="4B" or d=="4b":
    content.append("Hotel Himalya")
elif d=="4C" or d=="4c":
    content.append("Hotel Jingle Town")
else:
    print("Please enter a valid choice")
    d=input("Please enter your desired hotel:")
print("your selected details-->")
for i in content:
    print(i)
for i in range(0,1):
    print(" ")
e=input("please type Yes to Confirm the above mentioned details:")
import sys
if e =="Yes"or e=="YES" or e=="yes":
    print("We are good to go...")
else:
    print("Please try booking again...")
    sys.exit()
for i in range(0,1):
    print(" ")
print("Please select the room type")
r1=" R1-AC room--Rs.1200"
r2="R2-Non-AC room-Rs.1000"
r3="R3-Deluxe-Rs.1400"
r4="R4-Super Deluxe-Rs.1500"
print(r1,"\n",r2,"\n",r3,"\n",r4)
for i in range(0,1):
    print(" ")
v=input("Enter the room type:")
if v=="":
    print("you missed to fill a column...")
    v=input("Enter the room type:")
if v=="R1" or v=="r1":
     content.append("AC room")
elif v=="R2" or v=="r2":
    content.append("Non-AC room")
elif v=="R3" or v=="r3":
    content.append("Deluxe")
elif v=="R4" or v=="r4":
    content.append("Super Deluxe")
else:
    print("Please enter a valid choice")
    v=input("Enter the room type:")
print("Select your Bed preference")
if v=="R1" or v=="r1":
    t1=" 1-Single Bed"
    t2="2-Double Bed"
    print(t1,"\n",t2)
    expense.append(1200)
elif v=="R2" or v=="r2":
    t1=" 1-Single Bed"
    t2="2-Double Bed"
    print(t1,"\n",t2)
    expense.append(1000)
elif v=="R3" or v=="r3":
    t1=" 1-Single Bed"
    t2="2-Double Bed"
    print(t1,"\n",t2)
    expense.append(1400)
elif v=="R4" or v=="r4":
    t1=" 1-Single Bed"
    t2="2-Double Bed"
    print(t1,"\n",t2)
    expense.append(1500)
for i in range(0,1):
    print(" ")
h=input("Enter the Bed preference:")
if h=="":
    print("you missed to fill a column...")
    h=input("Enter the Bed preference:")
if h=="1":
    content.append("Single Bed")
elif h=="2":
    content.append("Double bed")
else:
    print("Please enter a valid choice")
    h=input("Enter the Bed preference:")
for i in range(0,1):
    print(" ")

#Fooding
print("The Hotel provides such food services:")
f1=" 1-Italian-Rs.900"
f2="2-Mexican-Rs.800"
f3="3-Thai-Rs.700"
f4="4-Chinese-Rs.500"
print(f1,"\n",f2,"\n",f3,"\n",f4)
for i in range(0,1):
    print(" ")
f=input("Enter the Food service preference:")
if f=="":
    print("you missed to fill a column...")
    f=input("Enter the Food service preference:")
if f=="1":
     content.append("Italian")
elif f=="2":
    content.append("Mexican")
elif f=="3":
    content.append("Thai")
elif f=="4":
    content.append("Chinese")
else:
    print("Please enter a valid choice")
    f=input("Enter the Food service preference:")
if f=="1":
    expense.append(900)
if f=="2":
    expense.append(800)
if f=="3":
    expense.append(700)
if f=="4":
    expense.append(500)

#Other miscelenous services
for i in range(0,2):
    print(" ")
print("The Hotel provides such miscelenous services:")
m1=" 1-Fitness GYM"
m2="2-Swimming Pool"
m3="3-Gaming Zone"
print(m1,"\n",m2,"\n",m3,"\n","**Enter the service code for the services you want to go for**\n *Type No if you don't want any more services*")
for i in range(0,1):
    print(" ")
for i in range(3):
    j=input("Enter the desired service:")
    if j=="1":
        content.append("Fitness GYM")
    elif j=="2":
        content.append("Swimming Pool")
    elif j=="3":
        content.append("Gaming Zone")
    else:
        content.append("Not interested")
for i in range(0,1):
    print(" ")
print("the current details you filled->")
for i in content:
    print(i)
e=input("Please type Yes to Confirm the above mentioned details:")
if e =="Yes"or e=="YES" or e=="yes":
    print("We are good to go further...")
else:
    print("Please try booking again...")
    sys.exit()
for i in range(0,1):
    print(" ")
aa=input("Please enter your Pickup & Drop Address:")
if aa=="":
    print("you missed to fill a column...")
    aa=input("Please enter your Pickup & Drop Address:")
content.append(aa)
print("We provide such modes of pickup & Drop,pricing included in Trip charge:")
p1=" 1-Bus"
p2="2-Luxurious Car"
p3="3-Van"
print(p1,"\n",p2,"\n",p3)
for i in range(0,1):
    print(" ")
p=input("Please select your pickup & Drop mode to the Hotel:")
if p=="":
    print("you missed to fill a column...")
    p=input("Please select your pickup & Drop mode to the Hotel:")
if p=="1":
    content.append("Bus")
elif p=="2":
    content.append("Luxurious Car")
elif p=="3":
    content.append("Van")
else:
    print("Please enter a valid choice")
    p=input("Please select your pickup & Drop mode to the Hotel:")

import mysql.connector as Q
mycon=Q.connect(host='localhost',user='root',passwd='welcome',database='vihara')
cursor=mycon.cursor()
cursor.execute('show tables')
t=cursor.fetchall()
if t==[]:
    cursor.execute('create table user_details(SL_no int,Name varchar(40),Aadhar_no varchar(12),Mob_no varchar(10), Residential_Address varchar(100))')

#users deatils input
for i in range(0,1):
    print(" ")
o=int(input("Enter the total no.of candidates:"))
if p=="":
    print("you missed to fill a column...")
    o=int(input("Enter the total no.of candidates:"))
for i in range(0,1):
    print(" ")

for i in range (o):
    s=int(input("Enter the serial no.-"))
    if s=="":
        print("you missed to fill a column...")
        s=int(input("Enter the serial no.-"))
    n=input("Enter the candidate name:")
    if n=="":
        print("you missed to fill a column...")
        n=input("Enter the candidate name:")
    a=int(input("Enter the Aadhar no.-"))
    if a=="":
        print("you missed to fill a column...")
        a=int(input("Enter the Aadhar no.-"))
    m=input("Enter the Mobile no.-")
    if m=="":
        print("you missed to fill a column...")
        m=input("Enter the Mobile no.-")
    aa=input("Enter the Residential Address:")
    if aa=="":
        print("you missed to fill a column...")
        aa=input("Enter the Residential Address:")
    query="insert into user_details values({},'{}',{},{},'{}')".format(s,n,a,m,aa)
    cursor.execute(query)
    mycon.commit()

#Expenses Calculation
for i in range(0,1):
    print(" ")
print("Please wait while we are calculating your total expenses:")
for i in range(0,5):
    print(".")
expenses=0
for i in range(len(expense)):
    expenses+=expense[i]
print("As per Your preferable choices...We have calculated your Total expenses as Rs.",expenses*o,"only")
for i in range(0,1):
    print(" ")
print("Let's move to the Bank's payment page to make your wish come true....")
for i in range(0,1):
    print(" ")
py=input("Type yes after making the complete payment for proceeding further--Thank You...")
if e=="Yes"or e=="YES" or e=="yes":
    print("we are good to go ahead....")
else:
    print("Payment not done....Please Try booking again....")
    sys.exit()

#Check-In
for i in range(0,1):
    print(" ")
print("Let's check-in without any physical contact")
for i in range(0,1):
    print(" ")
import datetime
try:
    date_entry = input('Enter Check-In date in DD-MM-YYYY format:')
    day, month, year = map(int, date_entry.split('-'))
    date1 = datetime.date(year, month, day)
    content.append(date1)
except ValueError:
    date1="Please enter valid Date"
    print(date1)
try:
    time_entry = input('Enter Check-In time in HH:MM:SS format:')
    hour, minute, sec = map(int, time_entry.split(':'))
    time1 = datetime.time(hour, minute, sec)
    content.append(time1)
except ValueError:
    time1="Please enter valid time"
    print(time1)
for i in range(0,1):
    print(" ")
print("Please submit a photocopy of your Aadhar Card at the Reception Counter for our Perusal")
for i in range(1):
    print(" ")

#Room Allotment
import random
s2=random.randrange(400,500)
print("The Room alloted to you is:","A-",s2)
for i in range(1):
    print(" ")
print("Please be Comfortable in your room\nWe will be proceeding for Tour at 11am sharp and will be returning back to Hotel at 6pm sharp\nThank You")

#Events
for i in range(0,1):
    print(" ")
print("The Hotel organises these events in the Hotel Arena")
e1=" 1-Fountain Show"
e2="2-Belly Dance"
e3="3-Orchestra show"
e4="4-Classical music show"
print(e1,"\n",e2,"\n",e3,"\n",e4,"\n","**Enter the Event code for the event you want to go for**\n *Type No if you don't want any more Event*")
for i in range(1):
    print(" ")
for i in range(4):
    j1=input("Enter the desired service:")
    if j1=="1":
        content.append("Fountain Show")
    elif j1=="2":
        content.append("Belly Dance")
    elif j1=="3":
        content.append("Orchestra show")
    elif j1=="4":
        content.append("Classical music show")
    else:
        content.append("Not Interested")
for i in range(0,1):
    print(" ")
print("When it comes to our customer's comfort we try to give the most comfortable things...\nFor the most comfortable Tour we provide such kind of Tour buses:")
b1=" 1-2x2 Bus"
b2="2-2x3 Bus"
b3="3-2x1 Bus"
print(b1,"\n",b2,"\n",b3)
for i in range(1):
    print(" ")
f1=input("Enter the Bus type preference:")
if f1=="":
    print("you missed to fill a column...")
    f1=input("Enter the Bus type preference:")
if f1=="1":
    content.append("2x2 Bus")
elif f1=="2":
    content.append("2x3 Bus")
elif f1=="3":
    content.append("2x1 Bus")
else:
    print("Please enter a valid choice")
    f1=input("Enter the Bus type preference:")
s3=random.randrange(1,50)
for i in range(0,1):
    print(" ")
print("The Bus seat alloted to you is","B-",s3)
for i in range(0,1):
    print(" ")

#Check Out
print("Let's check-Out without any physical contact")
for i in range(0,1):
    print(" ")
try:
    date_entry = input('Enter Check-Out date in DD-MM-YYYY format:')
    day, month, year = map(int, date_entry.split('-'))
    date2 = datetime.date(year, month, day)
    content.append(date2)
except ValueError:
    date2="Please enter valid Date"
    print(date2)
try:
    time_entry = input('Enter Check-Out time in HH:MM:SS format:')
    hour, minute, sec = map(int, time_entry.split(':'))
    time2 = datetime.time(hour, minute, sec)
    content.append(time2)
except ValueError:
    time2="Please enter valid time"
    print(time2)
for i in range(0,1):
    print(" ")
    
#Aadhar No. Entry
v=input("**Use underscore(_) b/w Aadhar No.s , if booking is done for more than 1 person**\n *Use underscore(_) after Aadhar No. , if booking is done for single person also*\nPlease Enter the Aadhar No. for further references of the company:")
content.append(v)
for i in range(0,1):
    print(" ")
print("Please be ready with your Bag and Baggages after 10 mins. of Check Out to reach your drop location on time\nThank You for choosing Vihara Tour and Travels\nWe hope you enjoyed your Trip well....")

#Customer Review
for i in range(0,1):
    print(" ")
print("Please rate Vihara's Services...")
r1=" 5-Outstanding"
r2="4-Excellent"
r3="3-Very Good"
r4="2-Good"
r5="1-Satisfactory"
print(r1,"\n",r2,"\n",r3,"\n",r4,"\n",r5)
for i in range(1):
    print(" ")
r=input("Enter your review:")
if r=="":
    print("Please don't leave us without rating us....")
    r=input("Please enter your review:")
if r=="5":
    content.append("Outstanding")
elif r=="4":
    content.append("Excellent")
elif r=="3":
    content.append("Very Good")
elif r=="2":
    content.append("Good")
elif r=="1":
    content.append("Satisfactory")
else:
    print("Sorry...Our rating scale is between 1 to 5 only...")
    r=input("Please enter your review:")
print("Thanks for your relevant Feedback")

#Database Storage
import csv
k=open("Trip_details.csv",'a+')
l=csv.writer(k)
j=open("Trip_details.csv",'r')
v=csv.reader(j)
h=[]
for i in v:
    h.append(i)
if h==[]:
    l.writerow(["Trip type","Trip place","Hotel type","Hotel Name","Room type","Bed type","fooding","Service_1","Service_2","Service_3","Pickup & Drop Address","Pickup & Drop mode","Check-in date(DD-MM-YYYY)","Check-in time(HH:MM:SS)","Event 1","Event 2","Event 3","Event 4","Bus Type","Check-Out date(DD-MM-YYYY)","Check-Out time(HH:MM:SS)","Aadhar No.","Review"])
l.writerow(content)
j.close()
k.close()
