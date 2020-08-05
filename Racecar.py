import random
import math

MANHATTAN = 0
EUCLIDIAN = 1

# class that contains the information needed for a racecar
class Racecar:
    def __init__(self, directions):
        self.directions = directions
    

    # calculate the distance from the exit
    def calculate_fitness(self, current_row, current_col, ending_row, ending_col, distance=MANHATTAN):
        if distance == EUCLIDIAN:
            return ((current_col - ending_col)**2 + (current_row - ending_row)**2)**0.5
        else:
            return abs(current_col - ending_col) + abs(current_row - ending_row)



    # see where the car ends up with directions
    def go(self, track):
        # set the current points
        current_row = track.starting_row
        current_col = track.starting_col

        # keep track of the directions that it has executed
        done = 0

        # go through the directions
        for direction in self.directions:
            # keep track of previous position before the move
            prev_row = current_row
            prev_col = current_col

            # update the positions
            if direction == "U":
                current_row -= 1
            elif direction == "D":
                current_row += 1
            elif direction == "L":
                current_col -= 1
            else:
                current_col += 1

            # check if valid move
            if (current_row < 0 or current_row >= track.height) or (current_col < 0 or current_col >= track.width) or (track.track[current_row][current_col] != " "):
                fitness = self.calculate_fitness(prev_row, prev_col, track.ending_row, track.ending_col)
                return (self.directions[:done], fitness)
            
            # add it to the directions that it has completed
            done += 1

        # all directions have been completed
        fitness = self.calculate_fitness(current_row, current_col, track.ending_row, track.ending_col)
        return (self.directions, fitness)