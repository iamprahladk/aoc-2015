import re

with open('input.txt') as d:
    data = d.read()

numbers = [int(n) for n in re.findall(r"-?\d+", data)]
print(f'Part 1: {sum(numbers)}')
