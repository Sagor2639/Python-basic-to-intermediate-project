#global, local and pas keyword in python

#What is Local and Global
#Here Data is global because it is easily access anywhere in this file
"""
data = " I am Global Value"  #Global variable

def test1( ):
    print("Access Global Value Inside function = ",data)
    data= 45  #Local data
    #data+=1 not possible 
    print("Local data=====",data)
def test2( ):
    print("Access Global Value Inside another Function = ",data)
    data = 698 #LOcal data
    print("Local data=====",data)
test1()
test2()


#Now we talk about Global Keyword
"""
"""
a = 78965
def new():
    global a
    print("previous===>",a)
    a+=9
    
    print("After change===",a)
new()

print("a====",a)
"""
"""
def new1():
    global a
    a = 78
    print("inner==>",a)
new1()
print(a)
"""
"""
x= 45 #global
def f1():
    
    x = 999 #Local
    print(x)
    #now i try to print global variable data when local variable data is present
    y = globals()["x"]
    print("Global value of x===",y)
f1()
"""

#Now we talk about pass----

"""
In Python programming, the pass statement is a null statement.
The difference between a comment and a pass statement in
Python is that while the interpreter ignores a comment entirely,
pass is not ignored.
"""


def hello():
      
    pass
hello()

for i in range(10):
    pass

if 45%5==0:
    pass

print("hello")
