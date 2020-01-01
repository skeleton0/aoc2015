lights = [[0 for x in range(1000)] for y in range(1000)]

def execute_turn_instruction(words):
    sx, sy = [int(i) for i in words[2].split(',')]
    ex, ey = [int(i) for i in words[4].split(',')]

    light_mode = 1
    if words[1] == 'off':
        light_mode = -1

    for y in range(sy, ey + 1):
        for x in range(sx, ex + 1):
            lights[y][x] += light_mode
            if (lights[y][x] < 0):
                lights[y][x] = 0

def execute_toggle_instruction(words):
    sx, sy = [int(i) for i in words[1].split(',')]
    ex, ey = [int(i) for i in words[3].split(',')]

    for y in range(sy, ey + 1):
        for x in range(sx, ex + 1):
            lights[y][x] += 2

def execute_instruction(string):
    words = line.split()
    if words[0] == 'turn':
        execute_turn_instruction(words)
    else:
        execute_toggle_instruction(words)

with open('input.txt') as input_file:
    for line in input_file:
        execute_instruction(line)

brightness = 0
for y in range(1000):
    for x in range(1000):
        brightness += lights[y][x]

print('Total brightness:', brightness)
