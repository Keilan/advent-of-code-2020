import sys

def check_passwords():
    input_lines = sys.stdin.read().splitlines()

    # Part 1
    valid_passwords = 0
    for line in input_lines:
        # Split input lines into data parts
        counts, letter, password = line.split(' ')
        min_count, max_count = [int(v) for v in counts.split('-')]
        letter = letter.strip(':') # Remove trailing ':'

        if min_count <= password.count(letter) <= max_count:
            valid_passwords += 1

    print(f'Part 1 - There are {valid_passwords} valid passwords.')

    # Part 2
    valid_passwords = 0
    for line in input_lines:
        # Split input lines into data parts
        counts, letter, password = line.split(' ')
        index1, index2 = [int(v) for v in counts.split('-')]
        letter = letter.strip(':') # Remove trailing ':'

        # The password is valid if they aren't both true or both false
        if (password[index1-1] == letter) != (password[index2-1] == letter):
            valid_passwords += 1

    print(f'Part 2 - There are {valid_passwords} valid passwords.')

if __name__ == '__main__':
    check_passwords()