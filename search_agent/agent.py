from google.adk.agents import Agent
import dotenv
from google.adk.tools import google_search

dotenv.load_dotenv() # Load environment variables from .env file

MODEL = "gemini-2.5-flash"


root_agent = Agent(
    name="search_agent",
    model=MODEL,
    instruction="You have access to the search trough the internet.",
    tools=[google_search],

)