#practice questin
#write a program to check the upper and lower case of any input string
"""
===========================================

def check(data):
    d = {"upper": 0, "lower": 0}
    for i in data:
        if i.isupper():
            d["upper"]+=1
                    
        elif i.islower():
            d["lower"]+=1
        else:
            pass
    print("Actual string: ", data, "len==", len(data))
    print("No. of upper case char: ", d["upper"])
    print("No. of lwer case char: ", d["lower"])
check("I love Deutschlan")
"""
"""
#wap to that accept comma string of word and then sort it in a alphabeticle order with space
separate e.g: input - -> "hello, zebra, cool, jam, vsdk, best, success, gun"
===================================


def check_strng(data):
    data = data.split(",")
    print("data ----", data)
    data.sort()
    data = "".join(data)
    print(data)
check_strng("hello, zebra, cool, jam, vsdk, best, success, gun")
"""

#wap to check number of local variables in a function

def var():
    x = 2
    y  = 3
    z = "I love programming"
    print("Python module")
print(var.__code__.co_nlocals)






















