lights = [[False for x in range(1000)] for y in range(1000)]

def execute_turn_instruction(words):
    light_mode = words[1] == 'on'
    sx, sy = [int(i) for i in words[2].split(',')]
    ex, ey = [int(i) for i in words[4].split(',')]

    for y in range(sy, ey + 1):
        for x in range(sx, ex + 1):
            lights[y][x] = light_mode

def execute_toggle_instruction(words):
    sx, sy = [int(i) for i in words[1].split(',')]
    ex, ey = [int(i) for i in words[3].split(',')]

    for y in range(sy, ey + 1):
        for x in range(sx, ex + 1):
            lights[y][x] = not lights[y][x]

def execute_instruction(string):
    words = line.split()
    if words[0] == 'turn':
        execute_turn_instruction(words)
    else:
        execute_toggle_instruction(words)

with open('input.txt') as input_file:
    for line in input_file:
        execute_instruction(line)

lights_lit = 0
for y in range(1000):
    lights_lit += lights[y].count(True)

print('Lights lit:', lights_lit)
