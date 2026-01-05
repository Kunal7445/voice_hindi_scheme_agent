def apply_for_scheme(profile, scheme):
    required = ["age", "income", "state"]

    for r in required:
        if r not in profile:
            return False, f"{r} missing"

    return True, "आवेदन सफल रहा"
