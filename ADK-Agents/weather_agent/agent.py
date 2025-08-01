from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

from weather_agent.tools.get_weather_tool import get_weather


AGENT_MODEL = LiteLlm(model="ollama_chat/llama3.2:1b")

root_agent = Agent(
    name="weather_agent",
    description="Provides weather information for specific cities.",
    model=AGENT_MODEL,
    instruction="""
        You are a helpful weather assistant.
        When the user asks for the weather in a specific city, 
        use the 'get_weather' tool to find the information. 
        If the tool returns an error, inform the user politely. 
        If the tool is successful, present the weather report clearly.
    """,
    tools=[get_weather],
)
