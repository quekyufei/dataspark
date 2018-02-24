import googlemaps as gmp
import polyline

API_KEY = "AIzaSyAKc0dmMyEXyn_R2Kp5q24Ba54DjXawTXA"
gmap = gmp.Client(key=API_KEY)

#testing values
#origin = (1.31859, 103.84658)
#destination = (1.32626, 103.85567)


def get_poly_line(origin, destination):
    result = gmap.directions(origin= origin,
        destination=destination, mode="transit", transit_mode="train")
    if result:
        polyline_list = polyline.decode(result[0]["overview_polyline"]['points'])
        polyline_dict = ",\n".join(
            ["{{lat: {lat}, lng: {lon}}}".format(lat=x[0], lon=x[1]) for x in polyline_list])
        print(polyline_dict)
    else:
        print("trip not valid")


print(get_poly_line((1.335239, 103.842639), (1.352616, 103.977933)))
