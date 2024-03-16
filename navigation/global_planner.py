# from controller import *        # controller is name of Webots API
#
import googlemaps
from datetime import datetime
def google_planner(start,goal):
    '''
    For global planner we plan to use google-maps API to retrieve global path
    start:
    Must be string of address that is passed to the directions method

    goal:
    Must be string of address that is passed to the directions method
    '''
    gmaps = googlemaps.Client(key='Add Your Key here')  # key should be kept secret on server
    path = []          # somehow need to build a map from the google maps directions

    # we can do many things, either search for the address based on location, feed address
    # big ticket item is converting the google maps directions to the webots


    # Geocoding an address
    geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

    # Look up an address with reverse geocoding
    reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

    # Request directions via public transit
    now = datetime.now()
    # Full explanation of arguments:
    # https://github.com/googlemaps/google-maps-services-python/blob/master/googlemaps/directions.py
    # https://googlemaps.github.io/google-maps-services-python/docs/index.html#googlemaps.Client.directions

    # manual testing, this is a 1/2 mile distance
    start = "Fuller Apartments, Institute Rd, Worcester, MA 01609"
    goal = "Worcester Art Museum, 55 Salisbury St, Worcester, MA 01609"
    # call directions method, set parameter to walking, departure_time
    # returns list of routes
    directions_result = gmaps.directions(start,
                                         goal,
                                         mode="walking",
                                         departure_time=now,
                                         )

    # Validate an address with address validation
    addressvalidation_result = gmaps.addressvalidation(['1600 Amphitheatre Pk'],
                                                       regionCode='US',
                                                       locality='Mountain View',
                                                       enableUspsCass=True)
    return directions_result
def interpret_directions():
    pass



