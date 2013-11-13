
class Session:
    #The basic Session
    #Lots of things incomplete

    #Constructor for a session
    def __init__(self, sd, ed, st, et, rec):
        self.startTime = d
        self.endTime = t
        self.tutor = None
        self.students = []

    #Adds a student to the seesion
    def addStudent(self, s):
        self.students.append(s)

    #Removes a student from the group
    def removeStudent(self, s):
        self.students.remove(s)

    #Adds a tutor to the session
    def addTutor(self, tr):
        self.tutor = tr
        self.tutor.addSession(self)

    #Removes a tutor from the session
    def removeTutor(self, tr):
        self.tutor = tr

    #Checks if a session is covered by a tutor
    def isCovered(self):
        if(self.tutor == ""):
            return False
        else:
            return True
