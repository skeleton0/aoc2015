def vowel_count(string):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    count = 0
    for char in string:
        if char in vowels:
            count += 1

    return count

def has_immediate_repitition(string):
    prev_char = '0'
    for char in string:
        if char == prev_char:
            return True
        else:
            prev_char = char

    return False

def has_bad_substring(string):
    return 'ab' in string or 'cd' in string or 'pq' in string or 'xy' in string

nice_strings = 0
with open('input.txt') as input_file:
    for string in input_file:
        if (vowel_count(string) >= 3 and 
           has_immediate_repitition(string) and 
           not has_bad_substring(string)):
               nice_strings += 1

print('Nice strings:', nice_strings)
