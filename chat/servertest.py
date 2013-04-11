import urllib

params = {}

params['user'] = 'user1'
params['password'] = 'password'

params = urllib.urlencode(params)
print params
f = urllib.urlopen("http://localhost:8000/login", params)
print f.read()
