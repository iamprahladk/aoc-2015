with open('input.txt') as data:
    data = data.read().splitlines()

correct_sue = [
    'children: 3',
    'cats: 7',
    'samoyeds: 2',
    'pomeranians: 3',
    'akitas: 0',
    'vizslas: 0',
    'goldfish: 5',
    'trees: 3',
    'cars: 2',
    'perfumes: 1'
]

for line in data:
    counter = 0
    for item in correct_sue:
        if item.split()[0] in line:
            if item.split()[1] == line[line.find(item.split()[0])+len(item.split()[0])+1]:
                counter += 1
    if counter == 3:
        print(f'Part 1: {line[4:6]}')
