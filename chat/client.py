from serverinterface import *
print "Welcome to KChat!"
print "...It doesn't do much yet"

serverInterface = ServerInterface()

#get the person's login information
login = False
while login == False:
    
    username = raw_input("What is your username? ")
    password = raw_input("what is your password? ")

#connect to the server
    login = serverInterface.logIn(username,password)
    if login == False:
        print "Invalid username or password. Try again."


#have them type a message
#check the server for messages

