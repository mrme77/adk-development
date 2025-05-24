from google.adk.agents import Agent

# Step 1: Define the agent
root_agent = Agent(
    name="greeting_agent",
    model="gemma3:12b-it-qat",  # Use the Gemma/Gemini model
    description="Greeting agent",
    instruction="""
    You are a helpful assistant that greets the user. 
    Ask for the user's name and greet them by name and add Forza Napoli!
    """
)


