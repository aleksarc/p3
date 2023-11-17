![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **March 14, 2023**

## Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!


## Errors

While trying to append new customer to the Google Sheet I was getting this error:

Traceback (most recent call last):
  File "/Users/aleksandrocandido/Documents/Code Institute/P3/p3/run.py", line 95, in <module>
    menu()
  File "/Users/aleksandrocandido/Documents/Code Institute/P3/p3/run.py", line 62, in menu
    newCustomer()
  File "/Users/aleksandrocandido/Documents/Code Institute/P3/p3/run.py", line 92, in newCustomer
    details.append_row(customer.name, customer.surname, customer.phone, customer.email, customer.address, customer.city, customer.country)
TypeError: Worksheet.append_row() takes from 2 to 6 positional arguments but 8 were given

By looking at some posts I understood why it was working in the Love Sandwiches project and not on mine, posts like this https://gis.stackexchange.com/questions/381046/python-error-typeerror-append-takes-at-most-5-arguments-6-given where saying the number of parameters taken by the method was 5, and then I noticed that the first param alone is taking inputs, but instead of a single value, it can take a set/list of inputs that will then be added to their respective columns in the worksheet.

No critical erros, but during the developement some errors such as:

Traceback (most recent call last):
  File "/Users/aleksandrocandido/Documents/Code Institute/P3/p3/run.py", line 359, in <module>
    menu()
  File "/Users/aleksandrocandido/Documents/Code Institute/P3/p3/run.py", line 67, in menu
    deleteCustomer()
  File "/Users/aleksandrocandido/Documents/Code Institute/P3/p3/run.py", line 353, in deleteCustomer
    SHEET.worksheet('details').delete_rows(int(key))
                                           ^^^^^^^^
ValueError: invalid literal for int() with base 10: 'email'

These type of errors were resolved by adjusting the code to pass the intended value, and the program resumed to the expected behaviour.

## References 
Skip first row: https://stackoverflow.com/questions/30871545/iterating-through-a-list-of-lists-skip-the-first-list

Concepts of working with Dictionaries in Python: https://www.youtube.com/watch?v=Ye7HS0JXNYE&t=2s

Delete rows: https://www.youtube.com/watch?v=6H6pNXFZZg8&t=423s