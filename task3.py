def password_strength(password):
    score = 0
    
    if len(password) >= 8:
        score += 1
    
    if any(char.isupper() for char in password) and any(char.islower() for char in password):
        score += 1
    
    if any(char.isdigit() for char in password):
        score += 1
    
    if any(char in r"!@#$%^&*()-_=+[]{}|;:',.<>?`~" for char in password):
        score += 1
    
    if score == 4:
        score += 1
    
    if score == 0:
        return "Very Weak"
    elif score == 1:
        return "Weak"
    elif score == 2:
        return "Moderate"
    elif score == 3:
        return "Strong"
    elif score >= 4:
        return "Very Strong"

user_password = input("Enter a password to check its strength: ")

strength = password_strength(user_password)
password_length = len(user_password)

print(f"The strength of your password is: {strength}")
print(f"The length of your password is: {password_length}")
