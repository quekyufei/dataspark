import definequerybody
import json, ast
import requests
import base64
import datetime as dt
from datetime import timedelta
import time
from apiconnnection import APIConnection as Conn

def discreteVisit(filterdict):
    n1 = dt.datetime.now()
    yestDate = n1 - timedelta(days=2)
    dateQuery = str(yestDate.year) + "-" + str(yestDate.month) + "-" + str(yestDate.day)

    subzoneDict = {}
    with open("Subzones.txt", "r") as file:
        for line in file:
            (key, val) = line.split('\t')
            subzoneDict[key] = val.replace("\n", "")

    no = 1
    rankingList = []
    for i in subzoneDict:
        if (no%75 == 0):
            time.sleep(60)

        queryBody = {
            "date": dateQuery,
            "location": {
                "locationType": "locationHierarchyLevel",
                "levelType": "discrete_visit_subzone",
                "id": i
            },
            "queryGranularity": {
                "type": "period",
                "period": "P1D"
            },
            "aggregations": [
                {
                    "metric": "unique_agents",
                    "type": "hyperUnique"
                }
            ]
        }

        # dicttemp = {"gender": "NA", "age": [1990, 1995], "race": "NA", "nationality": "NA"}

        queryBody.update(definequerybody.main_filter_thing(filterdict))


        queryResponse = requests.post("https://apistore.datasparkanalytics.com:443/discretevisit/v2/query",
                                      data=json.dumps(queryBody),
                                      headers={'Authorization': "Bearer " + Conn.token,
                                                 'Content-Type': Conn.contentType}
                                      )

        result = queryResponse.json()
        if len(result) != 0:
            result = result[0]
            print(result)
            rankingList.append(result)
        no += 1

    ranked = sorted(rankingList, key=lambda k:k['event']['hyperUnique_unique_agents'], reverse=True)
    print("RANKED:", ranked)
