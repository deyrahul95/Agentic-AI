from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

from weather_agent.tools.get_weather_tool import get_weather
from weather_agent.tools.get_current_time_tool import get_current_time

from weather_agent.prompt import WEATHER_PROMPT


AGENT_MODEL = LiteLlm(model="ollama_chat/llama3.2:1b")

root_agent = Agent(
    name="weather_agent",
    description="Provides weather information for specific cities.",
    model=AGENT_MODEL,
    instruction=WEATHER_PROMPT,
    tools=[get_current_time, get_weather],
)
