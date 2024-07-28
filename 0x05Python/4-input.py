email = input("what\'s Your email ?").strip().lower()

name = email[0:email.index("@")].capitalize()

email_service = email[email.index("@") + 1:email.index(".")]

top_email = email[email.index(".") + 1:]

print(f"YOur Name Is {name}")

print(f"Your Email Service Is {email_service}")

print(f"Your Top Email Is {top_email}")

