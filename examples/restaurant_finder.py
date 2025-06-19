from agentic.common import Agent, AgentRunner

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
    tools=[]
)

if __name__ == "__main__":
    AgentRunner(agent).repl_loop()