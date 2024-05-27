import validators

def main():
    # Prompt the user for an email address
    email = input("Email: ").strip()
    print(validate_email(email))


def validate_email(email):
    # Use the validators library to check if the email address is valid
    email= validators.email(email)
    # Validate the email address and print the appropriate result
    if email:
        return "Valid"
    else:
        return "Invalid"
if __name__ == "__main__":
    main()
