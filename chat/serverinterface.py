
#a dummy server interface
class ServerInterface:
    def __init__(self):
        pass

    #connection always fails
    def connect(self, ip):
        return False

    #log in always fails
    def logIn(self, username, password):
        return False

    def getUserList(self):
        return None
    
    def sendMessage(self, message, recipientId):
        return False

    def checkForMessages(self):
        return None

