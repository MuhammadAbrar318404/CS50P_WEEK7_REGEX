import re
def main():
    print(parse(input("HTML: ").strip()))
def parse(s):
    if matches:= re.search(r"^<iframe.*src=\"((?:http|https)://w*\.?youtube\.com/.+/[^\"]+)\".*></iframe>$",s):
        matches=matches.group(1).replace("youtube.com/embed","youtu.be")
        if  "www." in matches:
            matches=matches.replace("www.","")
        elif "https" not in matches:
            matches=matches.replace("http","https")
        return matches
    else:
        return None

if __name__ == "__main__":
    main()
