import sys
import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler

class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if(self.path=="/"):
            self.wfile.write("root")
        elif(self.path=="/login"):
            self.valid()
            self.login()
        else:
            self.invalid()
            self.wfile.write("Path = " + self.path)

    def valid(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
    def invalid(self):
        self.send_response(400)
        self.send_header('Content-type','text/html')
        self.end_headers()

    def login(self):
        print self.headers

class DataManager():
    def __init__(self):
        self.users = None
        self.userFile = "users.csv"
        pass

    def getUsers(self):
        if(self.users == None):
            self.users = self.loadUsersFromFile()
        print "Got ", len(self.users.keys()), "users"
        return self.users

    def loadUsersFromFile(self):
        f = open(self.userFile, "r")
        lines = f.readlines()
        users = {}
        for i in range(len(lines)):
            (user, password) = lines[i].strip().split(',')
            users[user] = password
        return users



#Setup
#HandlerClass = SimpleHTTPRequestHandler
HandlerClass = Handler
ServerClass  = BaseHTTPServer.HTTPServer
Protocol     = "HTTP/1.0"
dataManager = DataManager()

if sys.argv[1:]:
    port = int(sys.argv[1])
else:
    port = 8000
server_address = ('127.0.0.1', port)

#load data
users = dataManager.getUsers()

#Create http server
HandlerClass.protocol_version = Protocol
httpd = ServerClass(server_address, HandlerClass)

sa = httpd.socket.getsockname()
print "Serving HTTP on", sa[0], "port", sa[1], "..."
httpd.serve_forever()
