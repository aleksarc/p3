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


#methods to be developed:
# remove Customer

def menu():
    """
    The meny method will display options to the user.
    Each option will call the respective method to perform an action in the customers database.
    The user should type an available option based on the numbers presented along with their actions.
    """
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
    option = int(input('Type an option number: \n'))
    print('')
    if option == 1:
        newCustomer()
    elif option == 2:
        updateCustomer()
    elif option == 3:
        print('Call Delete method')
    elif option == 4:
        listSingleCustomer()
    elif option == 5:
        listAllCustomers()
    elif option == 6:
        print('')
        print('======================')
        print('## Program finished ##')
        print('======================\n')
    else:
        print('')
        print('====================')
        print('## Invalid option ##')
        print('====================\n')
        menu()
    
def newCustomer():
    """
    The newCustomer() method is used to create a new instance of the Customer Class as well as send
    new customer's detais to the Google Sheet using gspread.
    The user will be requested a series of input fields in order to create the new customer.
    The method will then call the constructor of the Customer Class passing the inputed details as parameters
    and also use the apend_row method of worksheets to add a new line (new customer) to the Google Sheet
    """
    print('Enter new customer details: \n')
    name = input('Name: \n')
    surname = input('Surname: \n')
    phone = input('Phone: \n')
    email = input('Email: \n')
    address = input('Address: \n')
    city = input('City: \n')
    country = input('Country: \n')

    customer = Customer(name, surname, phone, email, address, city, country)
    print('New customer created!\n')
    print(customer.name, customer.surname, customer.phone, customer.email, customer.address, customer.city, customer.country)
    print('')
    details = SHEET.worksheet('details')
    details.append_row([customer.name, customer.surname, customer.phone, customer.email, customer.address, customer.city, customer.country])
    print('New customer added to database!\n')
    menu()

def listSingleCustomer():
    """
    The listSingleCustomer() method will create an object retrieving all details from customers available in Google Sheets
    These details will be inserted into a Dictionary that will then allow for search by key (which is defined as email).
    The user will be requested the key/email as input and the system prints the details of the customer based on the provided key/email.
    """
    details = SHEET.worksheet('details').get_values()
    customers = {}
    for index, values in enumerate(details):
        if index == 0:
            continue
        if values:
            customer = Customer(values[0],values[1],values[2], values[3], values[4], values[5], values[6])
            customers[customer.email] = {'name': customer.name, 'surname': customer.surname, 'phone': customer.phone, 'email': customer.email,
                                        'address': customer.address, 'city': customer.city, 'country': customer.country}
        else:
            None   
    key = input('Type customer email: \n')
    if key in customers:
        print('')
        print('Customer found: \n')
        print(customers[key])
        print('')
    else:
        print('')
        print('===============')
        print('## Not Found ##')
        print('===============\n')
        menu()

def listAllCustomers():
    """
    The listAllCustomers() method calls the get_values() Google Sheet method to retrieve all details available in the Google Sheet.
    These details are inserted into a Dicitionary and printed as output for the user's visilibity.
    """
    details = SHEET.worksheet('details').get_values()
    customers = {}
    for index, values in enumerate(details):
        if index == 0:
            continue
        if values:
            customer = Customer(values[0],values[1],values[2], values[3], values[4], values[5], values[6])
            customers[customer.email] = {'name': customer.name, 'surname': customer.surname, 'phone': customer.phone, 'email': customer.email,
                                        'address': customer.address, 'city': customer.city, 'country': customer.country}
        else:
            None

    print('')
    print('Listing all customers:\n')
    for customer, values in customers.items():
        print(str(values))
    print('')
    print('End of the list\n')
    menu()

