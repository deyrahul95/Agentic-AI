from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

from task_tracker_agent.prompt import TASK_AGENT_PROMPT
from task_tracker_agent.tools import add_task, read_tasks, update_task, delete_task, init_sheet


OLLAMA_MODEL = LiteLlm(model="ollama_chat/qwen3:1.7b")

init_sheet()

root_agent = Agent(
    name="task_tracker_agent",
    description="A smart task tracker that manages a local task list in an Excel file.",
    model=OLLAMA_MODEL,
    instruction=TASK_AGENT_PROMPT,
    tools=[add_task, read_tasks, update_task, delete_task],
)
