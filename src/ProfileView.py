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

#Logged user session: tutor => profile view structure
def tutorView(tutor):
    print("Profile page: " tutor.firstName " " tutor.lastName)
    print("User type: tutor")
    print("classes given")
    print("Contact info")
    print("Office location")

#Logged user session: student => profile view structure
def studentView(student):
    print("Profile page: " student.firstName " " student.lastName)
    print("User type: student")
    print("classes taken")
    print("Attendance record")
    
