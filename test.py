import requests
r = requests.get('http://google.com')
print r.status_code
print r.headers
print r.text[0:1000]

url = 'http://localhost:8888/scale/'
myobj = {'mass': 'somevalue'}
x = requests.post(url, data = myobj)
print x.text 