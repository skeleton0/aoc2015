from hashlib import md5

secret_key = 'ckczppom'
val = 0

while True:
    digest = int(md5(bytes(secret_key + str(val), 'ascii')).hexdigest(), 16)
    if digest <= 0xfffffffffffffffffffffffffff:
        break
    else:
        val += 1

print(val)
