from datetime import date, datetime
from functions import *
from customers import *
from credit import *

consecutive = 100000
def paymentConsecutive():
    global consecutive        
    consecutive += 1
    return "P"+str(consecutive)    

def datePayment():
    currentDate = datetime.now() 
    con = 1     
    date = input("Please enter the date of payment (YYYYMMDD): ")
    while con < 3 and type(date) != datetime:
        try:        
            date = datetime.strptime(date,'%Y%m%d')                        
            if date > currentDate:
                date = input("You have not entered a correct date, please enter the date of payment (YYYYMMDD): ") 
                con += 1     
        except ValueError:
            date = input("You have not entered a correct date, please enter the year of payment (YYYYMMDD): ")
            con +=1
    return date

def valCustomer():
    customer = intValue()
    con = 1
    while con < 3 and customer not in customers:
        print("The ID is not recognized")
        customer = intValue()
        con += 1
    return customer


#Funcion para crear un nuevo pago
payments = {}
def newPayment():
    global payments
    idPayment = ""
    idCustomer=""
    date = ""
    paymentValue=""
    paymentCost=""
    moratoriumInterest=""
    expenses=""    

    idPayment = paymentConsecutive()

    if idPayment != "":
        date = datePayment()

    if date !="":
        print("Please enter the customer ID number")
        idCustomer = valCustomer()
        
    if idCustomer != "":
        print("Please enter the value of the payment")
        paymentValue = floatValue()
    
    if paymentValue != "":        
        print("Please enter the cost of collection")
        paymentCost = floatValue()
    
    if paymentCost != "":
        print("Please enter the value of default interest")
        moratoriumInterest = floatValue()
    
    if moratoriumInterest != "":
        print("Please enter the value of the expenses")
        expenses = floatValue()
    
    if expenses != "":    
        if paymentValue-paymentCost-moratoriumInterest-expenses >= 0:    
            payments[idPayment] = Payment(idPayment,date,idCustomer,paymentValue,paymentCost,moratoriumInterest,expenses)
            print("The payment was successfully applied")
            payments[idPayment].paymentDetails()
        else:
            print("Payment cannot be created because the value to apply is negative")
    else:
        print("Did not enter a valid value")



#Funcion para listar los pagos
def paymentsList():
    print("Total pyments: ",len(payments))    
    i = 0
    for key in payments:                                
        print(payments[key].paymentDetails())
        i +=1
        if i < len(payments):
            print(input("Press a key to see the next payment"))

