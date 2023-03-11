# задание 1
import http.client
import json
conn = http.client.HTTPConnection("167.172.172.227:8000")
conn.request('GET', '/number/2',)
x1 = conn.getresponse().read().decode()
x1_json = json.loads(x1)
print(x1_json['number'])
conn.request('GET', '/number/?option=2',)
# задание 2
x2 = conn.getresponse().read().decode()
x2_json = json.loads(x2)
print(x2)
res = x2_json['number']//x1_json['number']
print(res)
# задание 3
headers = {'Content-type': 'application/x-www-form-urlencoded'}
conn.request('POST', '/number/', 'option=2', headers)
x3 = conn.getresponse().read().decode()
x3_json = json.loads(x3)
print(x3)
res2 = x3_json['number'] * x2_json['number']
print(res2)
# задание 4
headers = {'Content-type': 'application/json'}
conn.request('PUT', '/number/', '{"option":2}', headers)
x4 = conn.getresponse().read().decode()
x4_json = json.loads(x4)
print(x4_json)
res3 = x4_json['number'] + x3_json['number']
print(res3)
# задание 5
conn.request('DELETE', '/number/', '{"option":2}',)
x5 = conn.getresponse().read().decode()
x5_json = json.loads(x5)
print(x5_json)
res4 = x4_json['number'] - x5_json['number']
print(res4)