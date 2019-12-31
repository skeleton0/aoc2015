with open('input.txt') as input:
    x = y = 0
    houses = {(x, y)}
    for char in input.read():
        if char == '^':
            y -= 1
        elif char == '>':
            x += 1
        elif char == 'v':
            y += 1
        elif char == '<':
            x -= 1

        houses.add((x, y))

print('Unique houses visited:', len(houses))
