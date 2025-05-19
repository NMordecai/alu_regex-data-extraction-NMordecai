#!/usr/bin/env python3
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



def validate_email(email):
    """
    Validates email addresses.
    - user@example.com
    - firstname.lastname@company.co.uk
    Args:
        email (str): The email address string to validate.
    Returns:
        bool: True if the email address is valid, False otherwise.
    """
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    # ^ - start of string
    # [a-zA-Z0-9._%+-]+ - One or more alphanumeric characters, dots, underscores, percent signs, plus or minus signs
    # @ - literal '@'
    # [a-zA-Z0-9.-]+ - One or more alphanumeric characters, dots, or hyphens
    # \. - literal '.'
    # [a-zA-Z]{2,} - Two or more letters
    # $ - end of string
    if not email:
        return False
    return bool(re.match(pattern, email))


def validate_time(time_str):
    """
    Validates time in 12-hour and 24-hour formats.
    - 14:30 (24-hour format)
    - 2:30 PM (12-hour format)
    Args:
        time_str (str): The time string to validate.
    Returns:
        bool: True if the time string is valid, False otherwise.
    """
    pattern_24h = r"^([01]\d|2[0-3]):[0-5]\d$"  # 24-hour format
    pattern_12h = r"^(0?[1-9]|1[0-2]):[0-5]\d\s(AM|PM)$"  # 12-hour format
    if not time_str:
        return False
    return bool(re.match(pattern_24h, time_str) or re.match(pattern_12h, time_str))



def validate_url(url):
    """
    Validates URLs.
    - https://www.example.com
    - https://subdomain.example.org/page
    Args:
        url (str): The URL string to validate.
    Returns:
        bool: True if the URL is valid, False otherwise.
    """
    pattern = r"^(https?://)([a-zA-Z0-9.-]+)(\.[a-zA-Z]{2,})(/[\w.-]+)*$"
    # ^ - start of string
    # (https?://) - Matches "http://" or "https://"
    # ([a-zA-Z0-9.-]+) - Matches the domain name (e.g., www.example.com)
    # (\.[a-zA-Z]{2,}) - Matches the top-level domain (e.g., .com, .org)
    # (/[\w.-]+)* - Optionally matches any number of subpages
    # $ - end of string
    if not url:
        return False
    return bool(re.match(pattern, url))

def validate_html_tag(html_string):
    """
    Validates basic HTML tags.  This is a simplified check.
    - <p>
    - <div class="example">
    - <img src="image.jpg" alt="description">
    Args:
        html_string (str): The HTML string to validate.
    Returns:
        bool: True if the HTML string is valid, False otherwise.
    """
    pattern = r"^<([a-zA-Z0-9]+)(?:\s[a-zA-Z0-9\-]+(?:=\"[^\"]*\")?)*>\s*(.*?)\s*<\/\1>$|^<([a-zA-Z0-9]+)(?:\s[a-zA-Z0-9\-]+(?:=\"[^\"]*\")?)*\/>$"
    # ^ - start of string
    # < - literal '<'
    # ([a-zA-Z0-9]+) - Tag name (e.g., p, div, img) - Capturing group 1
    # (?:\s[a-zA-Z0-9\-]+(?:="[^"]*")?)* - Optional attributes (e.g., class="example", src="image.jpg")
    # > - literal '>'
    # \s* - Optional whitespace
    # (.*?) - Any content (non-greedy) - Capturing group 2
    # \s* - Optional whitespace
    # <\/ - literal '</'
    # \1 - Backreference to the tag name captured in group 1 (closing tag)
    # > - literal '>'
    # | - OR
    # ^ - start of string
    # < - literal '<'
    # ([a-zA-Z0-9]+) - Tag name  (e.g., img) - Capturing group 3
    #  (?:\s[a-zA-Z0-9\-]+(?:="[^"]*")?)* - Optional attributes
    # /> - literal '/>' (for self-closing tags)
    # $ - end of string

    if not html_string:
        return False
    return bool(re.match(pattern, html_string))


