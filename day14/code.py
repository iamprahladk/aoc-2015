with open('input.txt') as d:
    data = d.read().splitlines()

racers = []

for line in data:
    time_limit = 2503
    distance = 0
    split_line = line.split()
    lst = [int(split_line[3]), int(split_line[6]), int(split_line[-2])]
    while time_limit > 0:
        for i in range(lst[1]):
            distance += lst[0]
            time_limit -= 1
        time_limit -= lst[2]
    racers.append(distance)
print(f'Part 1: {max(racers)}')
