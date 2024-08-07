inp = 'To continue, please consult the code grid in the manual. Enter the code at row 3010, column 3019.'
col, row = [int(item[:-1]) for item in inp.split()[-3::2]]

MULTIPLIER = 252533
DIVISOR = 33554393
counter = 0
current_col = 1
current_row = 1
current_number = 20151125

for n in range(2, col+row+10):
    col_lst = list(range(1, n+1))
    row_lst = list(range(n, 0, -1))
    for k in range(n):
        current_number *= MULTIPLIER
        current_number = current_number % DIVISOR
        if row_lst[k] == 3010 and col_lst[k] == 3019:
            print(f'Part 1: {current_number}')
