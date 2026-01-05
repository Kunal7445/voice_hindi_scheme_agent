def plan(user_text, memory):
    required_fields = ["age", "income", "state", "gender"]

    for field in required_fields:
        if field not in memory.profile:
            return f"ASK_{field.upper()}"

    return "CHECK_ELIGIBILITY"
