import re


def get_numbers(s):
    array = re.findall(r'[0-9]+', s)
    return array


def check_line_below(val, idx):
    for i in range(10 + idx - 1, 10 + idx + len(val) + 1):
        if content[i] == '.':
            return False
    return True


def check_line_above(val, idx):
    for i in range(-10 + idx - 1, -10 + idx + len(val) + 1):
        if content[i] == '.':
            return False
    return True


file = open("Input.txt", "r")

content = file.read()

sum = 0
count = 0

for num in get_numbers(content):
    value = str(num)
    idx = content.strip().replace("\n", "").find(value)
    print(num + ": Index is {index}".format(index=idx))
    if content[idx - 1] != '.' and content[idx + len(value)] != '.':
        print("Current line was already enough with number {number} and Index before: {idx1} and index after: {idx2}"
              .format(number=num, idx1=content[idx-1], idx2=content[idx + len(value)]))
        sum += int(num)
        count += 1
    else:
        count += 1
        if count == 1:
            if check_line_below(value, idx):
                print(num + ": First line is valid")
                sum += int(num)
        elif count == len(file.readlines()):
            if check_line_above(value, idx):
                print(num + ": Last line is valid")
                sum += int(num)
        else:
            if check_line_above(value, idx) and check_line_below(value, idx):
                print(num + ": InBetween line is valid")
                sum += int(num)


print(sum)
