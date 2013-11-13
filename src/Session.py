
class Session:
    #The basic Session
    #Lots of things incomplete

    #Constructor for a session
    def __init__(self, sd, st, et):
        self.sessionDate = sd
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
    
    #Checks for a conflict between two sessions
    def conflicts(self, session):
        if(self.sessionDate == s.sessionDate):
            if(((self.startTime > s.startTime) && (self.startTime < s.endTime)) || ((self.endTime > s.startTime) && (self.endTime < s.endTime))):
                return True
        else:
            return False
