#Creted By Ferhat Guneri
#Mail: guneriferhat21@gmail.com

# -*- coding: utf-8 -*-
import json
import base64
import requests


vropspass = "Base64EncodedPassword="
AlertID="YourAlertID"
url = "https://YourServer/suite-api/api/auth/token/acquire"
data = {"username": "admin", "password": base64.b64decode(vropspass)}
headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
r = requests.post(url, json=data, headers=headers, verify=False)
r = r.json()
r = json.dumps(r)
r = json.loads(r)
token = r.get("token")
token = "vRealizeOpsToken " + token

AlertURL = "https://YourServer/suite-api/api/alerts/"+str(AlertID)
headers = {'Content-type': 'application/json', 'Accept': 'application/json', 'Authorization': token}
res = requests.get(AlertURL, headers=headers, verify=False)
res = res.json()
res = json.dumps(res)
res = json.loads(res)
alertDefinitionId = res.get("alertDefinitionId")


DefinitionURL = "https://YourServer/suite-api/api/alertdefinitions/" + str(alertDefinitionId)
headers = {'Content-type': 'application/json', 'Accept': 'application/json', 'Authorization': token}
rest = requests.get(DefinitionURL, headers=headers, verify=False)
rest = rest.json()
rest = json.dumps(rest)
rest = json.loads(rest)

description =""
for myvalue in rest["states"]:
    for mysubvalue in myvalue["recommendationPriorityMap"]:
        RecommendationURL = "https://YourServer/suite-api/api/recommendations/"+str(mysubvalue)
        headers = {'Content-type': 'application/json', 'Accept': 'application/json', 'Authorization': token}
        r = requests.get(RecommendationURL, headers=headers, verify=False)
        r = r.json()
        r = json.dumps(r)
        r = json.loads(r)
        description += r.get("description")
        description +="\n"
print description
