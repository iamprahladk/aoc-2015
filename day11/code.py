def increment_char(string):
    string_reversed = list(string[::-1])
    for index, letter in enumerate(string_reversed):
        if letter != 'z':
            string_reversed[index] = chr(ord(string_reversed[index])+1)
            break
        else:
            string_reversed[index] = 'a'
    output = ''
    for item in string_reversed[::-1]:
        output += item
    return output


def password_rule_one(string):
    boolean = False
    for index, letter in enumerate(string[:-2]):
        if (ord(string[index+2]) - ord(string[index+1]) == 1 and
                ord(string[index+1]) - ord(string[index]) == 1):
            boolean = True
            break
    return boolean


def password_rule_two(string):
    if 'i' in string or 'o' in string or 'l' in string:
        return False
    else:
        return True


def password_rule_three(string):
    boolean = False
    skip_loop = False
    current_list = []
    for index, letter in enumerate(string[:-1]):
        if skip_loop:
            skip_loop = False
            continue
        if letter == string[index+1]:
            current_pair = f'{letter}{string[index + 1]}'
            current_list.append(current_pair)
            skip_loop = True
    if len(current_list) == 2:
        boolean = True
    return boolean


inp = 'hepxcrrq'
has_stopped = False

for n in range(1, 3):
    while not has_stopped:
        new_inp = increment_char(inp)
        if password_rule_one(new_inp) and password_rule_two(new_inp) and password_rule_three(new_inp):
            print(f'Part {n}: {new_inp}')
            inp = new_inp
            break
        else:
            inp = new_inp
