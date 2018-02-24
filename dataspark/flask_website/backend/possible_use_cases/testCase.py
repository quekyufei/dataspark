import json, ast
import requests
import base64
import datetime as dt
import time

consumerKey = "4xGO7wDdCta9g5nlX_NXUfbdWE8a"
consumerSecret = "jYtKEdtV9JlXw4lCimvwkrbtt1ca"

keySecret = (consumerKey + ":" + consumerSecret).encode('utf-8')
consumerKeySecretB64 = base64.b64encode(keySecret).decode('utf-8')
tokenResponse = requests.post("https://apistore.datasparkanalytics.com/token",
 data = { 'grant_type': 'client_credentials' },
 headers = { 'Authorization': 'Basic ' + consumerKeySecretB64 })
token = tokenResponse.json()['access_token']

contentType = "application/json"



n1 = dt.datetime.now()
print(n1)

subzoneDict = {}
with open("subzones.txt", "r") as file:
    for line in file:
        (key, val) = line.split('\t')
        subzoneDict[key] = val.replace("\n", "")

j = 1

for i in subzoneDict:

    print(j)
    j+=1

    if (j%75 == 0):
        time.sleep(10)

    queryBody = {
                  "date": "2017-05-29",
                  "timeSeriesReference": "destination",
                  "location": {
                    "locationType": "locationHierarchyLevel",
                    "levelType": "destination_planningarea",
                    "id": "OR"
                  },
                  "queryGranularity": {
                    "type": "period",
                    "period": "PT6H"
                  },
                  "filter": {

                    "type": "bound",
                    "dimension": "agent_year_of_birth",
                    "lower": 1980,
                    "upper": 2000
                  },
                  "dimensionFacets": [
                    "origin_subzone"
                  ],
                  "aggregations": [
                    {
                      "metric": "unique_agents",
                      "type": "hyperUnique"
                    }
                  ]
                }

    queryResponse = requests.post("https://apistore.datasparkanalytics.com:443/odmatrix/v3/query",
                                  data=json.dumps(queryBody),
                                  headers={'Authorization': "Bearer " + token,
                                             'Content-Type': contentType}
                                  )

    result = queryResponse.json()

    print(result)

print(dt.datetime.now() - n1)
