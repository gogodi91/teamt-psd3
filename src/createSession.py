# createSession.py
# Ally Weir - 1101682w
# 13/11/13

# Subsection of PSD3 Team Project - Undergraduate Booking System.

# Handles the creation of new teaching sessions, defining them
# and then adding them to the system as a class students with
# permission can join.

import time
from datetime import date

def main():


def validation(user):
		if user.type == "tutor" || user.type == "admin" || user.type == "staff":
			return True
		else:
			return False

def createSession():
	date = raw_input("Date of first session? (DD/MM/YY): ")
	startTime = raw_input("Start time of session(s)? (Format example: 1400): ")
	endTime = raw_input("End time of session(s)? (Same format): ")
	location = raw_input("Where do you want to hold it? (Building Name/Room Number): ")
	recurrence = raw_input("Is this a *single*, *weekly*, *monthly* or *bi-monthly* session? :")
	endDate = "00/00/00"
	if recurrence == "monthly" || recurrence == "bi-monthly":
		endDate = raw_input("What is the date of your last session? (DD/MM/YY): ")
	if isAvailable(date, satrtTime, endTime, location, recurrence, endDate): #isAvailable will handle new class if false
		print ("Those dates are available in that location.")
		sessionType = raw_input("What kind of session do you want to create?: ")
		sessionTitle = raw_input("What is the session's title? :")
		sessionDescription = raw_input("Briefly describe the session")
		#SUCCINCT WAY TO PRINT OUT CLASS DETAILS (STILL TO CREATE CLASS OBJECT)

		if classIsCorrect(): #will handle if false
			#STORE IN DATABASE
			return

def isAvailable(date, startTime, endTime, location, recurence):
	date = time.strptime(date, "%d/%m/%y")
	startTime = time.strptime(startTime, "%H %M")
	endTime = time.strptime(endTime, "%H %M")
	if endDate != "00/00/00":
		endDate = time.strptime(endDate, "%d/%m/%y")

	getArrayOfClassDates(date, recurrence, endDate)


def getArrayOfClassDates(date, recurrence, endDate):
	classDates = [date]
	if endDate == "00/00/00":
		return classDates
	else:
		for single_date in daterange(start_date, end_date):
    		classDates = classDates + single_date
    	return classDates

#pulled from http://stackoverflow.com/questions/1060279/iterating-through-a-range-of-dates-in-python
def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

