"""A simple agent using OpenAI's gpt-oss 120b model from Cerebras via Hugging Face by utilizing the Google ADK."""

import asyncio
import os
from datetime import datetime

from dotenv import load_dotenv
from google.adk.agents.llm_agent import LlmAgent
from google.adk.models.lite_llm import LiteLlm
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

load_dotenv()

APP_NAME = "weather_app"
USER_ID = "1234"
SESSION_ID = "session1234"


def calculate_sum(a: int, b: int) -> int:
    """
    Calculate the sum of two integers.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The sum of the two integers.
    """
    print("[debug] calculate_sum called")
    return a + b


def get_time(format_type: str) -> str:
    """
    Get the current time.

    Args:
        format_type (str): The time format to return. Use "HH:MM" for basic format
            or "HH:MM:SS" for format with seconds.

    Returns:
        str: The current time in the specified format.
    """
    print("[debug] get_time called")
    if format_type == "HH:MM":
        return datetime.now().strftime("%H:%M")
    elif format_type == "HH:MM:SS":
        return datetime.now().strftime("%H:%M:%S")
    else:
        return datetime.now().strftime("%H:%M")


async def main():
    """
    The main function to run the agent.
    """
    agent = LlmAgent(
        name="Hello_world",
        instruction="You are a helpful agent.",
        model=LiteLlm(
            model="huggingface/openai/gpt-oss-120b",
            api_key=os.environ["HF_TOKEN"],
        ),
        tools=[calculate_sum, get_time],
    )

    session_service = InMemorySessionService()
    await session_service.create_session(
        app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID
    )
    runner = Runner(agent=agent, app_name=APP_NAME, session_service=session_service)
    content = types.Content(
        role="user",
        parts=[types.Part(text="What is the current time and calculate what is 2+2?")],
    )
    events = runner.run(user_id=USER_ID, session_id=SESSION_ID, new_message=content)

    for event in events:
        print(f"\nDEBUG EVENT: {event}\n")
        if event.is_final_response() and event.content:
            final_answer = event.content.parts[0].text.strip()
            print("\n🟢 FINAL ANSWER\n", final_answer, "\n")


if __name__ == "__main__":
    asyncio.run(main())
