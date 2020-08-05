import math
import random
from Racecar import Racecar
from Track import Track


# merging directions to produce new directions
def merge(directions1, directions2):
    # determine where to crossover the directions
    crossover_point_1 = random.randrange(len(directions1))
    crossover_point_2 = random.randrange(len(directions2))

    # get the left and right parts of each direction
    directions1_left = directions1[:crossover_point_1]
    directions1_right = directions1[crossover_point_1:]
    directions2_left = directions2[:crossover_point_2]
    directions2_right = directions2[crossover_point_2:]

    # print("MERGING")
    # print(directions1_left, directions1_right)
    # print(directions2_left, directions2_right)

    # create new offspring
    offspring1 = directions1_left + directions2_right
    offspring2 = directions2_left + directions1_right

    return offspring1, offspring2



if __name__ == "__main__":
    # create a track instance
    track_file = "Track1.txt"
    track = Track(track_file)

    # all the possible directions of the racecar
    directions = ["D", "U", "L", "R"]

    # create 5 racecars to start with - first generation
    racecars = []
    for i in range(4):
        initial_directions = []
        for j in range(5):
            initial_directions.append(random.choice(directions))
        racecar = Racecar(initial_directions)
        racecars.append(racecar)
    

    # go through a given number of evolutions
    for evolutions in range(100):

        # keep track of the directions associated with each of the distances
        directions_to_distance = {}

        # check the fitness of every racecar through the number of directions completed and distance from ending point
        for racecar in racecars:
            directions_completed, distance = racecar.go(track)
            # print(directions_completed, distance)
            directions_to_distance[tuple(directions_completed)] = distance
        
        # sort the racecars by fitness
        best_directions = sorted(directions_to_distance, key=directions_to_distance.get)

        # remove the empty set of directions
        cleaned_best_directions = []
        for direction in best_directions:
            if len(direction) > 0:
                cleaned_best_directions.append(direction)
        best_directions = cleaned_best_directions


        # create the new set of racecars
        racecars = []

        # merge the directions together
        offspring1 = None
        offspring2 = None
        if len(best_directions) > 1:
            best_directions_0 = list(best_directions[0])
            best_directions_0.append(random.choice(directions))
            racecars.append(Racecar(best_directions_0))
        if len(best_directions) > 2:
            offspring1, offspring2 = merge(best_directions[0], best_directions[1])
            racecars.append(Racecar(offspring1))
            racecars.append(Racecar(offspring2))
            best_directions_1 = list(best_directions[1])
            best_directions_1.append(random.choice(directions))
            racecars.append(Racecar(best_directions_1))
        
        # create the new racecars
        while len(racecars) < 4:
            initial_directions = []
            for j in range(5):
                initial_directions.append(random.choice(directions))
            racecar = Racecar(initial_directions)
            racecars.append(racecar)
        

    # get the racecars and how much they go
    for racecar in racecars:
        directions_completed, distance = racecar.go(track)
        print(directions_completed, distance)


