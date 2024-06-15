#!/usr/bin/env python3

RANK_ORDER = { "2": 0, "3": 1, "4": 2, "5": 3, "6": 4, "7": 5, "8": 6, "9": 7, "T": 8, "J": 9, "Q": 10, "K": 11, "A": 12 }

def sort_single_hand(hand):
    return "".join(sorted(hand, key=lambda x: RANK_ORDER[x], reverse=True))

def hand_key(hand):
    # Convert each card in the hand to its numerical rank and sort in descending order
    return sorted([RANK_ORDER[card] for card in hand], reverse=True)

def sort_all_hands(list_of_all_hands):
    sorted_hands = []
    for hand in list_of_all_hands:
        sorted_hands.append(sort_single_hand(hand))
        
    sorted_hands = sorted(list_of_all_hands, key=hand_key, reverse=True)
    return sorted_hands

W
with open("Input.txt") as file:
    content = file.read().strip().split("\n")
    
total_sum = 0
hand_dict = dict()

for line in content:
    line = line.split(" ")
    hand_dict[line[0]] = line[1]
    
# print(hand_dict)
    
# cards_only = [line[0:5] for line in content]
sorted_hands = sort_all_hands(hand_dict.keys())

for i in range(0, len(sorted_hands)):
    total_sum += i * int(hand_dict[sorted_hands[i]])
# print(len(content))
print(sorted_hands)
print(total_sum)

