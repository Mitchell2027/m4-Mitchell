class SetFull(Exception):
    pass


class MemoryBank:
    def __init__(self):
        self.members = []

    def add_problem(self, problem_id):
        if problem_id in self.members:
            return
        if len(self.members) >= 10:
            raise SetFull
        self.members.append(problem_id)
