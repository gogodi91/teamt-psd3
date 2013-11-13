from User import *

class Student(User):
    
    #Constructor for a Student
    def __init__(self, fn, ln, guid):
        super().__init__(fn, ln)
        self.GUID = guid
        self.sessions = []
        
    #Assigns a session to the Student
    def addSession(self, s):
        self.sessions.append(s)
    
    #Removes a session from the Student
    def removeSession(self, s):
        self.sessions.remove(s)

    def sessionConflict(self):
        i = 1
        for s in self.sessions:
            if(s.conflicts(self.sessions[i:])):
                return True
            i++
        return False

        
