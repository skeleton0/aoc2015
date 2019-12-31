with open('input.txt') as input:
    x1 = y1 = x2 = y2 = 0
    houses = {(x1, y1)}
    for i, char in enumerate(input.read()):
        x = y = 0
        if char == '^':
            y -= 1
        elif char == '>':
            x += 1
        elif char == 'v':
            y += 1
        elif char == '<':
            x -= 1

        if i % 2 == 0:
            x2 += x
            y2 += y
            houses.add((x2, y2))
        else:
            x1 += x
            y1 += y
            houses.add((x1, y1))

print('Unique houses visited:', len(houses))
