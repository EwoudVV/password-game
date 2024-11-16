play_again = 1

def validate_rules(current_password):
    """Validate all password rules in sequence."""
    # Rule 1: Password must be at least 10 characters long
    if len(current_password) < 10:
        return "Your password must be at least 10 characters long."
    
    # Rule 2: Password must not contain any spaces
    if " " in current_password:
        return "Your password must not contain any spaces."
    
    # Rule 3: Password must contain at least 5 special characters
    special_chars = "!@#$%^&*()-_+=<>?/|{}[]~"
    special_count = sum(1 for char in current_password if char in special_chars)
    if special_count < 5:
        return "Your password must contain at least 5 special characters."
    
    # Rule 4: Password must contain at least 3 uppercase letters
    uppercase_count = sum(1 for char in current_password if char.isupper())
    if uppercase_count < 3:
        return "Your password must contain at least 3 uppercase letters."
    
    # Rule 5: Password must contain at least 3 digits
    digit_count = sum(1 for char in current_password if char.isdigit())
    if digit_count < 3:
        return "Your password must contain at least 3 digits."
    
    # Rule 6: Password must not contain consecutive repeated characters
    if any(current_password[i] == current_password[i + 1] for i in range(len(current_password) - 1)):
        return "Your password must not contain consecutive repeated characters."
    
    # Rule 7: Password must not contain any palindrome substring of length 3 or more
    def is_palindrome(s):
        return s == s[::-1]
    
    for i in range(len(current_password)):
        for j in range(i + 3, len(current_password) + 1):
            if is_palindrome(current_password[i:j]):
                return "Your password must not contain palindrome substrings of length 3 or more."
    
    # Rule 8: Password must start and end with a different character
    if current_password[0] == current_password[-1]:
        return "Your password must start and end with different characters."
    
    # If all rules pass
    return None

while play_again == 1:
    print("Welcome to the password game! Enter a password:")
    current_password = input()
    
    # Validate the password step by step
    rule_failed = validate_rules(current_password)
    while rule_failed:
        print(rule_failed)
        print("Please try again:")
        current_password = input()
        rule_failed = validate_rules(current_password)
    
    print("\nCongratulations! You have passed all levels!")
    print("Do you want to play again? Enter 1 for yes, or any other key to exit.")
    play_again = input()
    if play_again != "1":
        play_again = 0
        print("Thanks for playing!")
