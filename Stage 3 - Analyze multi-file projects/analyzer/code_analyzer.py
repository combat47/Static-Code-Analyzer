# This is Amirhossein Jahazi AKA combat47
import argparse
import os
import re


def print_pep8_error(filename, line_number, code):
    errors = {'S001': 'Too long',
              'S002': 'Indentation is not a multiple of four',
              'S003': 'Unnecessary semicolon',
              'S004': 'Less than two spaces before inline comments',
              'S005': 'TODO found',
              'S006': 'More than two blank lines preceding a code line'}

    print(f'{filename}: Line {line_number}: {code} {errors[code]}')


def check_errors(filename, lines):
    blank_lines = 0
    for i, line in enumerate(lines, start=1):
        if line == '\n':
            blank_lines += 1
            continue
        if len(line) > 79:
            print_pep8_error(filename, i, 'S001')
        if (len(line) - len(line.lstrip(' '))) % 4 != 0:
            print_pep8_error(filename, i, 'S002')
        if ';' in line and re.search(r'[\'"].*;.*[\'"]|#.*;', line) is None:
            print_pep8_error(filename, i, 'S003')
        if '#' in line and re.search(r'^#| {2,}#', line) is None:
            print_pep8_error(filename, i, 'S004')
        if 'todo' in line.lower() and re.search(r'#.*todo', line.lower()) is not None:
            print_pep8_error(filename, i, 'S005')
        if blank_lines > 2:
            print_pep8_error(filename, i, 'S006')
        blank_lines = 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('path')
    path = parser.parse_args().path

    if path.endswith('.py'):
        paths = [path]
    else:
        paths = [f'{path}\\{filename}' for filename in os.listdir(path) if filename.endswith('.py')]

    for file in paths:
        with open(file, 'r', encoding='utf-8') as f:
            check_errors(file, f.readlines())
