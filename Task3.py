import re

def check_password_strength(password):
    strength = 0
    criteria = [
        (len(password) >= 8, "At least 8 characters"),
        (re.search(r"[a-z]", password), "Lowercase letter"),
        (re.search(r"[A-Z]", password), "Uppercase letter"),
        (re.search(r"\d", password), "Number"),
        (re.search(r"[!@#$%^&*(),.?\":{}|<>]", password), "Special character"),
    ]
    
    passed_criteria = [desc for condition, desc in criteria if condition]
    strength = len(passed_criteria)
    
    if strength == 5:
        rating = "Very Strong"
    elif strength == 4:
        rating = "Strong"
    elif strength == 3:
        rating = "Moderate"
    elif strength == 2:
        rating = "Weak"
    else:
        rating = "Very Weak"
    
    return rating, passed_criteria

if __name__ == "__main__":
    password = input("Enter a password to check its strength: ")
    rating, criteria_met = check_password_strength(password)
    
    print(f"Password Strength: {rating}")
    print("Criteria met:")
    for criteria in criteria_met:
        print(f"- {criteria}")
