import re


def get_numbers(s):
    array = re.findall(r'[0-9]+', s)
    return array


def line_below_is_hit(val, idx):
    for i in range(10 + idx - 1, 10 + idx + len(val)):
        if content[i] not in ". ":
            return True
    return False


def line_above_is_hit(val, idx):
    for i in range(-10 + idx - 1, -10 + idx + len(val)):
        if content[i] not in ". ":
            return True
    return False


file = open("Input.txt", "r")
content = file.read()

sum = 0

for num in get_numbers(content):
    value = str(num)
    idx = content.strip().replace("\n", "").find(value)
    # print(num + ": Index is {index}".format(index=idx))

    # first check if before or after word in current line is anything except a point
    if content[idx - 1] != '.' and content[idx + len(value)] != '.':
        print("Current line hit for {number}. Index before: {idx1} and index after: {idx2}"
              .format(number=num, idx1=content[idx-1], idx2=content[idx + len(value)]))
        sum += int(num)
    else:
        if idx < 10:  # for all nums in first line, only check line below
            if line_below_is_hit(value, idx):
                print(num + ": Line below hits number")
                sum += int(num)
        # for all nums in last line, only check lines above
        elif idx >= 10 * len(file.readlines()) - 1:
            if line_above_is_hit(value, idx):
                print(num + ": Line above hits number")
                sum += int(num)
        else:
            if line_above_is_hit(value, idx) or line_below_is_hit(value, idx):
                print(num + ": Line above or below is a hit")
                sum += int(num)

file.close()
print(sum)
