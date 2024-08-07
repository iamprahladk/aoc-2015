with open('input.txt') as k:
    data = k.read()

num = 0
count = 0
boolean = True
for letter in data:
    count += 1
    if letter == '(':
        num += 1
    else:
        num -= 1
    if num == -1 and boolean:
        print(f'Part 2: {count}')
        boolean = False

print(f'Part 1: {num}')