def updateCustomer():
    """
    The updateCustomer() method retrieves all customers information from Google Sheet using the get_values() method and inserting the values into a
    Dictionary.
    The user will be presented with an options menu where they can choose which data to be updated in the customer's database. The user will also provide
    the key/email of the customer to be updated.
    Each option in the menu will bring the user to a different condition in the code, within the condition the new value will be requested/inputed from the user.
    The new value is then passed to the Google Sheet with worksheet.update_cell() method and the local Dictionary is also updated to show new details to the user.
    Because email is used as key for the Dictionary, whenever the user chooses to update the email field, the current customer is replaced by a new customer
    in the Dictionary as there's no option to update the key value.
    """
    details = SHEET.worksheet('details').get_values()
    customers = {}
    counter = 2
    tempInd = 0
    for index, values in enumerate(details):
        if index == 0:
            continue
        if values:
            customer = Customer(values[0],values[1],values[2], values[3], values[4], values[5], values[6])
            customers[customer.email] = {'ind': counter,'name': customer.name, 'surname': customer.surname, 'phone': customer.phone, 'email': customer.email,
                                        'address': customer.address, 'city': customer.city, 'country': customer.country}
            counter+=1
        else:
            None

    key = input('Enter the email of the customer to update: \n')
    if key in customers:
        print('')
        print('Customer found: \n')
        print(customers[key])
        print('')
        tempInd = customers[key]['ind']
    else:
        print('')
        print('===============')
        print('## Not Found ##')
        print('===============\n')
        menu()
    
    print('Which detail do you want to update?')
    print(
        '''
        [1] Name
        [2] Surname
        [3] Phone
        [4] Email
        [5] Address
        [6] City
        [6] Country
        '''
    )
    print('')
    inpt = input('Enter the option number: \n')

    if int(inpt) == 1:
        print('')
        data = input('Enter the new value: \n')
        print('')
        print('Updating customer...')
        SHEET.worksheet('details').update_cell(int(tempInd), 1, str(data))
        customers[key]['name'] = data
        print('')
        print('Name has been updated.')
        print('')
        print('New customer details:')
        print('')
        print(customers[key])
        print('')
        menu()
    elif int(inpt) == 2:
        print('')
        data = input('Enter the new value: \n')
        print('')
        print('Updating customer...')
        SHEET.worksheet('details').update_cell(int(tempInd), 2, str(data))
        customers[key]['surname'] = data
        print('')
        print('Surname has been updated.')
        print('')
        print('New customer details:')
        print('')
        print(customers[key])
        print('')
        menu()
    elif int(inpt) == 3:
        print('')
        data = input('Enter the new value: \n')
        print('')
        print('Updating customer...')
        SHEET.worksheet('details').update_cell(int(tempInd), 3, str(data))
        customers[key]['phone'] = data
        print('')
        print('Phone has been updated.')
        print('')
        print('New customer details:')
        print('')
        print(customers[key])
        print('')
        menu()
    elif int(inpt) == 4:
        print('')
        data = input('Enter the new value: \n')
        print('')
        print('Updating customer...')
        SHEET.worksheet('details').update_cell(int(tempInd), 4, str(data))
        customers[data] = customers.pop(key)
        customers[data]['email'] = data
        key = data
        print('')
        print('Email has been updated.')
        print('')
        print('New customer details:')
        print('')
        print(customers[key])
        print('')
        menu()
    elif int(inpt) == 5:
        print('')
        data = input('Enter the new value: \n')
        print('')
        print('Updating customer...')
        SHEET.worksheet('details').update_cell(int(tempInd), 5, str(data))
        customers[key]['address'] = data
        print('')
        print('Address has been updated.')
        print('')
        print('New customer details:')
        print('')
        print(customers[key])
        print('')
        menu()
    elif int(inpt) == 6:
        print('')
        data = input('Enter the new value: \n')
        print('')
        print('Updating customer...')
        SHEET.worksheet('details').update_cell(int(tempInd), 6, str(data))
        customers[key]['city'] = data
        print('')
        print('City has been updated.')
        print('')
        print('New customer details:')
        print('')
        print(customers[key])
        print('')
        menu()
    elif int(inpt) == 7:
        print('')
        data = input('Enter the new value: \n')
        print('')
        print('Updating customer...')
        SHEET.worksheet('details').update_cell(int(tempInd), 7, str(data))
        customers[key]['country'] = data
        print('')
        print('Country has been updated.')
        print('')
        print('New customer details:')
        print('')
        print(customers[key])
        print('')
        menu()
    else:
        print('Something went wrong :(')
        print('')
        menu()

def deleteCustomer():
    """
    Still studying a way to delete a row in Google Sheets, for the moment thinking to use deleteDimension.
    """
    print("delete")

menu()
