############################
# Author: Keir 'Kaffo' Smith
############################

class Users:

    #Constructor for a user list
    def __init__(self):
        self.list = {}

    def addUser(user):
        self.list[user.GUID] = user;

    def removeUser(guid):
        del self.list[guid];

    def getUser(guid):
        return self.list[guid];

#what ever else I can think of
