from bus_stops_subzones import busStops
from bus_routes import busRoutes

# origin = "HGSZ01"
# destination = "NVSZ01"

# finds buses that passes by both origin & destination
# does not take direction into account
# i.e. may include buses that pass by FROM destination TO origin
def findBuses(origin, destination):
    BS = busStops["value"]
    BR = busRoutes["value"]
    stopsInOrigin = []
    stopsInDest = []
    busesInOrigin = []
    busesInDest = []
    buses = []
    for i in BS:
        if i["Subzone"] == origin:
            stopsInOrigin.append(i["BusStopCode"])
        if i["Subzone"] == destination:
            stopsInDest.append(i["BusStopCode"])
    for i in stopsInOrigin:
        for j in BR:
            if i == j["BusStopCode"]:
                busesInOrigin.append(j["ServiceNo"])
    for i in stopsInDest:
        for j in BR:
            if i == j["BusStopCode"]:
                busesInDest.append(j["ServiceNo"])
    buses = list(set(busesInOrigin).intersection(busesInDest))

    return buses

def findBusRoutes(origin, destination):
    buses = findBuses(origin, destination)
    paths = {}
    print(buses)
    for bus in buses:
        start = None
        end = None
        routes = []
        for i in range(len(busRoutes["value"])):
            if bus == busRoutes["value"][i]["ServiceNo"] and busRoutes["value"][i]['Subzone'] == origin and start == None:
                start = i
            if bus == busRoutes["value"][i]["ServiceNo"] and busRoutes["value"][i]['Subzone'] == destination:
                end = i+1
        # To only include buses that passes by FROM origin TO destination
        if start < end:
            for each in busRoutes["value"][start:end]:
                busCode = each["BusStopCode"]
                Lat = "lat"
                Long = "lng"
                long = None
                lat = None
                for ea in busStops["value"]:
                    if busCode == ea["BusStopCode"]:
                        long = ea["Longitude"]
                        lat = ea["Latitude"]
                    if long != None:
                        break
                routes.append({Lat: lat, Long: long})
            routes = str(routes)
            routes = routes.replace("\'", '')
            print(routes)
            paths[bus] = routes
    return paths

print(findBusRoutes(origin, destination))
