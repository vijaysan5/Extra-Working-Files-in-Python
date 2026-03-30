# Feb 01
'''print("One, Feb")
a=5
b=12
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)
print(a//b)
print(a%b)

a=8
b=5
c=8
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a<=b)
print(a>=b)

x=5
print(x)
x+=2
print(x)
x-=5
print(x)
x*=2
print(x)
x/=2
print(x)
x**=5
print(x)
x//=10
print(x)

# And, Or, Not
a=23
b=25
c=23
print(a==c and c==a)
print(a>b or b>c)
print(not a==c)
#Is, Is Not
x=15
y=13
z=15
print(x is y)
print(x is z)
print(x is not y)
print(x is not z)
#In, Not in
a="Book is the Best Friend"
print('B' in a)
print('A' not in a)
print('is' not in a)
# &,|,<<,>>
a=8
b=4
print(a&b)
print(a|b)
print(a>>2)
print(a<<3)
print(a^5)

a=input("Enter the value : ")
print(a)
print(type(a))

b=input("Enter tha velue : ")
b=int(b)
print(b,type(b))

c=int(input("Enter the value : "))
print(c,type(c))
'''
#Input
x=input("b=")
print(x)
print(type(x))
y=complex(x)
print(y)
print(type(y))
z=int(x)
print(z)
print(type(z))
w=float(x)
print(w)
print(type(w))

# Feb 04
'''print("04 Feb")
a=16
b=8
print(a&b)
print(a|b)
print(a>>2)
print(b<<2)
print(a^8)
a=input("Total Value:")
print(a)
print(type(a))
b=int(a)
print(b)
print(type(b))
c=float(a)
print(c)
print(type(c))
d=complex(a)
print(d)
print(type(d))
a=input("Enter Any Value:")
print(a)
b=int(a)
print(b)
print(b+10)
print(b-5)
print(b*2)
print(b/4)
print(b%8)
print(b**2)
print(b//6)
x=input("a=")
print(x)
y=float(x)
print(y)
print(y+9)
print(y-2)
print(y*5)
print(y/2)
print(y%4)
print(y**3)
print(y//8)
'''
x="Devadarshini"
print(x[4:9])
print(x[0:-3:2])
print(x[-2:-9])
Hint=" HAppY New YeAr tO AlL  "
print(Hint.upper())
print(Hint.lower())
print(Hint.title())
print(Hint.swapcase())
print(Hint.capitalize())
print(Hint.strip())
print(Hint.rstrip())
print(Hint.lstrip())
print(len(Hint))
print(Hint.count("e"))
print(Hint.index("p"))
print(Hint.find("A"))
print(Hint.isalpha())
print(Hint.isdigit())
print(Hint.islower())
print(Hint.isupper())

a="12937834"
print(a.isdigit())
print(a.find("3"))

a='PrintThaTopictoand'
print(a.replace("a","e"))

x="Hello"
y="My Friend"
z=x+y
print(z)
print(x+"-"+y)
print(z.split(","))
print(x+" "+y)


# Feb 05
'''print("Feb05")
x=int(input("any value:"))
print(x)
print(type(x))
print(x+9)
print(x-2)
print(x*5)
print(x/2)
print(x%4)
print(x**3)
print(x//8)
a="Automatically"
print(a[0:-1])
print(a[:-4])
print(a[:-3:2])
Day=" SuNdAY MoNdAy "
print(Day.upper())
print(Day.lower())
print(Day.title())
print(Day.swapcase())
print(Day.strip())
print(Day.rstrip())
print(Day.lstrip())
print(Day.isnumeric())
print(len(Day))
print(Day.count("AY"))
print(Day.find("A",6))
print(Day.index("N"))
print(Day.islower())
print(Day.isdigit())
Num=" 3562436"
print(Num.strip())
print(Num.find("3"))
print(Num.isdigit())
print(Num.isalpha())
print(Num.replace("43","5 45ye4"))
a="Windows"
b="Backup"
c="Documents"
print(a+b)
print(b+c)
print(a+" "+b)
print(b+" "+c)
print(a+'_'+b+'_'+c)
Sys="Window i5 Core"
print(Sys)
print(Sys.startswith("W"))
print(Sys.endswith("e"))
print(Sys.split(" "))
print(Sys.encode())
a=Sys.encode()
print(a)
print(a.decode())
b=['23', '46', '56', '98']
print(b)
print("_".join(b))
a="Sangavi Anandh"
print(a[8:],end=" ")
print(a[0:7])
print(a[:-7],a[-7:])
b=a
print(b)
c=a[:-7]+a[-7:]
print(c)
'''
a="sandhiya anandh"
print(a.upper())
print(a[0].upper()+a[1:-1].lower()+a[-1].upper())
b="sandhiya"
print(b[:3].lower()+b[3:4].upper()+b[-4:].lower())


