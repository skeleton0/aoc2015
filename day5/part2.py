def has_duplicate_pair(string):
    for first_char in range(len(string) - 2):
        if string.count(string[first_char:first_char + 2]) >= 2:
            return True

    return False

def has_sandwhich(string):
    for first_char in range(len(string) - 3):
        if string[first_char] == string[first_char + 2]:
            return True

    return False

nice_strings = 0
with open('input.txt') as input_file:
    for string in input_file:
        if has_duplicate_pair(string) and has_sandwhich(string):
            nice_strings += 1

print('Nice strings:', nice_strings)
