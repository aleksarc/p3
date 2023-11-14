"""
Imported resources to make it possible working with Google Drive and Google Sheets
"""
import gspread
from google.oauth2.service_account import Credentials

"""
Scope and credentials defining the extension of access the project has do Google through APIs
"""
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('customers')

"""
Customer Class
This is the main class which sets the attributes and methods used to manipulated customer's database
"""
class Customer:
    
    """
    __init__
    constructor used to create a new instance of the the Customer Class
    """
    def __init__(self, name, surname, phone, email, address, city, country):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.email = email
        self.address = address
        self.city = city
        self.country = country


#methods to be created:
# remove Customer
# update Customer
# list single Customer
# list all customers

def menu():
    
    print(
        '''
        ## Options Menu ##\n
        [1] Add New Customer
        [2] Update Customer
        [3] Delete Customer
        [4] List Single Customer
        [5] List All Customers
        [6] Exit
        '''
    )
    option = int(input('Type an option number to start: \n'))
    if option == 1:
        newCustomer()
    elif option == 2:
        print('Call Update method')
    elif option == 3:
        print('Call Delete method')
    elif option == 4:
        listSingleCustomer()
    elif option == 5:
        print('Call list all method')
    elif option == 6:
        print('You exited the program')
    else:
        print('Invalid option')
        print('==============')
        menu()
    
def newCustomer():
    print('Enter new customer details: \n')
    name = input('Name: \n')
    surname = input('Surname: \n')
    phone = input('Phone: \n')
    email = input('Email: \n')
    address = input('Address: \n')
    city = input('City: \n')
    country = input('Country: \n')

    customer = Customer(name, surname, phone, email, address, city, country)
    print('New customer created!')
    print(customer.name, customer.surname)
    details = SHEET.worksheet('details')
    details.append_row([customer.name, customer.surname, customer.phone, customer.email, customer.address, customer.city, customer.country])
    print('New customer added to database!')

def listSingleCustomer():
    allCustomers = SHEET.worksheet('details').get_all_values()
    for customer in allCustomers:
        print(customer)

menu()