# Feb 07
"""
a="sandhiya"
print(a[:3].lower(),end=(""))
print(a[-5:-4].upper(),end=(""))
print(a[-4:].lower())
print(a.title())
print(a.startswith("san"))
print(a.endswith("ya"))
print(a.encode())
b=a.encode()
print(b)
print(b.decode())
c="  anandh sangavi "
print(c)
print(c[-8:].title(),c[2:8].title())
a=18
b=input("age:")
print(b)
c=int(b)
print(c)
if(a==c):
    print("Age is equal")
if(a<c):
    print("a is eligible to vote")
if(a<c):
    print("a is eligible to vote")
else:
    print("a is not eligible to vote")

a=input("name:")
b=int(input("age:"))
c=input("place:")
d=18
h="Mayiladuthurai"
if(b>d and c==h):
    print("a is eligible to Vote")
if(b>d):
    print("is eligible")
else:
     print("is not eligible")
if(c==h):
    print("is accepted")
else:
    print("is not accepted")

x=input("Name:")
a=int(input("Tamil:"))
b=int(input("English:"))
c=int(input("Maths:"))
d=int(input("Hindi:"))
e=int(input("EVS:"))

if(a>35) and (b>35)and(c>35)and(d>45) and (e>25):
    print("Pass")
else:
    print("Fail")
x=input("")
"""

# Feb 09
"""print("Feb 09")
#if
a=20
b=25
if(a<b):
    print("a is less than b")
print("--------------------------------------")
#else
a=40
b=53
if(a>b):
    print("a is greater than b")
else:
    print("b is greater than a")
print("--------------------------------------")
#elif
a=73
if(a>90):
    print("above 90")
elif(a>80):
    print("above 80")
elif(a>70):
    print("above 70")
else:
    print("not valid this value")
print("--------------------------------------")
#nested if
a=str(input("Name:"))
b=int(input("Age:"))
if(b>21):
    print("Age is valid for this Exam")
    sem1=int(input("sem:"))
    sem2=int(input("sem:"))
    sem3=int(input("sem:"))
    sem4=int(input("sem:"))
    x=(sem1+sem2+sem3+sem4)
    print(x)
    Ave=x/4
    if(Ave>90.0):
        print("stu. Qualified to JRF")
    else:
        print("stu. not Qualified to jrf")
        if(Ave>81.5):
            print("stu. Qualified to Ass. Prof.")
        else:
            print("stu. Not Qualified to Ass. Prof.")
            if(Ave>70.0):
                print("stu. Qualified to Ph.d")
            else:
                print("stu. Not Qualified")
else:
    print("Age is Not valid for this Exam")

a=str(input("Name: "))
Tam=int(input("Tamil:"))
Eng=int(input("English:"))
Math=int(input("Maths:"))
Sci=int(input("Science:"))
Soc=int(input("Social:"))
b=int(Tam+Eng+Math+Sci+Soc)
print(b)
if(b>(450)):
    print("'O' Gread")
elif(b>(400)):
    print("'A' Gread") 
elif(b>350):
    print("'B' Gread")
if(b>300):
    print("'C' Gread")
elif(b>250):
    print("'D' Gread")
else:
    print("Stu. is fail")
a=str(input("Name:"))
b=int(input("Age:"))
c=str(input("Qualification:"))
d=str(input("Distric: "))
x=25
x1=40
y="Diploma"
y1="Any Degree"
z="Mayiladuthurai"
if(b>x) and(b<x1):
    print("Age is Valid")
    if(c==y) or (c==y1):
        print("Education is Valid")
        if(z==d):
            print("Dis. is Valid")
else:
    print("Age is Not Valid")"""
