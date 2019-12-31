total = 0
with open('input.txt') as input:
    for dimensions in input:
        l, w, h = [int(v) for v in dimensions.strip().split('x')]
        s1, s2, s3 = (l * w), (w * h), (h * l)
        total += 2 * (s1 + s2 + s3) + min(s1, s2, s3)

print('Quantity of wrapping paper to order:', total)
