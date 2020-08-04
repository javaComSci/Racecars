import random
import math

track = []
# get the track that the car will run on
with open("Track1.txt", "r") as f:
    for line in f:
        track.append(list(line)[:-1])
starting_row = 1
starting_col = 2
ending_point_col = 70
track_width = len(track[0])
track_height = len(track)
print("TRACK WIDTH: ", track_width)
print("TRACK HEIGHT: ", track_height)


class Racecar:
    def __init__(self, directions):
        self.directions = directions
    
    # calculate the distance from the exit
    def calculate_fitness(self, current_row, current_col):
        return abs(current_col - ending_point_col)

    # get the directions provided
    def get_directions(self):
        return self.directions

    # see where the car ends up with directions
    def go(self):
        # set the current points
        current_row = starting_row
        current_col = starting_col

        # go through the directions
        for direction in self.directions:
            if direction == "U":
                current_row -= 1
            elif direction == "D":
                current_row += 1
            elif direction == "L":
                current_col -= 1
            else:
                current_col += 1

            # check if valid move
            if current_row < 0 or current_row >= track_height:
                return -1
            if current_col < 0 or current_col >= track_width:   
                return -1
            if track[current_row][current_col] != " ":
                return -1
        
        return self.calculate_fitness(current_row, current_col)
            



# all the possible directions of the racecar
directions = ["D", "U", "L", "R"]


# create the racecars with random directions
racecars = []
for i in range(5):
    initial_directions = []
    for j in range(5):
        initial_directions.append(random.choice(directions))
    racecar = Racecar(initial_directions)
    racecars.append(racecar)


# try this number of evolutions
for evolutions in range(20):
    directions_to_fitness = {}
    # see how well this set of racecars does
    for racecar in racecars:
        result = racecar.go()
        if result != -1:
            directions_to_fitness[tuple(racecar.get_directions())] = result
    print(directions_to_fitness)
    # create the new set of racecars
    racecars = []
    directions_to_fitness = {k: v for k, v in sorted(directions_to_fitness.items(), key=lambda item: item[1])}
    for key, value in directions_to_fitness.items():
        new_directions = list(key)
        new_directions.append(random.choice(directions))
        racecars.append(Racecar(new_directions))





