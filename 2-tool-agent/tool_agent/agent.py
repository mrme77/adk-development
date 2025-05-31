from google.adk.agents import Agent
from image_tool import generate_image
#from ..image_tool import generate_image

root_agent = Agent(
    name="tool_agent",
    model="gemini-2.0-flash",
    description="generate images based on text prompts",
    instruction="""
    You are a helpful assistant that can use the following tools:
    - generate_image
    """,
    tools=[generate_image],
)
