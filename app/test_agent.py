from app.tools.agents import run_agent


response = run_agent(
    elder_id=1,
    user_message=(
        "Mummy ki doctor appointment kab hai "
        "aur unki medicines kaunsi hain?"
    ),
)
print("\nSahaayak:")
print(response)