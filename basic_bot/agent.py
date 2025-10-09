from google.adk.agents import Agent
import dotenv

dotenv.load_dotenv() # Load environment variables from .env file

MODEL = "gemini-2.5-flash"

root_agent = Agent(
    name="main_agent",
    description="He the first test agent",
    model=MODEL,
    instruction="""You are the first ai agent. 
                   From begin every message say Hello master Andrew!.""",

)