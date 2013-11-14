"""
Gordon Adam
1107425
14/11/2013

Class for a single Session
"""
class Session:

    #Constructor for a session
    def __init__(self, sd, st, et):
        self.sessionDate = sd
        self.startTime = st
        self.endTime = et
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
    def conflicts(self, s):
        if(self.sessionDate == s.sessionDate):
            if(((self.startTime >= s.startTime) and (self.startTime <= s.endTime)) or ((self.endTime >= s.startTime) and (self.endTime <= s.endTime))):
                return True
        else:
            return False

    def __str__(self):
        return str(self.sessionDate) + " " +  str(self.startTime) + " " +  str(self.endTime)
