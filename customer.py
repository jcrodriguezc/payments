class Customer():
    def __init__(self,idCustomer,name,address,phone):
        self.__idCustomer = idCustomer
        self.__name =  name        
        self.__address = address
        self.__phone = phone
    
    def customerDetails(self):        
        print("\nID Customer: {}\nName: {}\nAddress: {}\nPhone: {}".format(self.__idCustomer,self.__name,self.__address,self.__phone))