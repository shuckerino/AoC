#!/usr/bin/env python3

with open("Input.txt") as file:
    content = file.read().strip().split("\n")
    time_list = [i for i in content[0].split(" ") if i.isnumeric()]
    distance_list = [i for i in content[1].split(" ") if i.isnumeric()]
    
    print(time_list)
    print(distance_list)
    

sum_of_all_possible_answers = 0
current_velocity = 0

# iterate over each race
for idx in range(0, len(time_list)):
    sum_of_all_possible_answers_of_race = 0
    # iterate over each possible waiting time
    for waiting_time in range(1, int(time_list[idx]) - 1):
        current_velocity = waiting_time # velocity equals waiting time 
        travelled_distance = (int(time_list[idx]) - waiting_time) * current_velocity # remaining race duration * velocity
        
        if travelled_distance > int(distance_list[idx]):
            sum_of_all_possible_answers_of_race += 1
            
    # the first result needs to be added, the rest need to be multiplied
    if sum_of_all_possible_answers == 0:
        sum_of_all_possible_answers += sum_of_all_possible_answers_of_race
    else:
        sum_of_all_possible_answers *= sum_of_all_possible_answers_of_race

print(f"result is {sum_of_all_possible_answers}")