# This is Amirhossein Jahazi AKA combat47
import re


def main():
    preceding_blank_line_counter: int = 0

    with open(input()) as f:
        for i, line in enumerate(f, start=1):
            if line == "\n":
                preceding_blank_line_counter += 1
                continue

            if len(line) > 79:
                print(f"Line {i}:", "S001 Too long")

            if re.match(r"(?!^( {4})*[^ ])", line):
                print(f"Line {i}:", "S002 Indentation is not a multiple of four")

            if re.search(r"^([^#])*;(?!\S)", line):
                print(f"Line {i}:", "S003 Unnecessary semicolon")

            if re.match(r"[^#]*[^ ]( ?#)", line):
                print(f"Line {i}:", "S004 At least two spaces before inline comment required")

            if re.search(r"(?i)# *todo", line):
                print(f"Line {i}:", "S005 TODO found")

            if preceding_blank_line_counter > 2:
                print(f"Line {i}:", "S006 More than two blank lines used before this line")
                preceding_blank_line_counter = 0


if __name__ == "__main__":
    main()