from serverinterfacehttp import *
import sys
print "Welcome to KChat!"
print "...It doesn't do much yet"
if len(sys.argv) == 2:
    host = sys.argv[1]
else:
    host ="localhost"
print "host is", host
serverInterface = ServerInterface()
serverInterface.connect(host+":8000")
#get the person's login information
login = False
while login == False:
    
    username = raw_input("What is your username? ")
    password = raw_input("what is your password? ")

#connect to the server
    login = serverInterface.logIn(username,password)
    if login == False:
        print "Invalid username or password. Try again."

serverInterface.setStatus('online')
print "You are logged in as",username

cfm = serverInterface.checkForMessages(username)
n=len(cfm)
print "You have %i unread messages"%(n)
while True:
    m = raw_input("Would you like to see the messages or create amessage? Type c to check messages or n to create a message. Type q to quit. ")

    if m=='c':
    
        cfm+=serverInterface.checkForMessages(username)
        for message in cfm:

            print message["from"]
            print message["message"]
            
            reply = raw_input("Would you like to reply to this message? Type yes or no ")
            if reply == 'yes':
                replymessage = raw_input('Type your message here: ')
                sendmessage = serverInterface.sendMessage(replymessage,message["from"],username)
                print "Your message has been sent."
        cfm = []
    if m=='n':
        sendid = raw_input("Type the username of the person you would like to send a message. ")
        sendm = raw_input("Type your message. ")
        sendmessage = serverInterface.sendMessage(sendm,sendid,username)
        print "Your message has been sent."
   
    if m == 'q':
       print "Goodbye Come back soon." 
       break

#check the server for messages

