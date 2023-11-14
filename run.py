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
# menu options
# add Customer
# remove Customer
# update Customer
# list single Customer
# list all customers
