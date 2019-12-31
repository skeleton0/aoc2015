with open('input.txt') as input:
    level = 0
    for i, char in enumerate(input.read(), 1):
        if char == '(':
            level += 1
        elif char == ')':
            level -= 1

        if level < 0:
            print('Santa entered the basement at character:', i)
            break
