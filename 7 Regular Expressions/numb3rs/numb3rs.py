import re  # Import the re module for regular expression operations

def main():
    print(validate(input("IPv4 Address: ")))  # Prompt the user for an IPv4 address and print whether it's valid

def validate(ip):
    # Use a regular expression to match valid IPv4 addresses
    if matches := re.search(r"^([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5])\.([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5])\.([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5])\.([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5])$", ip):
        return True  # Return True if the IP address matches the pattern
    else:
        return False  # Return False if the IP address does not match the pattern

if __name__ == "__main__":
    main()  # Call the main function to start the program
