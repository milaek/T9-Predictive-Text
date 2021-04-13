# View helper code attribuition in ReadMe

import re
import sys

def ask_for_numbers():
    while True:
        response = input('What numbers have you pressed? ').strip()
        if len(response) < 3:
            print('You need to enter at least three numbers.', file=sys.stderr)
        elif re.search("[^2-9]", response):
            print("You entered a character that isn't one of 2, 3, 4, 5, 6, 7, 8, or 9. Please try again.", file=sys.stderr)
        else:
            return response


def read_content(filename='words.txt'):
    with open(filename, 'r') as f:
        return f.read().strip().replace(',', ' ')
