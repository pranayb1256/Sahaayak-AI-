APPOINTMENT_TOOL = {
    "type": "function",
    "function": {
        "name": "get_upcoming_appointments",
        "parameters": {
            "type": "object",
            "properties": {},
            "additionalProperties": False,
        },
    },
}

MEDICATION_TOOL = {
    "type": "function",
    "function": {
        "name": "get_medications",
        "parameters": {
            "type": "object",
            "properties": {},
            "additionalProperties": False,
        },
    },
}


TOOLS = [
    APPOINTMENT_TOOL,
    MEDICATION_TOOL,
]