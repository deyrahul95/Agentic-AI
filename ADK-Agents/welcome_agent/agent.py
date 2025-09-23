from google.adk.agents import Agent
from google.genai import types
from google.adk.models.lite_llm import LiteLlm
from pydantic import BaseModel, Field


class PostSchema(BaseModel):
    """The post schema."""

    title: str = Field(description="The title of the social media post.")
    content: str = Field(description="The short and concise content of the post.")
    tags: list[str] = Field(
        description="The relevant tags of this post like hashtag we can use in social media."
    )


class OutputSchema(BaseModel):
    """Agent output schema"""

    posts: list[PostSchema] = Field(description="The list of social media post.")


AGENT_MODEL: LiteLlm = LiteLlm(model="openai/google/gemini-2.0-flash-exp:free")
AGENT_PROMPT: str = """
    You are a master of social media content creator with more than 5 years of experience. 
    Your task is to generate the number of short social media post about the topic provided by user.
    If post count or number of post not mention then create only one post.
    Keep it concise, relevant, easy to understand, and social media ready.
    Always response in json format.
    
    Output format:
    ```json 
    {
        'title': 'Discover the Power of Google Agent Development Kit (ADK)', 
        'content': 'Get started with AI development with Google's official ADK! 🚀', 
        'tags': ['#AI', '#ML', '#adk', '#google-adk', #ai-agent']
    }
    ```.
"""

root_agent = Agent(
    name="welcome_agent",
    description="A minimal agent that takes input and produces a simple output using LLM",
    model=AGENT_MODEL,
    instruction=AGENT_PROMPT,
    output_schema=OutputSchema,
    output_key="generate_post",
    generate_content_config=types.GenerateContentConfig(temperature=0.4),
)
