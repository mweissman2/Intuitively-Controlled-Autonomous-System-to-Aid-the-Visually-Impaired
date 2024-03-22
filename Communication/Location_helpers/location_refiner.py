import json
import requests
from Communication import utils

# Replace YOUR_API_KEY with your actual Google Places API key
API_KEY = utils.get_key("GOOGLE_MAPS_API_KEY")


def destination_search(text_query: str, location: tuple, radius: float = 1609.344) -> dict:
    """
    Input destination as string, current location and desired search radius (1-mile default)
    Returns dictionary of results
    """
    # Note: DEFAULT ranks by relevance, but can change to distance if we want

    # Build the request URL
    url = "https://places.googleapis.com/v1/places:searchText"

    # Request body as a dictionary
    request_body = {
        "textQuery": text_query
    }

    locationRestriction = {
        "circle": {
            "center": {
                "latitude": location[0],
                "longitude": location[1]
            },
            "radius": radius
        }
    }
    location_restriction_json = json.dumps(locationRestriction)

    # Request headers
    headers = {
        "Content-Type": "application/json",
        "X-Goog-Api-Key": API_KEY,
        # Include field mask for specific data
        "X-Goog-FieldMask": "places.displayName,places.formattedAddress,places.location",
        "locationRestriction": location_restriction_json
    }

    # Send the POST request with JSON data in body and headers
    response = requests.post(url, json=request_body, headers=headers)

    # Check for successful response
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Save the JSON data to a file
        # with open('search_results.json', 'w') as outfile:
        #     json.dump(data, outfile, indent=4)

        # Loop through results and print basic information
        for place in data["places"]:
            print(f"Name: {place['displayName']['text']}")
            print(f"Address: {place['formattedAddress']}")
            print(f"Location: {place['location']}")
            print()

        # Return Top place (dictionary)
        return data['places'][0]

    else:
        print(f"Error: {response.status_code}")


def get_gps_coords():
    # Enter actual get_gps_coords function here (or call from somewhere else)
    # For now, just using coords from WPI Quad
    return 42.27377897661122, -71.80928749664702


# Define search term
search_term = "grocery store near WPI"

# Get current position
lat, long = get_gps_coords()

# Run search
top_place = destination_search(search_term, location=(lat, long))
print(f"TOP PLACE: {top_place['displayName']['text']} \n"
      f"{top_place['formattedAddress']} \n"
      f"{top_place['location']}")
