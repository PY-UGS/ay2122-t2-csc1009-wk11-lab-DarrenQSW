class clockTime:

    # Constructor
    # Initializes the attributes to 0
    def __init__(self):
        self.hours = 0
        self.minutes = 0
        self.seconds = 0

    # Asks the user for the number of hours
    # Checks if number of hours is 0 - 23
    # Sets the hours attribute
    def setHours(self):
        self.hours = int(input("Please enter the number of hours from 0 to 23: "))
        # Asks user to re-enter if hours is invalid
        while (self.hours < 0 or self.hours > 23):
            print("Invalid input! Hours only from 0 to 23.")
            self.hours = int(input("Please enter the number of hours from 0 to 23: "))

    # Asks the user for the number of minutes
    # Checks if number of minutes is 0 - 59
    # Sets the minutes attribute
    def setMinutes(self):
        self.minutes = int(input("Please enter the number of minutes from 0 to 59: "))
        # Asks user to re-enter if minutes is invalid
        while (self.minutes < 0 or self.minutes > 59):
            print("Invalid input! Minutes only from 0 to 59.")
            self.minutes = int(input("Please enter the number of minutes from 0 to 59: "))

    # Asks the user for the number of seconds
    # Checks if number of seconds is 0 - 59
    # Sets the seconds attribute
    def setSeconds(self):
        self.seconds = int(input("Please enter the number of seconds from 0 to 59: "))
        # Asks user to re-enter if seconds is invalid
        while (self.seconds < 0 or self.seconds > 59):
            print("Invalid input! Seconds only from 0 to 59.")
            self.seconds = int(input("Please enter the number of seconds from 0 to 59: "))

    # Calls the above functions
    def setTime(self):
        self.setHours()
        self.setMinutes()
        self.setSeconds()

    # Prints the time in hours:minutes:seconds format
    def showTime(self):
        print("Time: {:02d}:{:02d}:{:02d}".format(self.hours, self.minutes, self.seconds))

# Creates clockTime object
cTime = clockTime()
# Sets the time
cTime.setTime()
# Prints the time
cTime.showTime()