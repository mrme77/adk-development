from google.adk.agents import Agent
import google.generativeai as genai

# Configure your API key (or rely on environment variables)
# genai.configure(api_key="YOUR_API_KEY")

# Define generation configuration
generation_config = genai.GenerationConfig(
    temperature=0.7,
    top_p=0.9,
    top_k=40, # Example value
    max_output_tokens=10, # Example value
    # You can also add 'stop_sequences' here
)

# Create the root agent
question_answering_agent = Agent(
    name="question_answering_agent",
    model="gemini-2.0-flash",
    description="Question answering agent",
    generation_config=generation_config,
    instruction="""
    You are a helpful assistant that answers questions about the user's preferences.

    Here is some information about the user:
    Name: 
    {user_name} #string interpolation
    Preferences: 
    {user_preferences}
    """,
)
