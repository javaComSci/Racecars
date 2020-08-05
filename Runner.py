import math
import random
from Racecar import Racecar
from Track import Track


# size in each generation
GENERATION_SIZE = 16

# all the possible directions of the racecar
directions = ["D", "U", "L", "R"]


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



# mutate the given direction list the given number of times
def mutate(parent, num_mutations):
    # create the mutated racecars
    racecars = []

    # create that many number of mutations to create racecars
    for i in range(num_mutations):
        new_parent = parent[:]
        mutation_point = random.randrange(len(parent))
        if new_parent[mutation_point] == "D":
            mutation_value = random.choice(["U", "L", "R"])
        elif new_parent[mutation_point] == "U":
            mutation_value = random.choice(["D", "L", "R"])
        elif new_parent[mutation_point] == "R":
            mutation_value = random.choice(["D", "L", "U"])
        elif new_parent[mutation_point] == "L":
            mutation_value = random.choice(["D", "R", "U"])
        new_parent[mutation_point] = mutation_value
        racecars.append(Racecar(new_parent))
    
    return racecars



# select the parents for creating offspring
def pick_parents(directions_to_distance):
    if len(directions_to_distance.keys()) == 1:
        return list(list(directions_to_distance.keys())[0]), list(list(directions_to_distance.keys())[0])
    else:
        return list(list(directions_to_distance.keys())[0]), list(list(directions_to_distance.keys())[1])


# generate the next generation
def generate_racecars(directions_to_distance):
    # create the new list of racecars
    racecars = []

    if len(directions_to_distance.keys()) > 0:
        # randomly pick parents of the generation
        parent1, parent2 = pick_parents(directions_to_distance)

        # add orignal parents in the generation
        racecars.append(Racecar(parent1))
        racecars.append(Racecar(parent2))

        # merge to create offspring
        crossover1, crossover2 = merge(parent1, parent2)
        racecars.append(Racecar(crossover1))
        racecars.append(Racecar(crossover2))

        # mutate to create offspring
        mutations1 = mutate(parent1, int((GENERATION_SIZE - 4)/2))
        mutations2 = mutate(parent2, int((GENERATION_SIZE - 4)/2))
        racecars += mutations1
        racecars += mutations2
    else:
        # create racecars with that specific number of directions
        for i in range(GENERATION_SIZE):
            initial_directions = []
            for j in range(5):
                initial_directions.append(random.choice(directions))
            racecar = Racecar(initial_directions)
            racecars.append(racecar)
    
    # add one more direction to each of the directions of the racecars
    for racecar in racecars:
        racecar.directions.append(random.choice(directions))

    return racecars



if __name__ == "__main__":
    # create a track instance
    track_file = "Track1.txt"
    track = Track(track_file)

    # create racecars to start with - first generation
    racecars = generate_racecars({})

    # go through a given number of evolutions
    for evolutions in range(100):

        # keep track of the directions associated with each of the distances
        directions_to_distance = {}

        # check the fitness of every racecar through the number of directions completed and distance from ending point
        for racecar in racecars:
            directions_completed, distance = racecar.go(track)
            # print(directions_completed, distance)
            directions_to_distance[tuple(directions_completed)] = distance
        
        # sort the racecars by fitness and remove empty directions
        directions_to_distance = {k: v for k, v in sorted(directions_to_distance.items(), key=lambda item: item[1]) if len(k) != 0}
        # print(directions_to_distance)

        # generate the new racecars based on existing directions
        racecars = generate_racecars(directions_to_distance)


    # view path of best racecar
    for racecar in racecars:
        directions_completed, distance = racecar.go(track)
        directions_to_distance[tuple(directions_completed)] = distance
    best_directions = sorted(directions_to_distance, key=directions_to_distance.get)
    best_racecar = Racecar(list(best_directions[0]))
    print(best_directions[0])
    best_racecar.go(track, view=True)
