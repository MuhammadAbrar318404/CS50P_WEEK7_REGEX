import re

def main():
    print(count(input("Text: ")))


def count(text):
    # Regular expression to find "um" as a standalone word, case-insensitively
    pattern = r'\bum\b'
    matches = re.findall(pattern, text, re.IGNORECASE)
    return len(matches)

if __name__ == "__main__":
    main()
