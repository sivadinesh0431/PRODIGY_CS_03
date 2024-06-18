import re

def password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Password should include at least one uppercase letter.")

    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Password should include at least one lowercase letter.")

    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("Password should include at least one number.")

    if re.search(r'[@$!%*?&#]', password):
        score += 1
    else:
        feedback.append("Password should include at least one special character (@, $, !, %, *, ?, &, #).")

    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Medium"
    elif score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    return strength, feedback

def main():
    print("Password Strength Assessment Tool")
    password = input("Enter a password to assess: ")
    strength, feedback = password_strength(password)

    print(f"Password Strength: {strength}")
    if feedback:
        print("Feedback:")
        for item in feedback:
            print(f"- {item}")

if __name__ == "__main__":
    main()
