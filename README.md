# Regex-data-extraction: Data aggregation
# Pythonic Regular Expression Validator
This Python script provides a set of utility functions for validating common data formats using regular expressions for specific types of data you receive from the API.
## Data types 
Email addresses, 
URLs, 
Phone numbers, 
Credit card numbers, 
Time in 12-hour or 24-hour format, 
HTML tags, 
Hashtags, and 
Currency amounts. 
## specific data types
Phone numbers, 
Credit card numbers, 
Hashtags, 
Currency amounts, Email address, time and URLs

### This Python script includes the following functions:

#### 1.validate_email(email): 
This function validates email addresses using a regular expression that checks for the standard format of user@domain.tld.

#### 2.validate_url(URL):
This function is designed to determine if a given string is a valid URL.  It checks the URL against a defined pattern to ensure it follows the general structure of a web address. The code defines a function named validate_url that takes one argument (url (str):) the string that the function will check to see if it's a valid URL

#### 3.validate_phone_number(phone_number): 
Validates phone numbers in various formats, including (XXX) XXX-XXXX, XXX-XXX-XXXX, and XXX.XXX.XXXX.

#### 4.validate_credit_card_number(card_number): 
Validates credit card numbers with and without hyphens or spaces.

#### 5.validate_time(time_str): 
This function validates time strings in both 24-hour format (e.g., 14:30) and 12-hour format (e.g., 2:30 PM). It uses separate regular expressions for each format and checks if the input matches either of them.

#### 6.validate_hashtag(hashtag): 
Validates hashtags, ensuring they start with '#' and contain only alphanumeric characters and underscores.

#### 7.validate_currency_amount(amount): 
Validates currency amounts in the format of $X.XX, $X,XXX.XX, and $XX.XX

Each function uses a regular expression to check if the input string matches the expected format.  The code is well-documented with function-level comments and inline comments to explain the regular expressions.  The if __name__ == "__main__": block provides example test cases for each function, demonstrating their usage and expected output.

## Data extraction process
### Import re: 
The code begins by importing the re module, which provides regular expression operations in Python.

### Validation Functions:

Each validation function (validate_phone_number, validate_credit_card_number, etc.) takes a string as input, representing the data to be validated.

Inside each function, a regular expression pattern is defined to capture the specific format of the data being validated.

The re.match() function is used to check if the input string matches the pattern from the beginning of the string.

The function returns True if the input string matches the pattern (i.e., is valid), and False otherwise.

If the input string is empty, the function returns False.

### Regular Expression Patterns:

The core of each validation function is the regular expression pattern. These patterns are carefully crafted to match the allowed formats for each data type.

The patterns use special characters and syntax to define the rules for matching (e.g., \d for digits, ? for optional elements, * for zero or more occurrences, ^ and $ for start and end of string, respectively).

### Test Cases:

The if __name__ == "__main__": block contains a series of test cases for each validation function.

These test cases demonstrate how to use the functions and show the expected output for various inputs, including both valid and invalid data.

The test cases help to ensure that the functions are working correctly and handle different scenarios.

## Execution in VS
![Screenshot (47)](https://github.com/user-attachments/assets/2bf885cf-99bc-4470-80f2-16c7d96499c8)

## Execution in the webterm from Ubuntu
![Screenshot (48)](https://github.com/user-attachments/assets/6e099613-1938-45b1-802b-1b8b674ee8c4)


