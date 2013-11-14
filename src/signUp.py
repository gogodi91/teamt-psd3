"""
Gordon Adam
1107425
14/11/2013

Session Sign Up part of PSD3 Project
"""
sessionTimes = []

#First function checks user type to judge which options to give
def signUp(user):
    if(user.position == "Tutor"):
        tutorOptions(user)
    elif(user.position == "Student"):
        studentOptions(user)

#if user is tutor these options are given (don't know why i'm explaining this!)
def tutorOptions(tutor):
    print("What would you like to do:\n")
    print("1: List Uncovered Sessions")
    print("2: List Number of Sessions covered by each Tutor")
    print("3: Sign up for a session")
    print("4: Remove yourself from a session\n")
    option = raw_input(">>> ")

    if(option == "1"):
        listFreeSessions()
    elif(option == "2"):
        listNumSessionCovered()
    elif(option == "3"):
        tutorSignUp(tutor)
    elif(option == "4"):
        tutorRemove(tutor)

#and here is the other options
def studentOptions(student):
    print("What would you like to do:\n")
    print("1: List Tutorial Sessions")
    print("2: Sign up to Session")
    option = raw_input(">>> ")

    if(option == "1"):
        listSessions()
    elif(option == "2"):
        studentSignUp(student)

#lists all the registered sessions
def listSessions():
    i = 0
    for st in sessionTimes:
        i += 1
        print(i + ": " + str(st))

#list all the registered sessions that are not covered by a tutor
def listFreeSessions():
    i = 0
    for st in sessionTimes:
        i += 1
        if(not(st.isCovered())):
            print(i + ": " + str(st))

#Signs a student up to a course
def studentSignUp(student):
    option = raw_input("Please enter the num of the session you would like: ")
    student.addSession(sessionTimes[option-1])

#Signs a tutor up to a course
def tutorSignUp(tutor):
    option = raw_input("Please enter the num of the session you would like: ")    
    tutor.addSession(sessionTimes[option-1])

"""
******************IGNORE ME*******************
def loadData():
   temp = []
    with open('sessionTimes.txt') as inputfile:
        for line in inputfile:
            temp.append(line)
    for st in temp:
        sessionDate = date(int(st[0:4]), int(st[5:7]), int(st[8:10]))
        startTime = time(int(st[11:13]), int(st[14:16]), int(st[17:19]))
        endTime = time(int(st[20:22]), int(st[23:25]), int(st[26:28]))
        session = Session(sessionDate, startTime, endTime, (st[29:30] == "1"))
        sessionTimes.append(session)     
**********************************************
"""
