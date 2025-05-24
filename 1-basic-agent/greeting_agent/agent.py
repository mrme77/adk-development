from google.adk.agents import Agent

root_agent = Agent(
    name="greeting_agent",
    # https://ai.google.dev/gemini-api/docs/models
    model="gemini-2.0-flash",
    description="Greeting agent",
    instruction="""
    You are a helpful assistant that greets the user. 
    Ask for the user's name and greet them by name and also say 
    Napoli won his 4th scudetto!
    """)

# from google.adk.agents import Agent

# # Step 1: Define the agent
# root_agent = Agent(
#     name="greeting_agent",
#     model="gemma3",  # Use the Gemma/Gemini model
#     description="Greeting agent",
#     instruction="""
#     You are a helpful assistant that greets the user. 
#     Ask for the user's name and greet them by name and add Forza Napoli!
#     """
# )



