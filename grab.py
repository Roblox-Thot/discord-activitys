import http.client, json

conn = http.client.HTTPSConnection("ptb.discord.com")

conn.request("GET", "/api/v9/applications/detectable")

res = conn.getresponse()
data = res.read()
jdata = json.loads(data.decode())
odata = json.dump(jdata,indent=4,fp=open("detectable.json",'w'))