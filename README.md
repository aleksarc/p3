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

### 1 While trying to append new customer to the Google Sheet I was getting this error:

Traceback (most recent call last):
  File "/Users/aleksandrocandido/Documents/Code Institute/P3/p3/run.py", line 95, in <module>
    menu()
  File "/Users/aleksandrocandido/Documents/Code Institute/P3/p3/run.py", line 62, in menu
    newCustomer()
  File "/Users/aleksandrocandido/Documents/Code Institute/P3/p3/run.py", line 92, in newCustomer
    details.append_row(customer.name, customer.surname, customer.phone, customer.email, customer.address, customer.city, customer.country)
TypeError: Worksheet.append_row() takes from 2 to 6 positional arguments but 8 were given

By looking at some posts I understood why it was working in the Love Sandwiches project and not on mine, posts like this https://gis.stackexchange.com/questions/381046/python-error-typeerror-append-takes-at-most-5-arguments-6-given where saying the number of parameters taken by the method was 5, and then I noticed that the first param alone is taking inputs, but instead of a single value, it can take a set/list of inputs that will then be added to their respective columns in the worksheet.

### 2 During the developement some errors such as:

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

### 3 Error invalid escape sequence
In the method to validate email, a regex uses a escape bar that causes a warning in Python:

python3 run.py
/Users/aleksandrocandido/Documents/Code Institute/P3/p3/run.py:364: SyntaxWarning: invalid escape sequence '\.'
  regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

Resolution: As the regex cannot be changed, added the r for raw string as suggested in https://stackoverflow.com/questions/52335970/how-to-fix-string-deprecationwarning-invalid-escape-sequence-in-python

### 4 Invalid Argument
Traceback (most recent call last):
  File "/Users/aleksandrocandido/Documents/Code Institute/P3/p3/run.py", line 393, in <module>
    menu()
  File "/Users/aleksandrocandido/Documents/Code Institute/P3/p3/run.py", line 62, in menu
    newCustomer()
  File "/Users/aleksandrocandido/Documents/Code Institute/P3/p3/run.py", line 101, in newCustomer
    currentList = SHEET.worksheet('details').get_values('D')
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages/gspread/utils.py", line 739, in wrapper
    return f(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages/gspread/worksheet.py", line 487, in get_values
    vals = fill_gaps(self.get(range_name, **kwargs))
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages/gspread/utils.py", line 739, in wrapper
    return f(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages/gspread/worksheet.py", line 1027, in get
    response = self.spreadsheet.values_get(range_name, params=params)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages/gspread/spreadsheet.py", line 175, in values_get
    r = self.client.request("get", url, params=params)
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages/gspread/client.py", line 93, in request
    raise APIError(response)
gspread.exceptions.APIError: {'code': 400, 'message': "Unable to parse range: 'details'!D", 'status': 'INVALID_ARGUMENT'}

Resolution: replace get_values() by col_values(): SHEET.worksheet('details').col_values(4)

### 5 PIP8 Heroku validation errors found:

Results:
24: E302 expected 2 blank lines, found 1
30: W293 blank line contains whitespace
45: E302 expected 2 blank lines, found 1
90: W293 blank line contains whitespace
91: E302 expected 2 blank lines, found 1
104: E225 missing whitespace around operator
106: E225 missing whitespace around operator
109: E265 block comment should start with '# '
111: E265 block comment should start with '# '
114: E265 block comment should start with '# '
116: E265 block comment should start with '# '
119: E265 block comment should start with '# '
121: E265 block comment should start with '# '
128: E265 block comment should start with '# '
129: E225 missing whitespace around operator
130: E265 block comment should start with '# '
133: E265 block comment should start with '# '
135: E265 block comment should start with '# '
152: E302 expected 2 blank lines, found 1
167: E231 missing whitespace after ','
167: E231 missing whitespace after ','
173: E128 continuation line under-indented for visual indent
174: E128 continuation line under-indented for visual indent
175: E128 continuation line under-indented for visual indent
177: W291 trailing whitespace
191: E302 expected 2 blank lines, found 1
204: E231 missing whitespace after ','
204: E231 missing whitespace after ','
210: E128 continuation line under-indented for visual indent
211: E128 continuation line under-indented for visual indent
212: E128 continuation line under-indented for visual indent
223: E302 expected 2 blank lines, found 1
250: E231 missing whitespace after ','
250: E231 missing whitespace after ','
253: W291 trailing whitespace
254: W291 trailing whitespace
255: W291 trailing whitespace
257: E128 continuation line under-indented for visual indent
257: W291 trailing whitespace
258: E128 continuation line under-indented for visual indent
258: W291 trailing whitespace
259: E128 continuation line under-indented for visual indent
260: E225 missing whitespace around operator
277: W293 blank line contains whitespace
396: E302 expected 2 blank lines, found 1
408: E231 missing whitespace after ','
408: E231 missing whitespace after ','
408: W291 trailing whitespace
411: W291 trailing whitespace
412: W291 trailing whitespace
413: W291 trailing whitespace
415: E128 continuation line under-indented for visual indent
415: W291 trailing whitespace
416: E128 continuation line under-indented for visual indent
416: W291 trailing whitespace
417: E128 continuation line under-indented for visual indent
418: E225 missing whitespace around operator
421: W293 blank line contains whitespace
441: W293 blank line contains whitespace
442: E302 expected 2 blank lines, found 1
452: E275 missing whitespace after keyword
452: E231 missing whitespace after ','
452: E711 comparison to None should be 'if cond is None
455: E225 missing whitespace around operator
461: E302 expected 2 blank lines, found 1
483: E302 expected 2 blank lines, found 1
485: W291 trailing whitespace
492: E225 missing whitespace around operator
496: E302 expected 2 blank lines, found 1
498: W291 trailing whitespace
503: E711 comparison to None should be 'if cond is None
504: E225 missing whitespace around operator
510: E302 expected 2 blank lines, found 1
512: E225 missing whitespace around operator
518: E225 missing whitespace around operator
522: E305 expected 2 blank lines after class or function definition, found 1

Resolution: fixed all erros as presented in list above, final result shows:

Results:
All clear, no errors found

## References 
Skip first row: https://stackoverflow.com/questions/30871545/iterating-through-a-list-of-lists-skip-the-first-list

Concepts of working with Dictionaries in Python: https://www.youtube.com/watch?v=Ye7HS0JXNYE&t=2s

Delete rows: https://www.youtube.com/watch?v=6H6pNXFZZg8&t=423s

Validate Email method provided by https://acervolima.com/verifique-se-o-endereco-de-e-mail-e-valido-ou-nao-em-python/

Validate string inputs for letters only: https://acervolima.com/python-string-isalpha-e-sua-aplicacao/
