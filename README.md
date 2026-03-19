# User Registration Problem

## Introduction

The User Registration Problem is a Python application used to Validate user's details. It validates user's first name, last name, Email address, phone number, password before creating user

## Features
 - validate user's first name
 - validate user's last name
 - validate user's email address
 - validate user's phone number
 - validate user's password



## Validation Rules
 - First/Last Name: Starts with a capital letter, minimum 3 characters

 - Email: Must follow standard email format (e.g., `username@domain.com`)

 -  Phone Number: Country code followed by space and  number (e.g., `91 9876543210`)

 - Password:
    - Minimum 8 characters
    - At least one uppercase letter
    - At least one digit
    - At least one special character


 ## Project Files
 ```
User_Registration_Problem/
│
├── src/
│   └── main.py
│
├── PyTest/
│   └── test.py
│
└── README.md
 ```

 ## How to Run

#### Run the main program:
```
python src/main.py
```

#### Run the tests:
- import pytest : **` pip install pytest `**
```
pytest PyTest/test.py
```

## Technologies Used
 - **Python**
 - **Regex**
 - **pytest**