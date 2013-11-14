"""
Gordon Adam (1107425a) and Peter Yordanov (1103620y)
14/11/2013

Class to include Tutors and Students
"""

class Users:
    
    #Constructor for a user
    def __init__(self, fn, ln):
        self.firstName = fn
        self.lastName = ln
		self.email = "user@hostname"

class Tutor(Users):
    
    #Constructor for a tutor
    def __init__(self, fn, ln):
        super().__init__(fn, ln)
        self.position = "Tutor"
        self.sessions = []
		self.phoneN = "-"
		self.office = "Building, room"

    #Assigns a session to the tutor
    def addSession(self, s):
        self.session.append(s)
        self.sessions[-1].addTutor(self)

    #Removes a session from the tutor
    def removeSession(self, s):
        self.session.remove(s)

    #Returns the number of Sessions Covered
    def sessionsCovered():
        return len(self.session)
		
	#Returns the sessions covered
    def sessionTimes():
		times = ""
		for session in self.sessions
			times+=session + "\n"
        return times
		
	#Returns the email address
    def emailAddress():
        return self.email
		
	#Returns phone number
    def phoneNumber():
        return self.phoneN
		
	#Returns the tutor's office
    def office():
        return self.office

    #Returns a String e.g "Scarlett Johanson"
    def __str__(self):
        return str(self.firstName) + " " + str(self.lastName)

class Student(Users):
    
    #Constructor for a Student
    def __init__(self, fn, ln, guid):
        super().__init__(fn, ln)
        self.position = "Student"
        self.GUID = guid
        self.sessions = []
		self.attendance = []
        
    #Assigns a session to the Student
    def addSession(self, s):
        if(not(self.sessionConflict(s))):
            self.sessions.append(s)
            self.sessions[-1].addStudent(self)
    
    #Removes a session from the Student
    def removeSession(self, s):
        self.sessions.remove(s)

    #Checks for conflicts in a new session with the rest of your registered sessions
    def sessionConflict(self, session):
        i = 0
        for s in self.sessions[i:]:
            if(session.conflicts(s)):
                return True
            i=i+1
        return False
	
	#Returns the email address
    def emailAddress():
        return self.email
		
	#Returns the number of sessions the student should be attending
    def sessionsTaken():
        return len(self.sessions)
		
	#Returns the total attendance
    def totalAttendance():
        return len(self.attendance)

    #Returns a String with the students GUID and there name e.g "Scarlett Johanson 1234567"
    def __str__(self):
        return str(self.firstName) + " " + str(self.lastName) + " " + str(self.GUID)
