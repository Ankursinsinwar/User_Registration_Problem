import re 

class User:

    def __init__(self, first_name, last_name, email, phone, password):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__phone = phone
        self.__password = password
    
    @property
    def first_name(self):
        return self.__first_name
    
    @property
    def last_name(self):
        return self.__last_name
    
    @property
    def email(self):
        return self.__email
    
    @property
    def phone(self):
        return self.__phone
    
    @property
    def password(self):
        return self.__password

    
    def __str__(self):
        return f'''
        First Name : {self.first_name} 
        Last Name  : {self.last_name}
        email      : {self.email}
        phone No.  : {self.phone}
        pasword    : {self.password}
'''




def validate_first_name(first_name):
    '''
    - Validate First name
      - 
      - First name should starts with capital letter 
      - first name should has atleast 3 characters
    '''
    try:
        pattern = "[A-Z][a-zA-Z]{2,}"
        if not re.match(pattern, first_name):
            raise ValueError(f"Error: First name should starts with Cap and should has minimum 3 characters")
        return first_name
    except ValueError as e:
        print(e)


def validate_last_name(last_name):
    '''
    - Validate Last name
      - 
      - Last name should starts with capital letter 
      - last name should has atleast 3 characters
    '''
    try:
        pattern = "[A-Z][a-zA-Z]{2,}"
        if not re.match(pattern, last_name):
            raise ValueError(f"Error: Last name should starts with Cap and should has minimum 3 characters")
        return last_name
    except ValueError as e:
        print(e)


def validate_email_name(email):
    '''
    - Validate Email
      - 
      - Validate username, symbol, domain in email address
    '''
    try:
        pattern = r"^[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)*@[a-zA-Z]+(\.[a-zA-Z0-9]+)+$"

        if not re.match(pattern, email):
            raise ValueError(f"Error: invalid email! ")
        return email
    except ValueError as e:
        print(e)


def validate_phone_no(phone):
    '''
    - Validate Phone number
      - 
      - Should starts with Country code follow by space and 10 digit number
    '''
    try:
        pattern = r"\d{1,2}\s\d{10}"
        if not re.match(pattern, phone):
            raise ValueError(f"Error: phone number should starts with Country code follow by space and 10 digit number")
        return phone
    except ValueError as e:
        print(e)


def validate_password(password):
    '''
    - Validate password
      - 
      - minimum 8 Characters
    '''
    try:
        pattern = r"[A-Za-z0-9]{8,}"
        if not re.match(pattern, password):
            raise ValueError(f"Error: Invalid password! ")
        return password
    except ValueError as e:
        print(e)



def main():
    while(True):
        first_name = input("Enter First name: ")
        last_name = input("Enter last name: ")
        email = input("Enter email: ")
        phone = input("Enter phone number: ")
        password = input("Enter password: ")
        if validate_first_name(first_name) and validate_last_name(last_name) and validate_email_name(email) and validate_phone_no(phone) and validate_password(password):
            user = User(first_name, last_name, email, phone, password)
            print(user)
            break


if __name__ == "__main__":
    main()