import http.client
import json
conn = http.client.HTTPConnection("167.172.172.227:8000")
conn.request('GET', '/number/?option=2',)
x2 = conn.getresponse().read().decode()
x2_json = json.loads(x2)
print(x2)