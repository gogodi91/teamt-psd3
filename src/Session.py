class Session:
    """The basic Session"""

    def __init__(self, sd, ed, d, t):
        self.startDate = sd
        self.endDate = ed
        self.day = d
        self.time = t
        self.tutor = ""
        self.students = []

    def addStudent(self, s):
        self.students.append(s)

    def addTutor(self, tr):
        self.tutor = tr

