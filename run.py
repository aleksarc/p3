"""
Imported resources to make it possible working with Google Drive and Google
Sheets
"""
import re
import gspread
from google.oauth2.service_account import Credentials

"""
Scope and credentials defining the access the project has to
Google through APIs
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


class Customer:
    """
    Customer Class
    This is the main class which sets the attributes and methods used
    to manipulated customer's database
    """
    def __init__(self, name, lastname, phone, email, address, city,
                 country):
        """
        __init__
        constructor used to create a new instance of the the Customer Class
        """
        self.name = name
        self.lastname = lastname
        self.phone = phone
        self.email = email
        self.address = address
        self.city = city
        self.country = country


def menu():
    """
    The meny method will display options to the user.
    Each option will call the respective method to perform an action in the
    customers database.
    The user should type an available option based on the numbers presented
    along with their actions.
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
    option = input('Type an option number: \n')
    print('')
    if option == '1':
        newCustomer()
    elif option == '2':
        updateCustomer()
    elif option == '3':
        deleteCustomer()
    elif option == '4':
        listSingleCustomer()
    elif option == '5':
        listAllCustomers()
    elif option == '6':
        print('======================')
        print('## Program finished ##')
        print('======================\n')
        print('')
    else:
        print('')
        print('====================')
        print('## Invalid option ##')
        print('====================\n')
        menu()


def newCustomer():
    """
    The newCustomer() method is used to create a new instance of the
    Customer Class as well as send
    new customer's detais to the Google Sheet using gspread.
    The user will be requested a series of input fields in order to create
    the new customer.
    The method will then call the constructor of the Customer Class passing
    the inputed details as parameters
    and also use the apend_row method of worksheets to add a new line
    (new customer) to the Google Sheet
    """
    print("Let's crete a new customer!")
    print('Note: Email address will be used as a customer key and must be' +
          'unique.')
    print("If you are not sure of existing email addresses, use the List" +
          "All Customers option to review the customer's list.")
    print('Provide new customer details as requested below:\n')
    # check input for a valid email pattern
    tempEmail = validateEmail(input('Email: \n'))
    # check duplicate email addresses
    email = checkDuplicate(tempEmail)
    print('')
    # validate name input for letters only)
    tempName = validateString(input('Name: \n'))
    # check if value is empty or null
    name = checkNonEmptyNull(tempName)
    print('')
    # validate lastname input for letters only)
    templastname = validateString(input('Last Name: \n'))
    # check if value is empty or null
    lastname = checkNonEmptyNull(templastname)
    print('')
    phone = validatePhone(input('Phone: \n'))
    print('')
    address = input('Address: \n')
    print('')
    # validate lastname input for letters only)
    tempcity = validateString(input('City: \n'))
    # check if value is empty or null
    city = checkNonEmptyNull(tempcity)
    print('')
    # validate lastname input for letters only)
    tempcountry = validateString(input('Country: \n'))
    # check if value is empty or null
    country = checkNonEmptyNull(tempcountry)

    customer = Customer(name, lastname, phone, email, address, city,
                        country)
    print('')
    print('New customer created:\n')
    print(customer.name, customer.lastname, customer.phone, customer.email,
          customer.address, customer.city, customer.country)
    print('')
    details = SHEET.worksheet('details')
    details.append_row([customer.name, customer.lastname, customer.phone,
                        customer.email, customer.address, customer.city,
                        customer.country])
    print('New customer added to database!')
    menu()


def listSingleCustomer():
    """
    The listSingleCustomer() method will create an object retrieving all
    details from customers available in Google Sheets
    These details will be inserted into a Dictionary that will then allow
    for search by key (which is defined as email).
    The user will be requested the key/email as input and the system prints
    the details of the customer based on the provided key/email.
    """
    details = SHEET.worksheet('details').get_values()
    customers = {}
    for index, values in enumerate(details):
        if index == 0:
            continue
        if values:
            customer = Customer(values[0], values[1], values[2], values[3],
                                values[4], values[5], values[6])
            customers[customer.email] = {'name': customer.name,
                                         'lastname': customer.lastname,
                                         'phone': customer.phone,
                                         'email': customer.email,
                                         'address': customer.address,
                                         'city': customer.city,
                                         'country': customer.country}
        else:
            None
    key = validateEmail(input('Type customer email: \n'))
    if key in customers:
        print('')
        print('Customer found: \n')
        print(customers[key])
        menu()
    else:
        print('')
        print('===============')
        print('## Not Found ##')
        print('===============')
        menu()


