import urllib

params = {}

#params['user'] = 'user1'
#params['password'] = 'password'

params['senderId'] = 'user1'
params['recipienId'] = 'user2'
params['message'] = 'hello'

params = urllib.urlencode(params)
print params
f = urllib.urlopen("http://localhost:8000/sendmessage", params)
print f.read()
