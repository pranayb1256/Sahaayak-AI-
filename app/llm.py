import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")

if not api_key:
    raise RuntimeError(
        "OPENROUTER_API_KEY is not set."
    )


client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)


MODEL_NAMES = [
    "openrouter/free",
    "qwen/qwen3-32b:free",
    "qwen/qwen3-8b:free",
]