# This is Amirhossein Jahazi AKA combat47
file = open(input())
lines = 1
for line in file:
    code = "S001"
    if len(line) > 79:
        print(f"Line {lines}: {code} Too long")
    lines += 1
file.close()
