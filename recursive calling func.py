#recursion in python

#recursion is defined as a function calling itself,
#until and unless it met with base condition. Advantahe is solve large
#problems very easily and disadvantage is time, space complexity both are
#high as compared with irteration
 
def text(x):
    print("hello")
   # text(x)
text(34)

#First find base condition
#Second Generalize the problem
#Optimize the Problem

#Find the sum of 5 natural number

def sum(x):
    if x ==1:
        return 1
    else:
        print("x====",x)
        
        return sum(x-1) +x
print(sum(5)) # output is 15
"""

#Reverse String using recursive calling

def data(z):
    if len(z)==0:
        return z
    else:
        print("z===",z)
        return data(z[1:])+z[0] # main logic 
data("i love deutschland")
"""


def fact_iter(data): #factorial of any number easy peasy
    fact = 1
    i = 1
    while i<=data:
        print('x==', data)
        fact = fact*i
        i+=1
        
    print("Using Iter==",fact)
fact_iter(4)


#factorial
def fact_rec(data):
    if data==1:
        return data
    else:
        #print("Value of number====>",data)
        a = (fact_rec(data-1) * data) #logic of recursion
        #print("result====",a)
        return a
print("Using Recurrsion==>",fact_rec(5))    

#Now write number of handshakes by n peoples
"""
def handshakes(peoples):
    if peoples<=1:
        return 0
    else:
        return (peoples*(peoples-1))/2
print(handshakes(6))

"""