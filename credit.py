from datetime import date, datetime
from unicodedata import name
from customers import *
from customer import *

class Payment():

    def __init__(self, idPayment,date,idCustomer,paymentValue,paymentCost,moratoriumInteres,expenses):        
     self.__idPayment = idPayment
     self.__date = date
     self.__idCustomer = idCustomer
     self.__paymentValue = paymentValue
     self.__paymentCost = paymentCost
     self.__moratoriumInterest = moratoriumInteres
     self.__expenses = expenses
     self.__applyValue = self.__paymentValue-self.__paymentCost-self.__moratoriumInterest-self.__expenses

    def paymentDetails(self):                
        print("\nID Payment: {}\nDate: {}\nId Customer: {}\nPayment Value: {:.2f}\nPayment Cost: {:.2f}\nMoratorium Interest: {:.2f}\nExpenses: {:.2f}\nApply Value: {:.2f}".format(self.__idPayment,self.__date,self.__idCustomer,self.__paymentValue,self.__paymentCost,self.__moratoriumInterest,self.__expenses,self.__applyValue))
    
        

    









