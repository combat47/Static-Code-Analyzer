# This is Amirhossein Jahazi AKA combat47
import argparse
import re
import os


def input_path() -> str:
    parser = argparse.ArgumentParser(usage="Static Code Analyzer")
    parser.add_argument("files", help="takes a single file or folder path")
    args = parser.parse_args()
    return args.files


def analyze_pathname(pathname: str):
    if os.path.isfile(pathname):
        return analyze_file(pathname)

    if os.path.isdir(pathname):
        scripts: list = os.listdir(pathname)
        for script in scripts:
            script_path: str = os.path.join(pathname, script)
            analyze_file(script_path)


def analyze_file(filename: str):
    preceding_blank_line_counter: int = 0

    with open(filename) as f:
        for i, line in enumerate(f, start=1):
            if line == "\n":
                preceding_blank_line_counter += 1
                continue

            error_source: str = f"{filename}: Line {i}:"

            if len(line) > 79:
                print(error_source, "S001 Too long")

            if re.match(r"(?!^( {4})*[^ ])", line):
                print(error_source, "S002 Indentation is not a multiple of four")

            if re.search(r"^([^#])*;(?!\S)", line):
                print(error_source, "S003 Unnecessary semicolon")

            if re.match(r"[^#]*[^ ]( ?#)", line):
                print(error_source, "S004 At least two spaces before inline comment required")

            if re.search(r"(?i)# *todo", line):
                print(error_source, "S005 TODO found")

            if preceding_blank_line_counter > 2:
                print(error_source, "S006 More than two blank lines used before this line")
            preceding_blank_line_counter = 0

            if re.match(r"^( *(?:class|def) ( )+)", line):
                print(error_source, "S007 Too many spaces after construction_name (def or class)")

            if matches := re.match(r"^ *class (?P<name>\w+)", line):
                if not re.match(r"(?:[A-Z][a-z0-9]+)+", matches["name"]):
                    print(error_source, f'S008 Class name {matches["name"]} should use CamelCase')

            if matches := re.match(r"^ *def (?P<name>\w+)", line):
                if not re.match(r"[a-z_]+", matches["name"]):
                    print(error_source, f'S009 Function name {matches["name"]} should use snake_case')


def main():
    analyze_pathname(input_path())


if __name__ == "__main__":
    main()
