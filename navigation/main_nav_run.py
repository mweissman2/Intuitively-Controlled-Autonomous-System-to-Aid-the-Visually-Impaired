from global_planner import *



if __name__ == "__main__":
    start ="Boston, MA"
    goal = "Worcester, MA"
    routes = google_planner(start,goal)     # call google planner and return routes