import uuid
from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.sessions.in_memory_session_service import InMemorySessionService
from google.adk.runners import Runner
from google.genai import types

from prompt import INFORMATION_AGENT_INSTRUCTION
from models import StateOutput

load_dotenv()


print("🚀 Initializing LLM Model...")
model = LiteLlm(model="openai/google/gemini-2.0-flash-exp:free")

print("⚙️ Creating Information Agent...")
agent = Agent(
    name="information_agent",
    description="You are a helpful information agent.",
    model=model,
    instruction=INFORMATION_AGENT_INSTRUCTION,
    output_schema=StateOutput,
    output_key="state",
)

print("📅 Initializing In-Memory Service ...")
service = InMemorySessionService()
session_id = str(uuid.uuid4())
app_name = "InformationApp"
user_id = "deyrahul95"

print("➕ Create Initial State into Session")
service.create_session_sync(
    app_name=app_name,
    user_id=user_id,
    session_id=session_id,
    state={"name": "Rahul Dey", "fav_color": "black", "fav_subject": "Mathematics"},
)

print("🤖 Initializing Runner...")
runner = Runner(agent=agent, session_service=service, app_name=app_name)

msg = types.Content(
    role="user",
    parts=[
        types.Part(
            text="Please change my favourite color to 'Blue' and my favourite subject to 'Computer Science'"
        )
    ],
)

print("🧑‍💻 Running the Agent ....")
for ev in runner.run(user_id=user_id, session_id=session_id, new_message=msg):
    if ev.is_final_response() and ev.content and ev.content.parts:
        raw = ev.content.parts[0].text
        print(raw, "\n")
        print("➖" * 50)

print("✅ Retrieving Updated State")
session = service.get_session_sync(
    app_name=app_name, user_id=user_id, session_id=session_id
)

if session is not None and "state" in session.state:
    structure_data = session.state["state"]
    print("☑️ Updating Session State...")

    for key, value in structure_data.items():
        session.state[key] = value
        print(f" - {key} updated to : {value} ")

    del session.state["state"]
else:
    print("🙅 No structured output found in session data.")

print("\n 🧊 Final Session State: ")
for key, value in session.state.items() if session is not None else []:
    print(f"{key}: {value}")
