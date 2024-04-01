#!/usr/bin/env python3

with open("Input.txt") as file:
    content = file.read().strip().split("\n")
    winning_numbers = [i.split('|')[0].split(':')[1].strip() for i in content]
    my_numbers = [i.split('|')[1].strip() for i in content]

# print(winning_numbers)
# print(my_numbers)

sum = 0

for i in range (0, len(winning_numbers)):
    individual_winning_numbers = [j for j in winning_numbers[i].split(" ") if j != ""]
    individual_my_numbers = [j for j in my_numbers[i].split(" ") if j != ""]
    
    print(individual_winning_numbers)
    print(individual_my_numbers)

    result_set = set(individual_winning_numbers).intersection(set(individual_my_numbers))
    
    if len(result_set) > 0:
        sum += 2 ** (len(result_set) - 1)

print("Sum for all is {s}".format(s = sum))
