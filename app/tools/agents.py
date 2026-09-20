import json

from app.llm_runner import chat_with_model
from app.tools.appointment import get_upcoming_appointments
from app.tools.medications import get_medications
from app.tools.definitions import TOOLS


SYSTEM_PROMPT = """
You are Sahaayak AI, an elderly-care coordinator for Indian families.

Rules:

1. Respond in English, Hindi, or Hinglish based on the user.
2. Never invent care information.
3. For appointment-related questions, use the appointment tool.
4. For medication-related questions, use the medication tool.
5. You may use multiple tools when the user asks multiple care-related questions.
6. Keep answers simple and easy for elderly users to understand.
7. You are not a doctor and must not diagnose medical conditions.

Available tools:

get_upcoming_appointments:
Use for doctor appointments, medical visits, dates, schedules, and upcoming consultations.

get_medications:
Use for medicines, dosage, medication schedules, and current medications.
"""


def run_agent(
    elder_id: int,
    user_message: str,
) -> str:

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT,
        },
        {
            "role": "user",
            "content": user_message,
        },
    ]

    first_response = chat_with_model(
        messages=messages,
        tools=TOOLS,
        tool_choice="auto",
    )

    assistant_message = first_response.choices[0].message

    messages.append(assistant_message)

    # No tool required.
    if not assistant_message.tool_calls:
        return assistant_message.content or ""

    for tool_call in assistant_message.tool_calls:

        tool_name = tool_call.function.name

        if tool_name == "get_upcoming_appointments":
            tool_result = get_upcoming_appointments(
                elder_id=elder_id
            )

        elif tool_name == "get_medications":
            tool_result = get_medications(
                elder_id=elder_id
            )

        else:
            tool_result = {
                "error": f"Unknown tool: {tool_name}"
            }

        messages.append(
            {
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": json.dumps(tool_result),
            }
        )

    final_response = chat_with_model(
        messages=messages,
        tools=TOOLS,
    )

    return final_response.choices[0].message.content or ""