#a simulated server interface
class ServerInterface:
    def __init__(self):
        self.read = False

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
        if(self.read):
            return None
        else:
            self.read = True
            return [
                    {
                        "from":"friend1", 
                        "message":"message1"
                    },
                    {
                        "from":"friend2", 
                        "message":"message2"
                    }
                    ]

    def setStatus(self, status):
        return True

