import requests
import time
import json
import operator
from possible_use_cases import APIConnection as conn

subzoneDict = {}
with open("subzones.txt", "r") as file:
    for line in file:
        (key, val) = line.split('\t')
        subzoneDict[key] = val.replace("\n", "")

subzoneRank = {}

subzoneNum = 1

for i in subzoneDict:

    if subzoneNum % 76 == 0:
        time.sleep(30)

    queryBody = {
        "date": "2018-02-14",
        "timeSeriesReference": "destination",
        "location": {
            "locationType": "locationHierarchyLevel",
            "levelType": "destination_subzone",
            "id": i
        },
        "queryGranularity": {
            "type": "period",
            "period": "P1D"
        },
        "filter": {
            "type": "AND",
            "fields": [{"type": "NOT"},
                       {}],


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
                                  headers={'Authorization': "Bearer " + conn.APIConnection.token,
                                           'Content-Type': conn.APIConnection.contentType}
                                  )

    result = queryResponse.json()

    print(str(subzoneNum) + ": dest->[" + str(i) + "]")
    subzoneNum += 1

    # for k in range(0, len(result)):
    #     string = str(result[k]['event']['origin_subzone']) + ": " \
    #              + str(result[k]['event']['hyperUnique_unique_agents'])
    #     print(string)

    sorted_result = sorted(result, key=lambda subzone: subzone['event']['hyperUnique_unique_agents'], reverse=True)

    for k in range(0, 3):
        tempStr = str(sorted_result[k]['event']['origin_subzone']) + "->" + str(i) + "->" + str(sorted_result[k]['timestamp'])
        subzoneRank[tempStr] = int(sorted_result[k]['event']['hyperUnique_unique_agents'])

    for area in subzoneRank:
        print(str(area) + "\t" + str(subzoneRank[str(area)]))

    print("__________________")

    sorted_x = sorted(subzoneRank.items(), key=operator.itemgetter(1), reverse=True)
    print(sorted_x)


