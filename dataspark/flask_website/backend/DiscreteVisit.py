import definequerybody
import json, ast
import requests
import base64
import datetime as dt
from datetime import timedelta
import time
from apiconnnection import APIConnection as Conn
import createheatmap

def discreteVisit(filterdict):
    n1 = dt.datetime.now()
    yestDate = n1 - timedelta(days=2)
    dateQuery = str(yestDate.year) + "-" + str(yestDate.month) + "-" + str(yestDate.day)

    subzoneDict = {}
    with open("Subzones1.txt", "r") as file:
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

        if definequerybody.main_filter_thing_DV(filterdict) is not None:
            queryBody.update(definequerybody.main_filter_thing_DV(filterdict))


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
    createHeat(ranked)
    return createTopList(ranked)
    # print("RANKED:", ranked)

def createHeat(ranked):
    dict = {}
    for i in range(len(ranked)):
        dict[ranked[i]['event']['discrete_visit_subzone']] = ranked[i]['event']['hyperUnique_unique_agents']
    #print("HEAT DICT:", dict)
    #print(len(dict))
    createheatmap.create_heat_map(dict)

def createTopList(ranked):
    list = []
    for i in range(5):
        list.append([ranked[i]['event']['discrete_visit_subzone'],ranked[i]['event']['hyperUnique_unique_agents']])
    #print("RETURN LIST:", list)
    return list

# dicttemp = {"gender": "M", "age": "NA", "race": "NA", "nationality": "SGP"}
# discreteVisit(dicttemp)