A=str(input("name: "))
B=float(input("Percentage:"))
C=70.5
D=50.8
if(B>C):
    print("Eligible for Paper 2 exam")
    if(B>D):
        print("Eligible for paper 1 Exam")
else:
    print("Not Eligible for this exam")

# Feb 12
a=0
while (a<5):
    print("a")
    a+=1   
for a in range(1, 5):
    print(a)
print("------------------------")
for b in range(1, 23, 2):
    print(b)
print("------------------------")
for x in range(0, 50, 5):
    print(x)


d="Location"
for x in range(len(d)):
    print(x)
a=["Locatin", "I am"]
b=["from Madurai", "from Chennai", "from Karaikal"]   
for y in a:
    for z in b:
        print(y,z)
print("------------------------------------------")
a=["Locatin", "I am", "Are you"]
b=["from Madurai", "from Chennai", "from Karaikal"]
for d in a:
    if d == "Are you":
        break
    print(d)
    for e  in b:
        if e == "from Chennai":
            continue
        print(e)
print("------------------------------------------")  
for x in range(15):
    if x == 3:
        continue
    print(x)
    print("============")
    if x == 5:
        break
    print(x)
    print("______________")


# Feb 13
    '''a=2
while (a>5):
    print(" ")
    a+=2
for x in range(0, 10):
    print(x)
for y in range(10, 50, 5):
    print(y)
a=["Happy", "New"]
b=["Day", "Year"]
for x in a:
    for y in b:
        print(x,y)
'''
txt=["vacation", "happy", "nice"]
xy=["today", "day" "week"]
for a in range(len(txt)):
    print(a)
for b in txt:
    if b=="happy":
        break
    print(b)
    for c in xy:
        if c=="day":
            continue
        print(c)
for x in range(8):
    if x==4 :
        break
    print(x)
    if x==2 :
        continue
    print(x)
    
# Feb 15
'''a=int(input("num:"))
b=0
while(a>0):
    c=a%10
    b=b*10+c
    a//=10
    print(c)
print(b)'''
'''
def name():
    print("Vijay")
name()

def myself(x):
    if (x%2==0):
        return "Even Num"
    else:
        return "Odd Num"
print(myself(20))
print(myself(25))

def value (b,a=5):
    print("b:",b)
    print("a:",a)
value(10)
print("------------------")'''
'''def anyvalue(s):
    if(s%2==0):
        return "Even num"
    else:
        return "Odd num"
print(anyvalue(int(input("s:"))))
print(anyvalue(int(input("s:"))))

def enter(b,a=5):
    print("a:",b)
    print("b:",a)
enter(input("b:"))
'''
def NameAge(Name, Age):
    print(Name, Age)
NameAge(Name=str(input("Name:")), Age=int(input("Age:")))

def Location(Name, Place):
    print("Hi Mam. My name is:", Name)
    print(" I'm from:", Place)
Location(Name=str(input("Name:")), Place=str(input("Place:")))
    
# Feb 17

def wish():
    print("Happy Birthday Sista")
wish()

def numfind(x):
    if x%2==0:
        return "Even Num"
    else:
        return "Odd Num"
print(numfind(int(input("x: "))))
print(numfind(int(input("x: "))))

def value (x,y=23):
    print("a:", x)
    print("b:", y)
value(int(input("x:")))

def NameAge(Name,Age):
    print(Name,Age)
NameAge(Name=str(input("Name:")),Age=int(input("Age:")))

def Location(Name,Place):
    print("Hi Mam. My Name is:",Name)
    print("I'm from:",Place)
Location(Name=str(input("Name:")),Place=str(input("Place:")))
"""
"""
def y(x):
    for a in range(x):
        if a%2==0:
            continue
        print(a)
y(23)

def value(x):
    z=0
    while x>0:
      y=x%10
      z=z*10+y
      x//=10
    print(z)
value(int(input("k:")))

def number(t):
    v=0
    while t>0:
        u=t%10
        v=v*10+u
        t//=10
    print(v)
number(int(input("enter:")))
        
