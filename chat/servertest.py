import urllib

params = {}

#params['user'] = 'user1'
#params['password'] = 'password'

params['senderId'] = 'user1'
params['recipientId'] = 'user2'
params['message'] = 'hello'

paramsEnc = urllib.urlencode(params)
#print params
#f = urllib.urlopen("http://localhost:8000/sendmessage", paramsEnc)
#print f.read()

params = {}
params['recipientId'] = 'user1'

paramsEnc = urllib.urlencode(params)

print "checked messages"
f = urllib.urlopen("http://localhost:8000/checkmessages", paramsEnc)
print f.read()

print "checked messages"
f = urllib.urlopen("http://localhost:8000/checkmessages", paramsEnc)
print f.read()
