# ============================================================
# PYTHON STRINGS ASSIGNMENT
# Student name: Rodriguez Reyes Juan Manuel
# Student ID: 2630321
# Group: IM 1-1
# File name: 2630321_JuanRodriguez__t_strings.py
# ============================================================

# EXECUTIVE SUMMARY
# A string is a sequence of characters used to store text in Python
# Strings are immutable, which means their characters cannot be changed directly
# Python provides operations to join strings, measure their length, and extract slices
# It also provides methods to search for text, replace parts, split sentences, and format output
# Input validation helps prevent empty or incorrectly formatted data from being processed
# Normalizing text with strip() and lower() makes comparisons more consistent
# This file presents six string problems with descriptions, inputs, outputs, and validations
# Each problem includes normal, border, and error test cases documented in comments
# The code demonstrates common string methods and basic input validation

# PRINCIPLES AND GOOD PRACTICES
# - Strings are immutable; string methods return a new string instead of changing the original
# - Use strip() and lower() to normalize input before comparing it
# - Use named constants instead of unexplained numeric values when practical
# - Document what a slice extracts, especially when using indexes
# - Prefer built-in string methods instead of rewriting basic text operations
# - Validate that input is not empty before checking its format
# - Use clear variable names and understandable error messages

# ============================================================
# Problem 1: Full name formatter
# Description:
# Normalize a full name, remove extra spaces, and display it in
# title case. Create initials from each name part.
#
# Inputs:
# - full_name: a person's full name as a string.
#
# Outputs:
# - Formatted name and initials.
#
# Validations:
# - The name cannot be empty after strip().
# - At least two words must be provided.
#
# Test cases:
# 1) Normal: "  JUAN   carlos tovar " -> "Juan Carlos Tovar", "J.C.T."
# 2) Border: "Ana Ruiz" -> "Ana Ruiz", "A.R."
# 3) Error: "     " -> "Error: invalid input"
# ============================================================

def problem_1():
    full_name = input("Enter full name: ")
    cleaned_name = " ".join(full_name.strip().split())

    if not cleaned_name:
        print("Error: invalid input")
        return

    name_parts = cleaned_name.split()

    if len(name_parts) < 2:
        print("Error: enter at least two words")
        return

    formatted_name = cleaned_name.title()
    initials = ".".join(part[0].upper() for part in name_parts) + "."

    print(f"Formatted name: {formatted_name}")
    print(f"Initials: {initials}")


# ============================================================
# Problem 2: Simple email validator
# Description:
# Check a basic email structure. A valid email must contain
# exactly one '@', a dot after '@', and no whitespace.
#
# Inputs:
# - email_text: an email address as a string.
#
# Outputs:
# - Whether the email is valid and, if valid, its domain.
#
# Validations:
# - The input cannot be empty.
# - Exactly one '@' must exist.
# - No whitespace is allowed.
# - The local part and domain must not be empty.
# - The domain must contain a dot that is not its first or last character.
#
# Test cases:
# 1) Normal: "student@example.com" -> valid, domain "example.com"
# 2) Border: "a@b.co" -> valid, domain "b.co"
# 3) Error: "student example.com" -> invalid
# ============================================================

def problem_2():
    email_text = input("Enter email: ").strip()

    if not email_text:
        print("Error: invalid input")
        print("Valid email: false")
        return

    is_valid = True

    if email_text.count("@") != 1:
        is_valid = False
    elif any(character.isspace() for character in email_text):
        is_valid = False
    else:
        at_position = email_text.find("@")
        local_part = email_text[:at_position]
        domain_part = email_text[at_position + 1:]
        dot_position = domain_part.find(".")

        if not local_part or not domain_part:
            is_valid = False
        elif dot_position <= 0 or dot_position == len(domain_part) - 1:
            is_valid = False

    print(f"Valid email: {str(is_valid).lower()}")

    if is_valid:
        print(f"Domain: {domain_part}")


# ============================================================
# Problem 3: Palindrome checker
# Description:
# Determine whether a phrase reads the same forward and backward.
# Spaces and letter case are ignored.
#
# Inputs:
# - phrase: a phrase as a string.
#
# Outputs:
# - Whether the phrase is a palindrome.
#
# Validations:
# - The input cannot be empty after strip().
# - At least three characters must remain after removing spaces.
#
# Test cases:
# 1) Normal: "Anita lava la tina" -> true
# 2) Border: "a b a" -> true
# 3) Error: "  " -> invalid input
# ============================================================

def problem_3():
    phrase = input("Enter a phrase: ").strip()

    if not phrase:
        print("Error: invalid input")
        return

    normalized_phrase = phrase.lower().replace(" ", "")

    if len(normalized_phrase) < 3:
        print("Error: enter at least three non-space characters")
        return

    reversed_phrase = normalized_phrase[::-1]  # Reverse the normalized phrase.
    is_palindrome = normalized_phrase == reversed_phrase

    print(f"Normalized phrase: {normalized_phrase}")
    print(f"Is palindrome: {str(is_palindrome).lower()}")


