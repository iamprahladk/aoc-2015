import hashlib

inp = 'iwrupvqb'
counter = 0
switch = True

while True:
    counter += 1
    updated_inp = inp + str(counter)
    md5 = hashlib.md5(updated_inp.encode()).hexdigest()
    if md5.startswith('00000') and switch:
        print(f'Part 1: {updated_inp[len(inp):]}')
        switch = False
    if md5.startswith('000000'):
        print(f'Part 2: {updated_inp[len(inp):]}')
        break
