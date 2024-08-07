def find_required_wrapping_paper(n1, n2, n3):
    lst = [n1*n2, n1*n3, n2*n3]
    slack = min(lst)
    surface_area = (lst[0] + lst[1] + lst[2]) * 2
    return slack + surface_area


def find_required_ribbon_length(n1, n2, n3):
    perimeters = [(n1+n2) * 2, (n1+n3) * 2, (n2+n3) * 2]
    bow = n1*n2*n3
    return min(perimeters) + bow


with open('input.txt') as d:
    data = d.read().splitlines()

num, num2 = 0, 0
for item in data:
    split_item = item.split('x')
    num += find_required_wrapping_paper(int(split_item[0]), int(split_item[1]), int(split_item[2]))
    num2 += find_required_ribbon_length(int(split_item[0]), int(split_item[1]), int(split_item[2]))

print(f'Part1: {num}, Part2: {num2}')