if __name__ == "__main__":
    # Test cases
    print("Phone Number Validation:")
    print(f"(123) 456-7890: {validate_phone_number('(123) 456-7890')}")
    print(f"123-456-7890: {validate_phone_number('123-456-7890')}")
    print(f"123.456.7890: {validate_phone_number('123.456.7890')}")
    print(f"1234567890: {validate_phone_number('1234567890')}")
    print(f"12-34-5678: {validate_phone_number('12-34-5678')}")
    print(f"abc-def-ghij: {validate_phone_number('abc-def-ghij')}")
    print(f"(123)456-7890: {validate_phone_number('(123)456-7890')}")
    print(f" : {validate_phone_number('')}")

    print("\nCredit Card Number Validation:")
    print(f"1234 5678 9012 3456: {validate_credit_card_number('1234 5678 9012 3456')}")
    print(f"1234-5678-9012-3456: {validate_credit_card_number('1234-5678-9012-3456')}")
    print(f"1234567890123456: {validate_credit_card_number('1234567890123456')}")
    print(f"1234 5678 9012: {validate_credit_card_number('1234 5678 9012')}")
    print(f"1234-5678-9012: {validate_credit_card_number('1234-5678-9012')}")
    print(f"123456789012345: {validate_credit_card_number('123456789012345')}")
    print(f"1234 abcdef 9012 3456: {validate_credit_card_number('1234 abcdef 9012 3456')}")
    print(f" : {validate_credit_card_number('')}")

    print("\nHashtag Validation:")
    print(f"#example: {validate_hashtag('#example')}")
    print(f"#ThisIsAHashtag: {validate_hashtag('#ThisIsAHashtag')}")
    print(f"#123: {validate_hashtag('#123')}")
    print(f"#_underscore: {validate_hashtag('#_underscore')}")
    print(f"example: {validate_hashtag('example')}")
    print(f"#: {validate_hashtag('#')}")
    print(f"#ThisIsAHashtag!: {validate_hashtag('#ThisIsAHashtag!')}")
    print(f" : {validate_hashtag('')}")

    print("\nCurrency Amount Validation:")
    print(f"$19.99: {validate_currency_amount('$19.99')}")
    print(f"$1,234.56: {validate_currency_amount('$1,234.56')}")
    print(f"$100: {validate_currency_amount('$100')}")
    print(f"$0.01: {validate_currency_amount('$0.01')}")
    print(f"$1000: {validate_currency_amount('$1000')}")
    print(f"$10,000: {validate_currency_amount('$10,000')}")
    print(f"19.99: {validate_currency_amount('19.99')}")
    print(f"$19,99: {validate_currency_amount('$19,99')}")
    print(f"$19.999: {validate_currency_amount('$19.999')}")
    print(f" : {validate_currency_amount('')}")

    print("\nEmail Validation:")
    print(f"user@example.com: {validate_email('user@example.com')}")
    print(f"firstname.lastname@company.co.uk: {validate_email('firstname.lastname@company.co.uk')}")
    print(f"invalid_email: {validate_email('invalid_email')}")
    print(f"missing@dotcom: {validate_email('missing@dotcom')}")
    print(f" : {validate_email('')}")

    print("\nTime Validation:")
    print(f"14:30: {validate_time('14:30')}")
    print(f"2:30 PM: {validate_time('2:30 PM')}")
    print(f"02:30 PM: {validate_time('02:30 PM')}")
    print(f"14:60: {validate_time('14:60')}")
    print(f"2:30AM: {validate_time('2:30AM')}")
    print(f"2:30: {validate_time('2:30')}")
    print(f"24:00: {validate_time('24:00')}")
    print(f"00:00: {validate_time('00:00')}")
    print(f" : {validate_time('')}")

    print("\nURL Validation:")
    print(f"https://www.example.com: {validate_url('https://www.example.com')}")
    print(f"https://subdomain.example.org/page: {validate_url('https://subdomain.example.org/page')}")
    print(f"http://example.com: {validate_url('http://example.com')}")
    print(f"invalid-url: {validate_url('invalid-url')}")
    print(f"https://example: {validate_url('https://example')}")
    print(f" : {validate_url('')}")

