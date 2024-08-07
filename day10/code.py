def look_and_say(num):
    lst = []
    sub_lst = []
    num_str = ''
    for index, digit in enumerate(num[0:]):
        if digit == num[index - 1]:
            sub_lst.append(digit)
        else:
            lst.append(sub_lst)
            sub_lst = [digit]
    lst.append(sub_lst)
    for sub_list in lst:
        if sub_list:
            num_str += f'{len(sub_list)}{sub_list[0]}'
    return num_str


inp = '1113222113'
for n in range(50):
    inp = look_and_say(inp)
    if n == 39:
        print(f'Part 1: {len(inp)}')
print(f'Part 2: {len(inp)}')
