#!/usr/bin/python3
# Data fetching goes here.
import os
from Datasets.__meta__.state_names import states

DATA_DIR = 'Datasets/USA'


# Some of this is pure data handling and some touches file system.
class StateData(object):

    def __init__(self):
        self.states = [f for f in os.listdir(DATA_DIR) if os.path.isfile(os.path.abspath(os.path.join(DATA_DIR, f))) and not f.startswith('.')]
        self.idx = 0

    def __iter__(self):
        yield from self.states

    def __next__(self):
        self.idx += 1
        try:
            return self.states[self.idx-1]
        except IndexError:
            self.idx = 0
            raise StopIteration

    def get_name(self, state_abbr):
        return states.get(state_abbr)
        pass

    def get_states(self):
        return states


class WorldData(object):
    pass


def get_region_data(region: str) -> str:
    "Given the name of a city, returns string containing filepath to city data csv"
    dataset = DATA_DIR + '/' + region + '.csv'
    return dataset
