from tools.eligibility_engine import check_eligibility

def execute(action, memory):
    if action == "CHECK_ELIGIBILITY":
        return check_eligibility(memory.profile)
