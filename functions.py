from pickletools import float8

def intValue():   
    con = 1 
    intValue = input("Enter the value: ")
    while con <3 and (intValue.isdigit() == False or len(intValue) < 1):        
        intValue = input("You have not entered a correct value, please try again: ")     
        con += 1    
    if intValue.isdigit():
        return int(intValue)
    else:
        return ""


def floatValue():
    con = 1    
    floatValue = input("Enter the value: ")
    while con < 3 and (floatValue.isdecimal() == False or len(floatValue) < 1):
        floatValue = input("You have not entered a correct value, please try again: ")
        con += 1
    if floatValue.isdecimal():
        return float(floatValue)
    else:
        return ""

def nameValidate(name):    
    val = True    
    for i in name[0]:
        if i == " ":
            val = False
            break
    for i in name:        
        if not(i.isalpha() or i ==" "):
            val = False
            break
    return val

def stringValue():
    con = 1
    stringValue = input("Enter the value: ")
    while con < 3 and (len(stringValue)<1 or nameValidate(stringValue) == False):
        stringValue = input("You have not entered a correct value, please try again: ")
        con +=1
    return stringValue

def addressValue():
    con = 1
    addressValue = input("Enter the value: ")
    while con < 3 and (addressValue =="" or addressValue ==" "):
        addressValue = input("You have not entered a correct value, please try again: ")
        con +=1
    return addressValue