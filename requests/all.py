import requests

# get method
r = requests.get('https://api.github.com/events')

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('https://httpbin.org/get', params=payload)

# post method
r = requests.post('https://httpbin.org/post', data = {'key':'value'})

# put delete head options
r = requests.put('https://httpbin.org/put', data = {'key':'value'})
r = requests.delete('https://httpbin.org/delete')
r = requests.head('https://httpbin.org/get')
r = requests.options('https://httpbin.org/get')

# print URL
print(r.url)

# RESPONSE CONTENT
r = requests.get('https://api.github.com/events')
print(r.text)
print(r.encoding)

# BINARY RESPONSE CONTENT
print(r.content)

from PIL import Image
from io import BytesIO

i = Image.open(BytesIO(r.content))

## JSON RESPONSE CONTENT

r = requests.get('https://api.github.com/events')
r.json()
print(r.json())


## RAW
r = requests.get('https://api.github.com/events', stream=True)
r.raw
r.raw.read(10)

# В целом, однако, вы должны использовать такой шаблон для сохранения потоковой передачи в файл:

# with open(filename, 'wb') as fd:
#     for chunk in r.iter_content(chunk_size=128):
#         fd.write(chunk)


## CUSTOM HEADERS
url = 'https://api.github.com/some/endpoint'
headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get(url, headers=headers)

## POST data
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post("https://httpbin.org/post", data=payload)
print(r.text)

url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}
r = requests.post(url, data=json.dumps(payload))


## POST a Multipart-Encoded File
# >>> url = 'https://httpbin.org/post'
# >>> files = {'file': open('report.xls', 'rb')}
#
# >>> r = requests.post(url, files=files)
# >>> r.text
# {
#   ...
#   "files": {
#     "file": "<censored...binary...data>"
#   },
#   ...
# }
## CONTENT_TYPE
# files = {'file': ('report.xls', open('report.xls', 'rb'), 'application/vnd.ms-excel', {'Expires': '0'})}
# string as file
# files = {'file': ('report.csv', 'some,data,to,send\nanother,row,to,send\n')}

# STATUS CODE
r.status_code

## HEADERS
r.headers
# >>> r.headers['Content-Type']
# 'application/json'
#
# >>> r.headers.get('content-type')
# 'application/json'

## Cookies
r.cookies['example_cookie_name']

cookies = dict(cookies_are='working')
r = requests.get(url, cookies=cookies)

## Redirection and History
# >>> r.history
# [<Response [301]>]
# r = requests.get('http://github.com/', allow_redirects=False)


## TIMEOUT
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# requests.exceptions.Timeout: HTTPConnectionPool(host='github.com', port=80): Request timed out. (timeout=0.001)


