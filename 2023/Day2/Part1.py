with open("Input.txt") as file:
    games = [i.split(':')[1] for i in file.read().strip().split("\n")]

red = 12
green = 13
blue = 14


def valid_subgames(game):
    subgames = [i.strip() for i in game.split(";")]
    for subgame in subgames:
        if not valid_subgame(subgame):
            return False

    return True


def valid_subgame(subgame):
    dice = subgame.split(",")
    for die in dice:
        die = die.split()
        value = int(die[0])
        color = die[1]

        if not (
                (color == 'blue' and value <= blue) or
                (color == 'red' and value <= red) or
                (color == 'green' and value <= green)
                ):
            return False

    return True


game_sum = 0
for id, game in enumerate(games):
    id += 1
    if valid_subgames(game):
        game_sum += id


print("Part 1: ", game_sum)
