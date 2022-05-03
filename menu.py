from customers import *
from payments import *
import sys

def menu():
    print("\n***MAIN MENU***\n1. Customers\n2. Payments\n3. List customers\n4. List payments \n5. Exit")
    optionMenu = input("Select one of the menu options: ")
    while optionMenu != "1" and optionMenu != "2" and optionMenu != "3" and optionMenu != "4" and optionMenu != "5":
        optionMenu = input("The selected option does not exist, please try again: ")        
    if optionMenu == "1":
        print("\n")
        customerMenu()
    elif optionMenu == "2":
        print("\n")
        paymentMenu()
        print(input("Press a key to continue..."))
        menu()
    elif optionMenu == "3":
        print("\n")
        customerList()
        print(input("Press a key to continue..."))
        menu()
    elif optionMenu == "4":
        print("\n")
        paymentsList()
        print(input("Press a key to return to the menu..."))
        menu()
    elif optionMenu =="5":
        sys.exit()

def customerMenu():
    print("\nCUSTOMER MENU\n1. Create customer\n2. Consult customer\n3. Delete customer\n4. Return")
    option = input("Select one of the menu options: ")
    while option != "1" and option != "2" and option != "3" and option != "4":
        option = input("The selected option does not exist, please try again")
    if option == "1":
        print("\nCREATE CUSTOMER")
        newCustomer()
        print(input("Press a key to continue..."))
        customerMenu()
    elif option == "2":
        print("\nCONSULT CUSTOMER")
        consultCustomer()
        print(input("Press a key to continue..."))
        customerMenu()
    elif option == "3":
        print("\nDELETE CUSTOMER")
        deleteCustomer()
        print(input("Press a key to continue..."))
        customerMenu()
    elif option == "4":
        menu()

def consultCustomer():
    print("Enter the customer ID:")
    customer = intValue()
    i = 1
    if type(customer) == int:
        while customer not in customers and i < 3:
            print("The ID is not registered")
            customer = intValue()
            i += 1            
        else:
            try:
                customers[customer].customerDetails()
                print(input("Press a key to continue..."))
                customerMenu()
            except:
                print("Number of attempts allowed exceeded (3)")
                customerMenu()
    else:
        print("Did not enter a valid value")
        customerMenu()

def deleteCustomer():
    print("Enter the customer ID to delete")
    customer = intValue()
    i = 1
    if type(customer) == int:
        while customer not in customers and i < 3:
            print("The ID is not registered")
            customer = intValue()
            i += 1            
        else:
            try:
                del customers[customer]
                print(input("The customer was successfully deleted, press a key to continue..."))
                customerMenu()
            except:
                print("Number of attempts allowed exceeded (3)")
                customerMenu()
    else:
        print("Did not enter a valid value")
        customerMenu()
    
def paymentMenu():
    print("\nPAYMENT MENU\n1. Create payment\n2. Consult payment\n3. Delete payment\n4. Return")
    option = input("Select one of the menu options: ")
    while option != "1" and option != "2" and option != "3" and option != "4":
        option = input("The selected option does not exist, please try again")
    if option == "1":
        print("\nCREATE PAYMENTS")
        newPayment()
        print(input("Press a key to continue..."))
        paymentMenu()
    elif option == "2":
        print("\nCONSULT PAYMENT")
        consultPayment()
        print(input("Press a key to continue..."))
        paymentMenu()
    elif option == "3":
        print("\nDELETE PAYMENT")
        deletePayment()
        print(input("Press a key to continue..."))
        paymentMenu()
    elif option == "4":
        menu()

def consultPayment():
    key = (input("Enter the payment to consult: ")).upper()        
    i = 1
    while key not in payments and i < 3:
        key = (input("Unrecognized payment, try again: ")).upper()                
        i += 1
    else:
        try:            
            payments[key].paymentDetails()
            print(input("Press a key to continue..."))
            paymentMenu()
        except:
            print("Number of attempts allowed exceeded (3)")
            paymentMenu()
    
def deletePayment():
    key = (input("Enter the payment to delete: ")).upper()        
    i = 1
    while key not in payments and i<3:
        key = (input("Unrecognized payment, try again: ")).upper()
        i += 1
    else:
        try:
            del payments[key]
            print(input("The payment was removed successfully, press a key to continue..."))
            paymentMenu()
        except:
            print("Number of attempts allowed exceeded (3)")
            paymentMenu()

menu()