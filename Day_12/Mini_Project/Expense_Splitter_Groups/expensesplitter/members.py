class GroupMembers:
    def __init__(self):
        self.members = []

    def add_member(self, name):
        name = name.strip()
        if name in self.members:
            raise ValueError(f"Member '{name}' already exists.")
        self.members.append(name)

    def get_members(self):
        return self.members
