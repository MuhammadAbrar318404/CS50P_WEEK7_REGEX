from response import validate_email

def test_valid_emails():
    assert validate_email("malan@harvard.edu") == "Valid"
    assert validate_email("youremail@example.com") == "Valid"  # Replace with your actual email

def test_invalid_emails():
    assert validate_email("malan@@@harvard.edu") == "Invalid"
    assert validate_email("youremail..example@example.com") == "Invalid"  # Replace with your own email mistyped
    assert validate_email("plainaddress") == "Invalid"
    assert validate_email("missingatsign.com") == "Invalid"
    assert validate_email("missing.domain@com") == "Invalid"
    assert validate_email("missing@dotcom") == "Invalid"
