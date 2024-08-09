def find_houses_delivered(string, return_list=False):
    x = 0
    y = 0
    count = 1
    lst = [(0, 0)]
    for item in string:
        if item == '^':
            y += 1
        elif item == 'v':
            y -= 1
        elif item == '>':
            x += 1
        elif item == '<':
            x -= 1
        if (x, y) not in lst:
            lst.append((x, y))
            count += 1
    if return_list:
        return lst
    else:
        return count


def find_houses_delivered_by_robot(string):
    switch = True
    str1 = ''
    str2 = ''
    lst = []
    for item in string:
        if switch:
            str1 += item
        else:
            str2 += item
        switch = not switch
    lst.extend(find_houses_delivered(str1, True))
    lst.extend(find_houses_delivered(str2, True))
    print(f'Part 2: {len(list(set(lst)))}')


with open('input.txt') as d:
    data = d.read()

print(f'Part 1: {find_houses_delivered(data)}')
find_houses_delivered_by_robot(data)