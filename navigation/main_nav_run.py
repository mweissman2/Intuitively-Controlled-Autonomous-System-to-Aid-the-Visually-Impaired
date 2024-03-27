from global_planner import *



if __name__ == "__main__":


    # store the ambiguous address/place and send it to places API
    start ="Boston, MA"             # example, it will be current position
    goal = "Worcester, MA"          # comms


    routes = google_planner(start,goal)     # call google planner and return routes

    # print(routes)

