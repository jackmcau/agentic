from agentic.common import Agent, AgentRunner
import os
import requests

def location_to_long_lat(address):
    # This was added due to an inconsistency in the longitude and latitude that ChatGPT gave to the actual location
    # Longitude and latitude is supposedly needed in order to call the nearby search api from what I've seen
    url = "https://maps.googleapis.com/maps/api/geocode/json"
    # set up google maps api key with export GOOGLE_MAPS_API_KEY=<key>
    key = os.environ["GOOGLE_MAPS_API_KEY"]
    params = {"address": address, "key": key}
    response = requests.get(url, params=params).json()
    location = response["results"][0]["geometry"]["location"]
    return f"Latitude: {location["lat"]}, Longitude: {location["lng"]}"

agent = Agent(
    name="agent",
    welcome="""I can help you find restaurants in your area!
            Input your location,
            how far from this location you would be willing to go,
            the type of cuisine or food you would like to eat,
            and the time of day you will be eating at.
            """,
    instructions="""You help people find restaurants to eat at. You must first:
                Ask about the preferred location, cuisine or food, and time of day. The user may input these in a comma separated list.
                Then convert the location to longitude and latitude, the food to a cuisine type, and the time of day to breakfast, lunch, or dinner
                Lastly, tell these converted values back to the user. Do not say anything other than the converted values.
                """,
    tools=[location_to_long_lat]
)

if __name__ == "__main__":
    AgentRunner(agent).repl_loop()
