import requests
import time
import json
import operator
import os

from .apiconnnection import APIConnection as Conn
from . import definequerybody


# The main function in the class, an example is below
# Input is a dict example: {"gender": "NA", "age": [1990, 1995], "race": "NA", "nationality": "NA"}
# Output
def fetchODPairs(filterdict):
	subzoneDict = {}
	__location__ = os.path.realpath(
	os.path.join(os.getcwd(), os.path.dirname(__file__)))
	with open(os.path.join(__location__,"subzones1.txt"), "r") as file:
		for line in file:
			(key, val) = line.split('\t')
			subzoneDict[key] = val.replace("\n", "")

	subzoneRank = {}

	subzoneNum = 1

	for i in subzoneDict:

		if subzoneNum % 76 == 0:
			time.sleep(60)

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

		queryBody.update(definequerybody.main_filter_thing_OD(filterdict, i))

		queryResponse = requests.post("https://apistore.datasparkanalytics.com:443/odmatrix/v3/query",
									  data=json.dumps(queryBody),
									  headers={'Authorization': "Bearer " + Conn.token,
											   'Content-Type': Conn.contentType}
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
			tempStr = str(sorted_result[k]['event']['origin_subzone']) + "->" + str(i) + "->" + str(
				sorted_result[k]['timestamp'])
			subzoneRank[tempStr] = int(sorted_result[k]['event']['hyperUnique_unique_agents'])

		for area in subzoneRank:
			print(str(area) + "\t" + str(subzoneRank[str(area)]))

		print("__________________")

	sorted_x = sorted(subzoneRank.items(), key=operator.itemgetter(1), reverse=True)
	for y in range(0,3):
		print(sorted_x[y])

	return sorted_x[0:3]


# For testing purposes!
print(fetchODPairs({"gender": "M", "age": [1990, 1995], "race": "CHINESE", "nationality": "NA"}))

