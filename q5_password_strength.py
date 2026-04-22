import re
common_pwd=[
    "123456", "12345678", "password", "qwerty",
    "abc123", "111111", "123123", "admin"
    ]

def check_strength(password):
    score=0
    if len(password)>=8:
        score+=2
    if re.search(r"[A-Z]",password):
        score+=1
    if re.search(r"[a-z]",password):
        score+=1
    if re.search(r'[0-9]',password):
        score+=1
    if re.search(r"[!@#$%^&*(),.?\:{}|<>]",password):
        score+=1
    if password.lower() in common_pwd:
        score-=3
    if re.search(r"(.)\1\1",password):    #repeated characters
        score-=2

    sequences=["1234", "abcd", "qwerty"]
    for seq in sequences:
        if seq in password.lower():
            score-=2

    if score<=2:
        strength="Weak"
    elif score<=5:
        strength="Medium"
    else:
        strength="Strong"

    return score, strength

test_passwords=["1234", "password", "Admin123", "P@ssword", "Sohail@2025", "11111111",
                "88888888"]

for pwd in test_passwords:
    scr, strg=check_strength(pwd)
    print(f"Password: {pwd}\tScore: {scr}\tStrength: {strg}\n")