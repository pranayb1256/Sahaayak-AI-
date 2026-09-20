from openai import APIError, RateLimitError

from app.llm import client, MODEL_NAMES


def chat_with_model(
    *,
    messages: list,
    tools: list | None = None,
    tool_choice: str | None = None,
):
    last_error = None

    for model in MODEL_NAMES:

        try:

            request = {
                "model": model,
                "messages": messages,
            }

            if tools is not None:
                request["tools"] = tools

            if tool_choice is not None:
                request["tool_choice"] = tool_choice

            response = client.chat.completions.create(
                **request
            )

            actual_model = getattr(
                response,
                "model",
                model,
            )

            print(
                f"[Sahaayak] Model used: {actual_model}"
            )

            return response

        except (RateLimitError, APIError) as exc:

            print(
                f"[Sahaayak] Model failed: {model}"
            )

            print(
                f"[Sahaayak] Reason: {exc}"
            )

            last_error = exc

    raise RuntimeError(
        "All configured OpenRouter models failed."
    ) from last_error