# ProfileView.py
# Peter Yordanov - 1103620y
# 14/11/13

# Subsection of PSD3 Team Project - Undergraduate Booking System.

# Presents the user with account information after login
# >> Tutor - sees classes that is tutoring, contact information (email, phone number, office, ..), (profile image)
# >> Student - sees attendance record, classes taken , etc


#Check if the session logged user is that of a tutor or a student
def profileView(user):
    
    if(user.position == "Tutor"):
        tutorView(user)
    elif(user.position == "Student"):
        studentView(user)

#Logged user: tutor => profile view structure
def tutorView(tutor):
    print("User name: " __str__(tutor))
    print("User type: tutor")
    
    print("Sessions covered" tutor.sessionsCovered())

    
    print("Contact information:")
    print(">> Email address: " tutor.emailAddress())
    print(">> Phone number: " tutor.phoneN())
    print(">> Office location: " tutor.office())

#Logged user: student => profile view structure
def studentView(student):
    print("User ID and name: " student.firstName " " student.lastName)
    print("User type: student")
    print("Classes taken:")

    sC = student.sessions()
    sA = student.totalAttendance()
    absentN = sC - sA
    print("Attendance record: absent from " absentN " classes")
    print(">> Total sessions: " sC)
    print(">> Total attendance: " sTA)

    print("Contact information:")
    print(">> Email address: " student.emailAddress())
    
