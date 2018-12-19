# -*- coding: utf-8 -*-
import requests
import json

url = "https://SunucuIP/suite-api/api/auth/token/acquire"
data = {"username":"KullaniciAdi","password":"Sifre"}
headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
r = requests.post(url, json=data, headers=headers, verify=False)
r = r.json()
r = json.dumps(r)
r = json.loads(r)
token = r.get("token")

token = "vRealizeOpsToken "+token
print token

url = "https://SunucuIP/suite-api/api/resources?resourceKind=virtualmachine"
headers = {'Content-type': 'application/json', 'Accept': 'application/json', 'Authorization': token}
r = requests.get(url, headers=headers, verify=False)
r = r.json()
for item in r["resourceList"]:
    identifier = item["identifier"]
    print identifier
    print item["resourceKey"]["name"]

    url = "https://SunucuIP/suite-api/api/resources/"+identifier+"/properties"
    headers = {'Content-type': 'application/json', 'Accept': 'application/json', 'Authorization': token}
    req = requests.get(url, headers=headers, verify=False)
    req = req.json()
    for item in req["property"]:
        name = item["name"]
        value = item["value"]
