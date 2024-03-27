

import numpy as np

class OccupancyMap:

    def __init__(self):
        self.occupancy_grid = []




    def test_grid(self):
        # create test array for obstacle velocity
        self.occupancy_grid = np.zeros((100,100),dtype = int)

        # put some random obtacles in it