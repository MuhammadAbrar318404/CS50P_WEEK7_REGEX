import re
import sys

def main():
    print(convert(input("Hours: ").strip()))  # Prompt user for input and print the converted time

def convert(s):
    # Match the input string with the specified pattern
    if match := re.search(r"^([0-9]?[0-2]?:?[0-5]?[0-9]?)\s(AM|PM)\sto\s([0-9]?[0-2]?:?[0-5]?[0-9]?)\s(PM|AM)$", s):
        if ":" in match.group(1) or ":" in match.group(3):  # Check if the input contains minutes
            starth, startm = match.group(1).split(":")  # Split start time into hours and minutes
            endh, endm = match.group(3).split(":")  # Split end time into hours and minutes
            starth, endh, endm, startm = int(starth), int(endh), int(endm), int(startm)  # Convert to integers
        else:
            starth = match.group(1)  # Get start hour
            endh = match.group(3)  # Get end hour
            starth, endh, endm, startm = int(starth), int(endh), 0, 0  # Default minutes to 0

        # Convert AM/PM to 24-hour format for start and end times
        if match.group(2) == "AM" and match.group(4) == "AM":
            if starth == 12 and endh != 12:
                starth = 0  # Midnight case for start time
            elif endh == 12 and starth != 12:
                endh = 0  # Midnight case for end time
            elif endh == 12 and starth == 12:
                starth = 0
                endh += 12
        elif match.group(2) == "AM" and match.group(4) == "PM":
            if starth == 12 and endh != 12:
                starth = 0  # Midnight case for start time
                endh += 12  # PM case for end time
            elif starth == 12 and endh == 12:
                starth = 0
            elif starth != 12 and endh == 12:
                starth = starth  # No change needed
            else:
                endh += 12  # PM case for end time
        elif match.group(2) == "PM" and match.group(4) == "AM":
            if starth != 12 and endh == 12:
                starth += 12  # PM case for start time
                endh = 0  # Midnight case for end time
            elif starth == 12 and endh == 12:
                endh = 0  # Midnight case for end time
            elif starth == 12 and endh != 12:
                starth = starth  # No change needed
            else:
                starth += 12  # PM case for start time
        else:
            if starth == 12 and endh == 12:
                starth = starth  # No change needed
            elif starth != 12 and endh == 12:
                starth += 12  # PM case for start time
            elif starth == 12 and endh != 12:
                endh += 12  # PM case for end time
            else:
                starth += 12  # PM case for start time
                endh += 12  # PM case for end time

        # Format and return the converted time range
        return f"{starth:02}:{startm:02} to {endh:02}:{endm:02}"
    else:
        raise ValueError()  # Raise an error if the input format is invalid

if __name__ == "__main__":
    main()
