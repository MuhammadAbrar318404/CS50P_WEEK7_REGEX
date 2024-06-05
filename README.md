# CS50P_WEEK7_REGEX
This is week7 of the CS50P which was about the regular expression and re library, this repo contains the project files that i have designed to implement the theoretical knowledge. The projects covered various topics such as validating input formats, parsing HTML content, converting time formats, and counting occurrences of specific words. Let's explore each project:

---

#### 1. IPv4 Address Validation

In `numb3rs.py`, I implemented a script to validate whether a given input string represents a valid IPv4 address. The script utilizes regular expressions to match valid IPv4 addresses and returns `True` if the address is valid, and `False` otherwise.

---

#### 2. YouTube URL Parser

The `watch.py` script parses HTML content to extract YouTube video URLs and converts them into shorter, shareable youtu.be URLs. It uses regular expressions to identify the YouTube video URL within the HTML code and transforms it into the desired format.

---

#### 3. 12-hour to 24-hour Time Converter

`working.py` converts time ranges specified in 12-hour format to 24-hour format. The script handles various input formats and validates the input before performing the conversion. It utilizes regular expressions to parse the input time range and applies logic to convert it into the desired format.

---

#### 4. Word Occurrence Counter

The `um.py` script counts the occurrences of the word "um" in a given text line. It searches for the word "um" as a standalone word using regular expressions and returns the total count of occurrences, case-insensitively.

---

#### 5. Email Address Validation

In `response.py`, I implemented a program to validate the syntactical validity of email addresses provided by the user. The script utilizes the `validators` library to check whether the input email address is valid and prints either "Valid" or "Invalid" based on the validation result.

---

These projects demonstrate proficiency in handling various types of input data, performing data validation, and manipulating text and HTML content effectively using Python. Each project addresses a specific task and contributes to a deeper understanding of Python programming concepts and techniques.
