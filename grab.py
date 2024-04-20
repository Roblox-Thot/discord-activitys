import http.client, json

#region Main discord
conn = http.client.HTTPSConnection("discord.com")

conn.request("GET", "/api/v9/applications/detectable")

res = conn.getresponse()
data = res.read()
jdata = json.loads(data.decode())
odata = json.dump(jdata,indent=4,fp=open("json/detectable.json",'w'))
#endregion

#region PTB discord
conn = http.client.HTTPSConnection("ptb.discord.com")

conn.request("GET", "/api/v9/applications/detectable")

res = conn.getresponse()
data = res.read()
jdata = json.loads(data.decode())
odata = json.dump(jdata,indent=4,fp=open("json/ptb detectable.json",'w'))
#endregion

#region Canary discord
conn = http.client.HTTPSConnection("canary.discord.com")

conn.request("GET", "/api/v9/applications/detectable")

res = conn.getresponse()
data = res.read()
jdata = json.loads(data.decode())
odata = json.dump(jdata,indent=4,fp=open("json/canary detectable.json",'w'))
#endregion