from numb3rs import validate  # Import the validate function from the numb3rs module

def test_valid_values():
    # Test with valid IPv4 addresses
    assert validate("255.255.255.255") == True
    assert validate("1.2.3.10") == True

def test_invalid_values():
    # Test with invalid IPv4 addresses
    assert validate("256.255.255.255") == False  # Invalid because 256 is out of the range 0-255
    assert validate("255.256.255.255") == False  # Invalid because 256 is out of the range 0-255
    assert validate("1.2.3.1000") == False  # Invalid because 1000 is out of the range 0-255
