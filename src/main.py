#main.py
#Ally Weir - 1101682w
#13/11/13

#A basic menu to drive the project
#Yes I know its not finished

import os
os.system('cls' if os.name=='nt' else 'clear')

print("Welcome to the Undergraduate Booking System")
print("Enter the code for the option you want:")
print()
print("For all:")
print("l - Log In")
print("s - Sign Up")
print("lo - Log Out")
print("p - View profile")
print()
print("For Tutors, Staff or Admin:")
print("1 - Create a new session")
print("2 - Manually edit a session")
print("3 - Register attendence for session")
print("4 - Export data")
print("5 - Complete availability form")
print()
print("For Students:")
print("6 - Sign up for session")
print("7 - View attendence record")
print()
option = raw_input("Please enter your choice: ")