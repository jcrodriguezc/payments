from customer import *
from functions import *

#Funcion para crear un nuevo cliente
customers = {}

def newCustomer():
    global customers                
    idCustomer=""
    name=""
    address=""
    phone=""
    
    print("ID number")
    idCustomer = intValue()
        
    if idCustomer != "":        
        print("Name ")
        name = stringValue()    
    
    if name != "":
        print("Address")
        address = addressValue()
        
    if address != "" and address != " ":
        print("Phone")
        phone = intValue()
        
    if phone != "":
        customers[idCustomer] = Customer(idCustomer,name,address,phone)
        print("The customer was successfully created")
        customers[idCustomer].customerDetails()
    else:
        print("You have not entered a valid value")


#Funcion para listar los clientes
def customerList():
    print("Total customers: ",len(customers))    
    i = 0
    for key in customers:
        customers[key].customerDetails()
        i +=1
        if i < len(customers):            
            print(input("Press a key to see the next customer"))