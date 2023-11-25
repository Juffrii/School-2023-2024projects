class Reaction:
    def __init__(self, compounds: str, result: str, ion: bool, is_char: bool):
        self.compound = compounds
        self.result = result
        self.ion = ion
        self.is_char = is_char