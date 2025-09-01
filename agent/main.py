"""A simple agent using OpenAI's gpt-oss 120b model from Cerebras via Hugging Face by utilizing the Agents SDK."""

import asyncio
import os
from datetime import datetime

from agents import (
    Agent,
    OpenAIChatCompletionsModel,
    Runner,
    function_tool,
    set_tracing_disabled,
)
from dotenv import load_dotenv
from openai import AsyncOpenAI

load_dotenv()
set_tracing_disabled(True)


@function_tool
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


@function_tool
def get_time() -> str:
    """
    Get the current time.

    Returns:
        str: The current time in HH:MM format.
    """
    print("[debug] get_time called")
    return datetime.now().strftime("%H:%M")


async def main():
    """
    The main function to run the agent.
    """
    agent = Agent(
        name="Hello world",
        instructions="You are a helpful agent.",
        model=OpenAIChatCompletionsModel(
            model="openai/gpt-oss-120b:cerebras",
            openai_client=AsyncOpenAI(
                base_url=os.environ["CEREBRAS_URL"],
                api_key=os.environ["CEREBRAS_API_KEY"],
            ),
        ),
        tools=[calculate_sum, get_time],
    )
    result = await Runner.run(
        agent, input="What is the current time and weather in Skopje?"
    )
    print(result)
    print("\n___________ONLY_THE_FINAL_OUTPUT____________\n")
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
