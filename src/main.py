import re 

class User:

    def __init__(self, first_name):
        self.__first_name = first_name
    
    @property
    def first_name(self):
        return self.__first_name
    
    @first_name.setter
    def first_name(self, first_name):
        self.__first_name = first_name

    
    def __str__(self):
        return f"First Name: {self.first_name}"




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




def main():
    while(True):
        first_name = input("Enter First name: ")
        if validate_first_name(first_name):
            user = User(first_name)
            print(user)
            break


if __name__ == "__main__":
    main()