from User import *

class Tutor(User):
    
    #Constructor for a tutor
    def __init__(self, fn, ln):
        super().__init__(fn, ln)
        self.session = []

    #Assigns a session to the tutor
    def addSession(self, s):
        self.session.append(s)

    #Removes a session from the tutor
    def removeSession(self, s):
        self.session.remove(s)

    def sessionsCovered():
        return len(self.session)


