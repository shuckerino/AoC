#!/bin/python3


if __name__ == "__main__":
    all_lines = []
    list1 = []
    list2 = []
    with open("./input.txt", "r") as file:
        all_lines = file.readlines()
    for line in all_lines:
        val_list = [val.strip()
                    for val in line.strip().split(" ") if val != ""]
        list1.append(val_list[0])
        list2.append(val_list[1])

    list1 = sorted(list1)
    list2 = sorted(list2)
    # print(list1)
    # print(list2)
    result_diff = 0
    for i in range(len(list1)):
        result_diff += abs(int(list1[i]) - int(list2[i]))
    print(result_diff)
