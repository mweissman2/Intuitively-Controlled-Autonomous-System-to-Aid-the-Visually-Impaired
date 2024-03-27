from global_planner import *
from local_planner import *
from occupancy_map import *

if __name__ == "__main__":


    # store the ambiguous address/place and send it to places API
    start ="Boston, MA"             # example, it will be current position
    goal = "Worcester, MA"          # comms

    # routes = google_planner(start, goal)  # call google planner and return routes


    # Below is testing
    robot_velocity = [5,0]
    robot_pos = [50,40]
    obstacle = [50,60]
    o_velocity =[-3,3]


    # print(routes)

    vo_algo = velocityObstacle()

    o_map = OccupancyMap()
    o_map.test_grid()    # create test grid


    vo_algo.vo_calculation(o_map.occupancy_grid,robot_pos,o_velocity,robot_velocity)
    # path = mplpath.Path(cone_vertices) # use this to visualize the cone construction