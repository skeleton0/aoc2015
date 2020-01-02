code_len = 0
memory_len = 0

with open('input.txt') as f:
    for line in f:
        strlen = len(line.strip())
        code_len += strlen

        pos = 1 
        while pos < strlen - 1:
            if line[pos] == '\\':
                if line[pos + 1] == 'x':
                    pos += 4
                else:
                    pos += 2
            else:
                pos += 1

            memory_len += 1

print(code_len - memory_len)