# ============================================================
# Problem 4: Sentence word stats
# Description:
# Split a sentence into words and report the word count, first
# and last words, and shortest and longest words.
#
# Inputs:
# - sentence: a sentence as a string.
#
# Outputs:
# - Word count, first word, last word, shortest word, longest word.
#
# Validations:
# - The sentence cannot be empty after strip().
# - At least one word must remain after split().
#
# Test cases:
# 1) Normal: "Python makes useful tools" -> 4 words; shortest "tools"
#    (shortest and longest are selected by length; ties use first occurrence)
# 2) Border: "Hi" -> 1 word; first and last are "Hi"
# 3) Error: "   " -> invalid input
# ============================================================

def problem_4():
    sentence = input("Enter a sentence: ").strip()

    if not sentence:
        print("Error: invalid input")
        return

    words = sentence.split()

    if not words:
        print("Error: no valid words found")
        return

    shortest_word = min(words, key=len)
    longest_word = max(words, key=len)

    print(f"Word count: {len(words)}")
    print(f"First word: {words[0]}")
    print(f"Last word: {words[-1]}")
    print(f"Shortest word: {shortest_word}")
    print(f"Longest word: {longest_word}")


# ============================================================
# Problem 5: Password strength classifier
# Description:
# Classify a password as weak, medium, or strong using length
# and character-type rules.
#
# Inputs:
# - password_input: a password as a string.
#
# Outputs:
# - Password strength: weak, medium, or strong.
#
# Validations:
# - The password cannot be empty.
# - Length and character types are checked.
#
# Rules:
# - Weak: fewer than 8 characters.
# - Strong: at least 8 characters and includes uppercase, lowercase,
#   a digit, and a non-alphanumeric symbol.
# - Medium: at least 8 characters but does not meet every strong rule.
#
# Test cases:
# 1) Normal: "Robot2026!" -> strong
# 2) Border: "abc12345" -> medium
# 3) Error: "" -> invalid input
# ============================================================

def problem_5():
    password_input = input("Enter password: ")

    if not password_input:
        print("Error: invalid input")
        return

    has_upper = any(character.isupper() for character in password_input)
    has_lower = any(character.islower() for character in password_input)
    has_digit = any(character.isdigit() for character in password_input)
    has_symbol = any(not character.isalnum() for character in password_input)

    if len(password_input) < 8:
        strength = "weak"
    elif has_upper and has_lower and has_digit and has_symbol:
        strength = "strong"
    else:
        strength = "medium"

    print(f"Password strength: {strength}")


# ============================================================
# Problem 6: Product label formatter
# Description:
# Create a product label containing a product name and a positive
# price. The final label is exactly 30 characters long.
#
# Inputs:
# - product_name: a non-empty product name.
# - price_value: a positive numeric price.
#
# Outputs:
# - A label exactly 30 characters long, padded or truncated as needed.
#
# Validations:
# - The product name cannot be empty after strip().
# - The price must be numeric and greater than zero.
#
# Test cases:
# 1) Normal: product "Notebook", price "25.50" -> 30-character label
# 2) Border: product "A", price "0.01" -> 30-character label
# 3) Error: product "Pen", price "zero" -> invalid price
# ============================================================

LABEL_WIDTH = 30

def problem_6():
    product_name = input("Enter product name: ").strip()
    price_text = input("Enter product price: ").strip()

    if not product_name:
        print("Error: invalid product name")
        return

    try:
        price_value = float(price_text)
    except ValueError:
        print("Error: invalid price")
        return

    if price_value <= 0:
        print("Error: price must be positive")
        return

    label_base = f"Product: {product_name.upper()} | Price: ${price_value:.2f}"
    label = label_base[:LABEL_WIDTH].ljust(LABEL_WIDTH)

    print(f'Label: "{label}"')
    print(f"Length: {len(label)}")


# ============================================================
# MAIN MENU
# Choose one problem to run. Enter 0 to exit.
# ============================================================

def main():
    while True:
        print("\n=== STRING PRACTICE MENU ===")
        print("1. Full name formatter")
        print("2. Simple email validator")
        print("3. Palindrome checker")
        print("4. Sentence word stats")
        print("5. Password strength classifier")
        print("6. Product label formatter")
        print("0. Exit")

        choice = input("Choose a problem (0-6): ").strip()

        if choice == "1":
            problem_1()
        elif choice == "2":
            problem_2()
        elif choice == "3":
            problem_3()
        elif choice == "4":
            problem_4()
        elif choice == "5":
            problem_5()
        elif choice == "6":
            problem_6()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Error: invalid input")


# CONCLUSIONS
# Strings are important for receiving, processing, and displaying text.
# strip() removes extra spaces at the beginning and end of input.
# lower() helps compare text without being affected by letter case.
# split() separates text into words, while join() combines words with a separator.
# Input validation prevents empty values and common format errors.
# String immutability means methods create new strings instead of editing the original.
# Slicing is useful for extracting or reversing text and limiting a label's length.

# REFERENCES
# 1) Python Software Foundation. Built-in Types: Text Sequence Type — str.
#    https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
# 2) Python Software Foundation. Built-in Functions.
#    https://docs.python.org/3/library/functions.html
# 3) Python Software Foundation. Errors and Exceptions.
#    https://docs.python.org/3/tutorial/errors.html
# 4) Python Software Foundation. More on Defining Functions.
#    https://docs.python.org/3/tutorial/controlflow.html#defining-functions
# 5) Python Software Foundation. An Informal Introduction to Python.
#    https://docs.python.org/3/tutorial/introduction.html

if __name__ == "__main__":
    main()
