import urllib
import json

class ServerInterface:
    def __init__(self):
        self.read = False

    #connection always succeeds
    def connect(self, ip):
        self.ip = ip
        return True

    #log in always 
        if f.read()=='success':
            return True
        else:
            return False
    def logIn(self, username, password):
        
        params = {}

        params['user'] = username
        params['password'] =password

        params = urllib.urlencode(params)
        
        f = urllib.urlopen("http://"+self.ip+"/login", params)
        status = f.read()
        print status
        if status == 'success':     
            return True
        else:
            
            return False
    
    def getUserList(self):
        f=urllib.urlopen("http://"+self.ip+"/friends")

        data = f.read()
        return json.loads(data)
    
    def sendMessage(self, message, recipientId, senderId):
        params = {}

        params['message']= message
        params['recipientId']=recipientId
        params['senderId']=senderId

        params = urllib.urlencode(params)

        f=urllib.urlopen("http://"+self.ip+"/sendmessage", params)

        if f.read()=='success':
            return True
        else:
            return False

    def checkForMessages(self,recipientId):
      
        params = {}

        params['recipientId']=recipientId

        params = urllib.urlencode(params)


        f=urllib.urlopen("http://"+self.ip+"/checkmessage", params)
      
        data = f.read()
        return json.loads(data)


    def setStatus(self, status):
        return True

