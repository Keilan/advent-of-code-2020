import sys


def is_valid(passport):
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for field in required_fields:
        if field not in passport:
            return False
    
    # Check specific rules now that we know all fields are present
    birth_year = int(passport['byr'])
    if birth_year < 1920 or birth_year > 2002:
        return False

    issue_year = int(passport['iyr'])
    if issue_year < 2010 or issue_year > 2020:
        return False

    expiration_year = int(passport['eyr'])
    if expiration_year < 2020 or expiration_year > 2030:
        return False

    height = passport['hgt']
    if 'cm' in height:
        value = int(height.replace('cm', ''))
        if value < 150 or value > 193:
            return False
    elif 'in' in height:
        value = int(height.replace('in', ''))
        if value < 59 or value > 76:
            return False
    else:
        return False

    hair = passport['hcl']
    if hair[0] != '#' or len(hair) != 7:
        return False
    if any([value not in '0123456789abcdef' for value in hair[1:]]):
        return False

    eye = passport['ecl']
    if eye not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False
    
    pid = passport['pid']
    if len(pid) != 9:
        return False
    
    # If we made it here, all required fields are present
    return True


def main():
    # Read passport fields into a dictionary, calling the processing function
    # when we reach a blank line, indicating that the passport is finished
    valid_count = 0
    passport = {}
    for line in sys.stdin.read().splitlines():
        if line != '':
            for item in line.split(' '):
                k, v = item.split(':')
                passport[k] = v

        # Blank line, process passport
        else:
            valid_count += is_valid(passport)
            passport = {}
    
    # Final passport doesn't end with a blank line
    valid_count += is_valid(passport)

    print(f'There are {valid_count} valid passwords.')


if __name__ == '__main__':
    main()
