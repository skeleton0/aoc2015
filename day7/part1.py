#part2 requires no code changes

class Instruction:
    def __init__(self, input_a, input_b, operation):
        self.input_a = input_a
        self.input_b = input_b
        self.operation = operation

instructions = {}
cache = {}

def calc_input(wire):
    #check if we've cached a value for this input wire
    if wire in cache:
        return cache[wire]

    if wire.isdecimal():
        res = int(wire)
    else:
        instr = instructions[wire]
        if not instr.operation:
            res = calc_input(instr.input_a)
        elif instr.operation == 'NOT':
            #effectively a logical NOT on the first 16 bits
            res = calc_input(instr.input_a) ^ 0x0FFFF
        elif instr.operation == 'AND':
            res = calc_input(instr.input_a) & calc_input(instr.input_b)
        elif instr.operation == 'OR':
            res = calc_input(instr.input_a) | calc_input(instr.input_b)
        elif instr.operation == 'RSHIFT':
            res = calc_input(instr.input_a) >> calc_input(instr.input_b)
        elif instr.operation == 'LSHIFT':
            #left shifting may create a 17-bit number, so we bitwise AND with a 16-bit mask to prevent that
            res = calc_input(instr.input_a) << calc_input(instr.input_b) & 0x0FFFF
        else:
            raise RuntimeError('Unknown operation')

    #cache result
    cache[wire] = res
    return res

with open('input.txt') as input_file:
    for line in input_file:
        words = line.split()
        if words[0] == 'NOT':
            instructions[words[3]] = Instruction(words[1], '', words[0])
        elif words[1] == '->':
            instructions[words[2]] = Instruction(words[0], '', '')
        else:
            instructions[words[4]] = Instruction(words[0], words[2], words[1])

print('Input to wire a:', calc_input('a'))