# Feb 18
'''def abc(x):
    for a in range(x):
        if a%2==1:
            continue
        print(a)
abc(25)    
def any(a):
    x=0
    while a>0:
        b=a%10
        x=x*10+b
        a//=10
    print(x)
any(int(input("value:")))
'''        
'''
a={"b":1,"d":2,"c":3}
for i,j in a.items():
    print(f"{i} == {j}")
    print("{} == {}".format(i,j))
'''
'''b=("Hey","Welcome")
for i in b:
    print(i)
'''
'''
x,*y=23,34,24
print(x,y)

def san(ak, *bk, **ck):
    print("Txt:", ak)
    print("Txt*:", bk)
    print("Txt**:", ck)
san("Disk", "Hp", "Ssd", "samT", akk = 23 , skk = 25)

def vi(*NumI, **NumII):
    print("Hello:")
    for I in NumI:
        print(I)

    print("Hi World")
    for II,IJ in NumII.items():
        print(f"{II}=={IJ}")

vi("long", "live", "skip", "turn", cm=523, km="200m")

x={"a":32,"b":51,"c":89}
for a in x:
    print(a)
    
for c,d in x.items():
    print(c,d)
for sa,vs in x.items():
    print(f"{sa}=={vs}")'''

def v(sa,sv,sy):
    return (sa+sv+sy)
value=[23,35,51]
enter = v(*value)
print(enter)

def s(a,b,c):
    return (a,b,c)
v = (1,3,5)
ef = s(*v)
print(ef)

# Feb 19
def vj(NumI, *NumII, **NumIII):
    print("Txt1:",NumI)
    print("Txt2:",NumII)
    print("Txt3:",NumIII)
vj("ABC", "BCD", "CDE", "DEF", "EFG", Place="Budhapast", Name="Yash", Age=21)

def vi(Sanv,*San,**SanI):
    for san in Sanv:
        print(san,sep="_")
    
    for I in San:
        print(I)
   
    for A in SanI:
        print(A)
    
    for X,Y in SanI.items():
        print(f"{X}=*={Y}")
vi("lovely", "Happy", "Smile", "Nice", "Cute", Place="Budhapast", Name="Yash", Age=21)


x={21:"A", 23:"B", 25:"C", 29:"D"}
for a in x:
    print(a)

for c,d in x.items():
    print(f"{c}='_'={d}")

for e,f in x.items():
    print(e,f)
    
def vy(ab, cd, ef):
    return (ab+cd+ef)
value=[23,25,29]
ani=vy(*value)
print(ani)

"____________________
user=25
def san():
    pas=14
    print(user)
    print(pas)
san()

def sanv():
    c=21
    print(user)
    print(c)
sanv()
print(user)

def win():
    global user
    user=23
    print(user)
win()

def swe(s):
    if s == 0:
        return 1
    else:
        return s * swe(s- 1)
print(swe(9))

def recv(vs):
    if vs>0:
        return 1
    else:
        return vs+recv(vs-2)
print(recv(21))




# Feb 21
'''a=56
b=89
c=58
v=30
def use():
    if(a<v) and (b<v) and (c<v):
        print("HDFC")
    else:
        print("fjhug")
use()


xy=35
Tam=int(input("Tam:"))
Eng=int(input("Eng:"))
EVS=int(input("evs:"))
Hindi=int(input("Hn:"))
def answer():
    if (xy<Tam) and (xy<Eng) and (xy<EVS) and (xy<Hindi):
        print( "Pass" )
    else:
        print( "Fail" )
answer()
'''
def sanvi(en,an,yn):
    print("Name:",en)
    print("Place:",an)
    print("Pincode:",yn)
sanvi("vijay", "Mayiladuthurai", "609001")

def leo(n):
    return n*n*n
print(leo(3))

jleo=lambda m:m**2
print(jleo(5))

hnum=lambda k,v:k+v
print(hnum(21,23))

jnm=[2,4,3,6,5,8]
knm=list(map(lambda x:x*5,jnm))
print(knm)

abc=[23,89,54,14,3,24,68,90]
Even=list(filter(lambda a:a%2==0,abc))
print(Even)

efg=[23,89,54,14,3,24,68,90]
Odd=list(filter(lambda x:x%2!=0,efg))
print(Odd)

start=[23,89,54,14,3,24,68,90]
end=list(map(lambda a:a%2==0,start))
print(end)

start1=[23,89,54,14,3,24,68,90]
end1=list(map(lambda a:a%2!=0,start1))
print(end1)


