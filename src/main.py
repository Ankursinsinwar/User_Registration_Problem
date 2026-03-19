import re 

class User:

    def __init__(self, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name
    
    @property
    def first_name(self):
        return self.__first_name
    
    @property
    def last_name(self):
        return self.__last_name

    
    def __str__(self):
        return f'''
        First Name : {self.first_name} 
        Last Name  : {self.last_name}'''




def validate_first_name(first_name):
    '''
    - Validate First name
      - 
      - First name should starts with capital letter 
      - irst name should has atleast 3 characters
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
      - irst name should has atleast 3 characters
    '''
    try:
        pattern = "[A-Z][a-zA-Z]{2,}"
        if not re.match(pattern, last_name):
            raise ValueError(f"Error: Last name should starts with Cap and should has minimum 3 characters")
        return last_name
    except ValueError as e:
        print(e)




def main():
    while(True):
        first_name = input("Enter First name: ")
        last_name = input("Enter last name: ")
        if validate_first_name(first_name) and validate_last_name(last_name):
            user = User(first_name,last_name)
            print(user)
            break


if __name__ == "__main__":
    main()