def listAllCustomers():
    """
    The listAllCustomers() method calls the get_values() Google Sheet
    method to retrieve all details available in the Google Sheet.
    These details are inserted into a Dicitionary and printed as output
    for the user's visilibity.
    """
    details = SHEET.worksheet('details').get_values()
    customers = {}
    for index, values in enumerate(details):
        if index == 0:
            continue
        if values:
            customer = Customer(values[0], values[1], values[2], values[3],
                                values[4], values[5], values[6])
            customers[customer.email] = {'name': customer.name,
                                         'lastname': customer.lastname,
                                         'phone': customer.phone,
                                         'email': customer.email,
                                         'address': customer.address,
                                         'city': customer.city,
                                         'country': customer.country}
        else:
            None

    print('Listing all customers:\n')
    for customer, values in customers.items():
        print(str(values))
    print('')
    print('End of the list')
    menu()


def updateCustomer():
    """
    The updateCustomer() method retrieves all customers information from
    Google Sheet using the get_values() method and inserting the values
    into a Dictionary.
    The user will be presented with an options menu where they can choose
    which data to be updated in the customer's database. The user will also
    provide the key/email of the customer to be updated.
    Each option in the menu will bring the user to a different condition in
    the code, within the condition the new value will be requested/inputed
    from the user.
    The new value is then passed to the Google Sheet with
    worksheet.update_cell() method and the local Dictionary is also updated
    to show new details to the user.
    Because email is used as key for the Dictionary, whenever the user
    chooses to update the email field, the current customer is replaced by
    a new customer in the Dictionary as there's no option to update the key
    value.
    """
    details = SHEET.worksheet('details').get_values()
    customers = {}
    counter = 2
    tempInd = 0
    for index, values in enumerate(details):
        if index == 0:
            continue
        if values:
            customer = Customer(values[0], values[1], values[2], values[3],
                                values[4], values[5], values[6])
            customers[customer.email] = {'ind': counter,
                                         'name': customer.name,
                                         'lastname': customer.lastname,
                                         'phone': customer.phone,
                                         'email': customer.email,
                                         'address': customer.address,
                                         'city': customer.city,
                                         'country': customer.country}
            counter += 1
        else:
            None

    key = validateEmail((input('Enter the email of the customer to '
                               + 'update: \n')))
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
        print('===============')
        menu()

    print('Which detail do you want to update?')
    print(
        '''
        [1] Name
        [2] Last Name
        [3] Phone
        [4] Email
        [5] Address
        [6] City
        [7] Country
        '''
    )
    inpt = input('Enter the option number: \n')
    print('')
    # update name
    if inpt == '1':
        print('')
        data = validateString(input('Enter the new value: \n'))
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
        menu()
    # update lastname
    elif inpt == '2':
        print('')
        data = validateString(input('Enter the new value: \n'))
        print('')
        print('Updating customer...')
        SHEET.worksheet('details').update_cell(int(tempInd), 2, str(data))
        customers[key]['lastname'] = data
        print('')
        print('Last Name has been updated.')
        print('')
        print('New customer details:')
        print('')
        print(customers[key])
        menu()
    # update phone
    elif inpt == '3':
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
        menu()
    # update email
    # here the email key will be replaced, thus the current row will be
    # removed from the worksheet and a new row will be created
    # for this to happen, the current value is copied to a temp list
    # in the dictionary, a new email key is provided and these temp
    # data attributed to the new key, with the new key and values
    # copied from the previous customer, a new row will be added to the
    # worksheet.
    # currently is not possible to replace a key value in a dictionary
    # thus the above workaround used
    elif inpt == '4':
        print('')
        data = validateEmail(input('Enter the new value: \n'))
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
        menu()
    # update address
    elif inpt == '5':
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
        menu()
    # update city
    elif inpt == '6':
        print('')
        data = validateString(input('Enter the new value: \n'))
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
        menu()
    # update country
    elif inpt == '7':
        print('')
        data = validateString(input('Enter the new value: \n'))
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
        menu()
    # return error if all validations failed
    else:
        print('Something went wrong :(')
        menu()


