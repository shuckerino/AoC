#!/usr/bin/env python3

with open("Input.txt") as file:
    content = file.read().strip().split("\n")
    race_duration = "".join([i for i in content[0].split(" ") if i.isnumeric()])
    distance_record = "".join([i for i in content[1].split(" ") if i.isnumeric()])
    
    print(race_duration)
    print(distance_record)
    

result = 0

for waiting_time in range(1, int(race_duration) - 1):
    current_velocity = waiting_time # velocity equals waiting time 
    travelled_distance = (int(race_duration) - waiting_time) * current_velocity # remaining race duration * velocity
        
    if travelled_distance > int(distance_record):
        result += 1

print(f"result is {result}")