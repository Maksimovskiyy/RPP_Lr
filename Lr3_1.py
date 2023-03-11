import http.client
import json
conn = http.client.HTTPConnection("167.172.172.227:8000")
conn.request('GET', '/number/2',)
x1 = conn.getresponse().read().decode()
x1_json = json.loads(x1)
print(x1_json['number'])