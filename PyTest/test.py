import pytest
import re


first_name_Pattern = r"^[A-Z][a-zA-Z]{2,}$"
last_name_Pattern = r"^[A-Z][a-zA-Z]{2,}$"
email_Pattern = r"^[a-zA-Z0-9+_-]+(\.[a-zA-Z0-9_-]+)*@[a-zA-Z0-9]+(\.[a-zA-Z]{2,}){1,2}$"
phone_Pattern = r"^\d{1,2}\s\d{10}$"
pasword_Pattern = r"^(?=.{8,}$)(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])[a-zA-Z0-9]*[-_@#$%+][a-zA-Z0-9]*$"




@pytest.mark.parametrize("first_name, expected", [
    ("Ankur", True),   
    ("ab", False),         
    ("firstname", False),  
    ("First1name", False),  
])
def test_fires_name(first_name, expected):
    assert bool(re.match(first_name_Pattern, first_name)) == expected



@pytest.mark.parametrize("last_name, expected", [
    ("Sinsinwar", True),   
    ("ab", False),         
    ("lastname", False),  
    ("Last1name", False),  
])
def test_last_name(last_name, expected):
    assert bool(re.match(first_name_Pattern, last_name)) == expected



@pytest.mark.parametrize("phone, expected", [
    ("91 9876543210", True),
    ("+919876543210", False),
    ("+91 9876543210", False),
    ("12345678", False),     
    ("123-456-789", False), 
])
def test_phone(phone, expected):
    assert bool(re.match(phone_Pattern, phone)) == expected



@pytest.mark.parametrize("email, expected", [
    ("abc@yahoo.com", True),
    ("abc-100@yahoo.com", True),
    ("abc.100@yahoo.com", True),
    ("abc111@abc.com", True),
    ("abc-100@abc.net", True),
    ("abc.100@abc.com.au", True),
    ("abc@1.com", True),
    ("abc@gmail.com.com", True),
    ("abc+100@gmail.com", True),
    ("abc123@gmail.a", False), 
    (".abc123@.com", False), 
    ("abc()*@gmail.com", False), 
    ("abc@%*.com", False), 
    ("abc..2002@gmail.com", False), 
    ("abc.@gmail.com", False), 
    ("abc@abc@gmail.com", False), 
    ("abc@gmail.com.1a", False), 
    ("abc@gmail.com.aa.au", False), 
])
def test_email(email, expected):
    assert bool(re.match(email_Pattern, email)) == expected



@pytest.mark.parametrize("password, expected", [
    ("Abcdef1@", True),    
    ("abcdef1@", False),   
    ("Abcdef@", False),    
    ("Abcdef1@@", False),  
    ("Abc1@", False),
])
def test_password(password, expected):
    assert bool(re.match(pasword_Pattern, password)) == expected




