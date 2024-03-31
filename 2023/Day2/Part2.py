with open("Input.txt") as file:
    games = [i.split(':')[1] for i in file.read().strip().split("\n")]


def get_power_of_game(game):
    subgames = [i.strip() for i in game.split(";")]
    min_red = 0
    min_blue = 0
    min_green = 0
    for subgame in subgames:
        dice = subgame.split(",")
        for die in dice:
            die = die.split()
            value = int(die[0])
            color = die[1]

            if color == 'blue' and value >= min_blue:
                min_blue = value
            elif color == 'red' and value >= min_red:
                min_red = value
            elif color == 'green' and value >= min_green:
                min_green = value

    return min_red * min_green * min_blue


game_sum = 0
for _, game in enumerate(games):
    game_sum += get_power_of_game(game)


print("Part 2: ", game_sum)