ax=["Air", "Filter", "Birth", "Earth", "Unavailable", "Idea", "Logical"]
bx=['a','e','i','o','u']
div=list(filter(lambda ab:ab[0].lower() not in (bx),ax))
print(div)

# Feb 22
def an(m):
    return m*m*m
print(an(2))

I=lambda n:n**3
print(I(2))

II=lambda a,b:a*b
print(II(21,5))

Inum=[2,4,9,7,8]
mvalue=list(map(lambda a:a*3,Inum))
print(mvalue)

IInum=[23,89,80,58,45,34]
addvalue=list(map(lambda b:b+2,IInum))
print(addvalue)

IIInum=[45,48,34,89,76]
Sample1=list(filter(lambda c:c%2==0,IIInum))
print(Sample1)
Sample2=list(filter(lambda d:d%2!=0,IIInum))
print(Sample2)
'''
IVnum=[86,78,56,45,35,23,21]
mapfil=list(map(lambda e:e%2==0,IVnum))
print(mapfil)
mapfil2=list(map(lambda f:f%2!=0,IVnum))
print(mapfil2)
alpha=["Home", "Our Family", "Anniversary", "Everythin", "My Family", "Teacher"]
    alf=list(filter(lambda x:x=="A" and "E"
    print(x)
'''
a=["Home", "Our Family", "Anniversary","Teacher", "Earth", "Birthday"]
b=["a", "e", "i", "o", "u"]
al=list(filter(lambda xy:xy[0].lower() not in (b),a))
print(al)



# Feb 23
word=["Apple", "Best", "Choco", "Enable", "Idea", "Outstanding", "Student", "Teacher", "Understanding"]
b=["A", "E", "I", "O", "U"]
Alpha=list(filter(lambda x:x[0].upper() not in (b),word))
print(Alpha)

san=[23,54,67,56,43,67,89,45,32,42,58]
even=list(filter(lambda y:y%2==0,san))
print(even)

san=[23,54,67,56,43,67,89,45,32,42,58]
even=list(map(lambda y:y%2==0,san))
print(even)

# Feb 28
word=["Best", "Choco", "Enable", "Idea", "Outstanding", "Student"]
b=["A", "E", "I", "O", "U"]
for i in word:
    if i[0] in b:
        print(i)
print("--------")
Colour=["While", "Pink", "Blue", "Silver", "Gold", "Pistagreen", "Green"]
for x in Colour:
    if x[1] in "i":
        print(x)
print("--------")
xy=["While", "Pink", "Blue", "Silver", "Gold", "Pistagreen", "Green"]
for z in xy:
    if z[1] not in "i":
        print(z)
print("--------")
dhiv=["Student", "teacher", "best", "Family", "idea"]
for x in dhiv:
    if x[0] in x.upper():
        print(x)
print("--------")
dev=["long", "bee", "Short","Being", "tail"]
for x in dev:
    if x[0:-1]in x.lower():
        print(x)

vc=['hAppY', 'TALkIng', 'Best']
for n in vc:
    if "A" in n:
        print(n)

# March 06
ab1={"Blueberry", "Cherry", "Strawberry"}
ab2={"Berry", "Cherry", "Pineapple"}
ab3= ab1.difference(ab2)
ab4=ab1^ab2
print(ab3)
print(ab4)
print(type(ab4))


# March 07
Reg={
    "Username" : "yazh_rose",
    "Password" : "yazhu@12352"
    }
login=int(input("1.login, 2.signin  enter 1 or 2:"))
if login==1:
    print("Enter Your UserName")
    User=input("username:")
    Pass=input("password:")
    if Reg["Username"]==User and Reg["Password"]==Pass:
        print("Ready to Registration")
    else:
        print("Please Enter the correct Username & Password")
elif login==2:
    New={
        "NewUser":input("newusername:"),
        "NewPass":input("newpassword:")
        } 
    Reg.update(New)
    print(Reg) 
    NewUser1=input("Enter your NewUser:") 
    NewPass1=input("Enter your NewPass:")
    if Reg["NewUser"]==NewUser1 and Reg["NewPass"]==NewPass1:
        print("Ready to Registration")
    else:
        print("Enter Other Username") 
else:
    print("Enter No.1 = Old user << and >> Enter No.2 = New user")






    
