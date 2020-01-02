code_len = 0
memory_len = 0

with open('input.txt') as f:
    for line in f:
        strlen = len(line.strip())
        memory_len += strlen
        code_len += strlen + 4

        pos = 1
        while pos < strlen - 1:
            if line[pos] == '\\':
                if line[pos + 1] == '"' or line[pos + 1] == '\\':
                    code_len += 2
                    pos += 2
                elif line[pos + 1] == 'x':
                    code_len += 1
                    pos += 4
                else:
                    code_len += 1
                    pos += 2
            else:
                pos += 1

print(code_len - memory_len)
