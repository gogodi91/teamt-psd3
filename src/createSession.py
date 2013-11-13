# createSession.py
# Ally Weir - 1101682w
# 13/11/13

# Subsection of PSD3 Team Project - Undergraduate Booking System.

# Handles the creation of new teaching sessions, defining them
# and then adding them to the system as a class students with
# permission can join.

def main():


def validation(user):
		if user.type == "tutor" | user.type == "admin" | user.type == "staff":
			return True
		else:
			return False

def createSession():
	sessionType = raw_input("What kind of session do you want to create?: ")
	date = raw_input("Date of first session? (DD/MM/YY): ")
	location = raw_input("Where do you want to hold it? (Building Name/Room Number): ")
	recurrence = raw_input("Is this a *single*, *weekly*, *monthly* or *bi-monthly* session? :")
	if isAvailable(date, location, recurrence): #isAvailable will handle new class if false
		print ("Those dates are available in that location.")
		sessionTitle = raw_input("What is the session's title? :")
		sessionDescription = raw_input("Briefly describe the session")
		#SUCCINCT WAY TO PRINT OUT CLASS DETAILS (STILL TO CREATE CLASS OBJECT)

		if classIsCorrect(): #will handle if false
			#STORE IN DATABASE
			return

