import math
import random


# class to keep track of the information in the track
class Track:
    def __init__(self, track_file):
        self.track_file = track_file

        # create a 2d array with the track
        self.track = []

        # get the track that the car will run on
        with open(track_file, "r") as f:
            # add all the lines on the file without the appended newline
            for line in f:
                self.track.append(list(line)[:-1])
        
        ######## TRACK1 #########
        # set the starting position of the track
        self.starting_row = 2
        self.starting_col = 1
        # set the ending position of the track
        self.ending_row = 3
        self.ending_col = 69
    
        ######## TRACK2 #########
        # # set the starting position of the track
        # self.starting_row = 2
        # self.starting_col = 1
        # # set the ending position of the track
        # self.ending_row = 17
        # self.ending_col = 34

        # get the boundaries of the track
        self.width = len(self.track[0])
        self.height = len(self.track)

        print("TRACK DIMENSIONS: ", self.height, self.width)
