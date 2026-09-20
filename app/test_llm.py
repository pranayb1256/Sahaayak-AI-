


response = client.chat.completions.create(
    model=MODEL_NAME,
    messages=[
        {
            "role": "system",
            "content": (
                "You are Sahaayak AI, an elderly-care coordinator "
                "for Indian families. "
                "You communicate clearly, politely, and naturally "
                "in English, Hindi, or Hinglish."
            ),
        },
        {
            "role": "user",
            "content": (
                "Namaste. Meri mummy ko kal doctor ke paas jaana hai. "
                "Unse Hinglish mein politely baat karo."
            ),
        },
    ],
)

print(response.choices[0].message.content)