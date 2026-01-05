class Memory:
    def __init__(self):
        self.profile = {}
        self.history = []

    def update(self, key, value):
        if key in self.profile and self.profile[key] != value:
            return False
        self.profile[key] = value
        return True

    def log(self, text):
        self.history.append(text)
