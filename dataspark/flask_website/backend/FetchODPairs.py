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
	with open(os.path.join(__location__,"subzones2.txt"), "r") as file:
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

		for k in range(0, 1):
			tempStr = str(sorted_result[k]['event']['origin_subzone']) + "->" + str(i)
			subzoneRank[tempStr] = int(sorted_result[k]['event']['hyperUnique_unique_agents'])

		for area in subzoneRank:
			print(str(area) + "\t" + str(subzoneRank[str(area)]))

		print("__________________")

	sorted_x = sorted(subzoneRank.items(), key=operator.itemgetter(1), reverse=True)
	sortedlist = [[sorted_x[0][0][:6],sorted_x[0][0][8:],sorted_x[0][1]],
				  [sorted_x[1][0][:6],sorted_x[1][0][8:],sorted_x[1][1]],
				  [sorted_x[2][0][:6],sorted_x[2][0][8:],sorted_x[2][1]],
				  [sorted_x[3][0][:6],sorted_x[3][0][8:],sorted_x[3][1]],
				  [sorted_x[4][0][:6],sorted_x[4][0][8:],sorted_x[4][1]]]

	return sortedlist


# For testing purposes!
#print(fetchODPairs({"gender": "M", "age": [1990, 1995], "race": "CHINESE", "nationality": "NA"}))

