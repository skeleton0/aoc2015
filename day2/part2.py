total = 0
with open('input.txt') as input:
    for dimensions in input:
        l, w, h = [int(v) for v in dimensions.strip().split('x')]
        total += 2 * ((l + w + h) - max(l, w, h))
        total += l * w * h

print('Quantity of ribbon to order:', total)
