#!/usr/bin/env python4
import re

def validate_phone_number(phone_number):
    """
    Validates phone numbers in various formats:
    - (123) 456-7890
    - 123-456-7890
    - 123.456.7890
    - 1234567890
    Args:
        phone_number (str): The phone number string to validate.

    Returns:
        bool: True if the phone number is valid, False otherwise.
    """
    # Regex pattern for phone number validation
    pattern = r"^(?:\(\d{3}\)|\d{3})[-.\s]?\d{3}[-.\s]?\d{4}$"
    # ^ - start of string
    # (?:\(\d{3}\)|\d{3}) - Non-capturing group, matches either (XXX) or XXX
    # [-.\s]? - Optional hyphen, dot, or whitespace
    # \d{3} - Three digits
    # [-.\s]? - Optional hyphen, dot, or whitespace
    # \d{4} - Four digits
    # $ - end of string

    if not phone_number:  # added check for empty string
        return False

    return bool(re.match(pattern, phone_number))



def validate_credit_card_number(card_number):
    """
    Validates credit card numbers in the following formats:
    - 1234 5678 9012 3456
    - 1234-5678-9012-3456
    - 1234567890123456
    Args:
        card_number (str): The credit card number string to validate.

    Returns:
        bool: True if the credit card number is valid, False otherwise.
    """
    # Regex pattern for credit card number validation
    pattern = r"^(?:\d{4}[- ]?){3}\d{4}$"
    # ^ - start of string
    # (?:\d{4}[- ]?){3} - Non-capturing group, matches four digits followed by optional hyphen or space, repeated three times
    # \d{4} - Four digits
    # $ - end of string
    if not card_number: # added check for empty string
        return False
    return bool(re.match(pattern, card_number))



def validate_hashtag(hashtag):
    """
    Validates hashtags.
    - #example
    - #ThisIsAHashtag
    Args:
        hashtag (str): The hashtag string to validate.

    Returns:
        bool: True if the hashtag is valid, False otherwise.
    """
    # Regex pattern for hashtag validation
    pattern = r"^#[a-zA-Z0-9_]+$"
    # ^ - start of string
    # # - literal '#'
    # [a-zA-Z0-9_]+ - One or more alphanumeric characters or underscores
    # $ - end of string
    if not hashtag: # added check for empty string
        return False
    return bool(re.match(pattern, hashtag))


def validate_currency_amount(amount):
    """
    Validates currency amounts.
    - $19.99
    - $1,234.56
    - $100
    - $0.01
    Args:
        amount (str): The currency amount string to validate.

    Returns:
        bool: True if the currency amount is valid, False otherwise.
    """
    # Regex pattern for currency amount validation
    pattern = r"^\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?$"
    # ^ - start of string
    # \$ - literal '$'
    # \d{1,3} - one to three digits
    # (?:,\d{3})* - Non-capturing group, zero or more occurrences of: comma followed by three digits
    # (?:\.\d{2})? - Optional non-capturing group:  dot followed by two digits
    # $ - end of string
    if not amount: # added check for empty string
        return False
    return bool(re.match(pattern, amount))

if __name__ == "__main__":
    # Test cases
    print("Phone Number Validation:")
    print(f"(123) 456-7890: {validate_phone_number('(123) 456-7890')}")  # True
    print(f"123-456-7890: {validate_phone_number('123-456-7890')}")    # True
    print(f"123.456.7890: {validate_phone_number('123.456.7890')}")    # True
    print(f"1234567890: {validate_phone_number('1234567890')}")      # True
    print(f"12-34-5678: {validate_phone_number('12-34-5678')}")      # False
    print(f"abc-def-ghij: {validate_phone_number('abc-def-ghij')}")  # False
    print(f"(123)456-7890: {validate_phone_number('(123)456-7890')}") # True
    print(f" : {validate_phone_number('')}") # False

    print("\nCredit Card Number Validation:")
    print(f"1234 5678 9012 3456: {validate_credit_card_number('1234 5678 9012 3456')}")  # True
    print(f"1234-5678-9012-3456: {validate_credit_card_number('1234-5678-9012-3456')}")  # True
    print(f"1234567890123456: {validate_credit_card_number('1234567890123456')}")      # True
    print(f"1234 5678 9012: {validate_credit_card_number('1234 5678 9012')}")          # False
    print(f"1234-5678-9012: {validate_credit_card_number('1234-5678-9012')}")          # False
    print(f"123456789012345: {validate_credit_card_number('123456789012345')}")        # False
    print(f"1234 abcdef 9012 3456: {validate_credit_card_number('1234 abcdef 9012 3456')}") # False
    print(f" : {validate_credit_card_number('')}") # False

    print("\nHashtag Validation:")
    print(f"#example: {validate_hashtag('#example')}")          # True
    print(f"#ThisIsAHashtag: {validate_hashtag('#ThisIsAHashtag')}")  # True
    print(f"#123: {validate_hashtag('#123')}")              # True
    print(f"#_underscore: {validate_hashtag('#_underscore')}") # True
    print(f"example: {validate_hashtag('example')}")          # False
    print(f"#: {validate_hashtag('#')}")                  # False
    print(f"#ThisIsAHashtag!: {validate_hashtag('#ThisIsAHashtag!')}") # False
    print(f" : {validate_hashtag('')}") # False

    print("\nCurrency Amount Validation:")
    print(f"$19.99: {validate_currency_amount('$19.99')}")      # True
    print(f"$1,234.56: {validate_currency_amount('$1,234.56')}")  # True
    print(f"$100: {validate_currency_amount('$100')}")        # True
    print(f"$0.01: {validate_currency_amount('$0.01')}")        # True
    print(f"$1000: {validate_currency_amount('$1000')}")      # True
    print(f"$10,000: {validate_currency_amount('$10,000')}")    # True
    print(f"19.99: {validate_currency_amount('19.99')}")        # False
    print(f"$19,99: {validate_currency_amount('$19,99')}")      # False
    print(f"$19.999: {validate_currency_amount('$19.999')}")    # False
    print(f" : {validate_currency_amount('')}") # False

