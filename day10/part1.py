sequence = '3113322113'

for i in range(40):
    next_sequence = ''
    char = sequence[0]
    char_count = 1
    for c in sequence[1:]:
        if c == char:
            char_count += 1
        else:
            next_sequence += str(char_count) + char
            char = c
            char_count = 1
            
    next_sequence += str(char_count) + char
    sequence = next_sequence

print(len(sequence))
