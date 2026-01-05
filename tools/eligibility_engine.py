def check_eligibility(profile):
    schemes = []

    if profile["income"] < 200000:
        schemes.append("प्रधानमंत्री जन धन योजना")

    if profile["gender"] == "महिला":
        schemes.append("सुकन्या समृद्धि योजना")

    return schemes