def deleteCustomer():
    """
    The delteCustomer() method will take an input of email to find the customer
    using the email key.
    Once found, the customer will be shown in the screen and subssequentially
    deleted from the Google Sheet.
    The email key is used to find the customers in the worksheet, and a
    tempIndex (numeric value) will identify the customer's index in the
    worksheet. This tempIndex will be used to send a delete_row() command
    to delete the customer from the worksheet.
    Finally, a customer deleted message will be shown to the user. At this
    point the customer was already deleted from the worksheet.
    """
    details = SHEET.worksheet('details').get_values()
    customers = {}
    counter = 2
    tempInd = 0
    for index, values in enumerate(details):
        if index == 0:
            continue
        if values:
            customer = Customer(values[0], values[1], values[2], values[3],
                                values[4], values[5], values[6])
            customers[customer.email] = {'ind': counter,
                                         'name': customer.name,
                                         'lastname': customer.lastname,
                                         'phone': customer.phone,
                                         'email': customer.email,
                                         'address': customer.address,
                                         'city': customer.city,
                                         'country': customer.country}
            counter += 1
        else:
            None

    key = validateEmail(input('Enter the email of the customer to delete: \n'))
    if key in customers:
        print('')
        print('Customer found: \n')
        print(customers[key])
        tempInd = customers[key]['ind']
    else:
        print('')
        print('===============')
        print('## Not Found ##')
        print('===============')
        menu()
    print('')
    print('Deleting customer...')
    SHEET.worksheet('details').delete_rows(int(tempInd))
    print('')
    customerName = {customers[key]['name']}
    customerLastName = {customers[key]['lastname']} 
    print(f'Customer {customerName} {customerLastName} was deleted.')
    menu()


def validateEmail(email):
    """
    The validateEmail() method will check for valid characters inputed by
    the user.
    Returns the email address to be added in the new customer record in
    case it's validated and
    requests new input providing an example of acceptable pattern in case
    the user types an invalid email address.
    """
    regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if (re.search(regex, email)) is None:
        print('!!! Invalid email address !!!')
        print('')
        email = validateEmail(input('Enter email' +
                                    '(e.g. email@email.com): \n'))
        return email
    else:
        return email


def checkDuplicate(email):
    """
    The checkDuplicate() method will retrieve a list with current emails
    existing in the GoogleSheet and
    in case the email already exists, it will request the user to input a
    new email address, otherwise
    add the inputed email to the correspondent attribute of new customer.
    This method also calls for validateEmail() as the user might need to
    input a new address in case
    the inputed email already exists.
    """
    currentList = SHEET.worksheet('details').col_values(4)
    if (email in currentList):
        print('')
        print('Customer already exists')
        print('')
        tempEmail = validateEmail(input('Enter a new email: \n'))
        email = checkDuplicate(tempEmail)
        return email
    else:
        return email


def validateString(data):
    """
    The validateString() method will check for letters only to prevent
    the user from entering numbers or other characaters
    where not expected
    """
    if data.isalpha():
        return data
    else:
        data = validateString(input('Invalid input, enter new value (only' +
                                    ' letters allowed): \n'))
        return data


def checkNonEmptyNull(data):
    """
    The checkNonEmptyNull() method validates if the inputed value is not
    empty or null(None).
    In case the user presses enter with no value, the method will require
    a new input until the condition is satisfied.
    """
    if data is None or data == '':
        data = checkNonEmptyNull(input('Value cannot be empty or null.' +
                                       ' Type new value: \n'))
        return data
    else:
        return data


def validatePhone(phone):
    """
    The validatePhone() method validates if the inputed value is shorter than
    10 numbers and also if it's only comprised of numbers by using the
    isdecimal() function.
    Using this method the user is required to input a valid 10 digits number
    which attends for most of the phone numbers known today.
    """
    if len(phone) > 10:
        phone = validatePhone(input('Type phone number with max 10' +
                                    ' digits: \n'))
        return phone
    elif phone.isdecimal():
        return phone
    else:
        phone = validatePhone(input('Type a valida phone (only numbers' +
                                    ' allowed): \n'))
        return phone


menu()
