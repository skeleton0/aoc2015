level = 0

with open('input.txt') as input:
    for char in input.read():
        if char == '(':
            level += 1
        elif char == ')':
            level -= 1

print('Final level:', level) 
