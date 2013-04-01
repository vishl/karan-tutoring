#a simulated server interface
class ServerInterface:
    def __init__(self):
        self.sent = True

    #connection always succeeds
    def connect(self, ip):
        return True

    #log in always 
    def logIn(self, username, password):
        return username=="user" and password=="password"

    def getUserList(self):
        return ["friend1", "friend2"]
    
    def sendMessage(self, message, recipientId):
        return True

    def checkForMessages(self):
        if(self.sent):
            return None
        else:
            return [{"friend1", ["message1"]}]

    def setStatus(self, status):
        return True

