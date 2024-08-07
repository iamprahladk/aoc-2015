# Part one functions
def test_one(string):
    counter_ = 0
    vowels = 'aeiou'
    boolean = False
    for letter in string:
        if letter in vowels:
            counter_ += 1
        if counter_ == 3:
            boolean = True
            break
    return boolean


def test_two(string):
    current_letter = ''
    boolean = False
    for letter in string:
        if letter == current_letter:
            boolean = True
            break
        else:
            current_letter = letter
    return boolean


def test_three(string):
    lst = ['ab', 'cd', 'pq', 'xy']
    boolean = True
    for val in lst:
        if val in string:
            boolean = False
            break
    return boolean


# Part two functions
def new_test_one(string):
    boolean = False
    current_list = []
    for index, letter in enumerate(string[:-1]):
        current_pair = f'{letter}{string[index+1]}'
        current_list.append(current_pair)
    for index, pair in enumerate(current_list[:-2]):
        if pair in current_list[index+2:]:
            boolean = True
            break
    return boolean


def new_test_two(string):
    boolean = False
    for index, letter in enumerate(string[:-2]):
        if letter == string[index+2]:
            boolean = True
            break
    return boolean


with open('input.txt') as d:
    data = d.read().splitlines()

counter = 0
counter2 = 0

for item in data:
    if test_one(item) and test_two(item) and test_three(item):
        counter += 1
    if new_test_one(item) and new_test_two(item):
        counter2 += 1

print(counter)
print(counter2)
