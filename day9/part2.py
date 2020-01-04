from itertools import permutations

distances = {}
locations = set()
with open('input.txt') as f:
    for line in f:
        words = line.split()
        distances[(words[0], words[2])] = int(words[4])
        distances[(words[2], words[0])] = int(words[4])
        locations.add(words[0])
        locations.add(words[2])

longest_distance = 0
for route in permutations(locations):
    distance = 0
    for i in range(1, len(route)):
        distance += distances[(route[i-1], route[i])]
    if distance > longest_distance:
        longest_distance = distance

print(longest_distance)
