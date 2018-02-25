#from __future__ import print_function
import math
 
 
class Map(object):
 
	def __init__(self):
		self._points = []
 
	# def add_point(self, coordinates):
	# 	"""
	# 	Adds coordinates to map
	# 	:param coordinates: latitude, longitude
	# 	:return:
	# 	"""
 
	# 	# add only points with existing coordinates
	# 	if not ((math.isnan(coordinates[0])) or (math.isnan(coordinates[1]))):
	# 		self._points.append(coordinates)
 
	# @staticmethod
	# def _lat_rad(lat):
	# 	"""
	# 	Helper function for _get_zoom()
	# 	:param lat:
	# 	:return:
	# 	"""
	# 	sinus = math.sin(math.radians(lat + math.pi / 180))
	# 	rad_2 = math.log((1 + sinus) / (1 - sinus)) / 2
	# 	return max(min(rad_2, math.pi), -math.pi) / 2
 
	# def _get_zoom(self, map_height_pix=900, map_width_pix=1900, zoom_max=21):
	# 	"""
	# 	Algorithm to derive zoom from the activity route. For details please see
	# 	 - https://developers.google.com/maps/documentation/javascript/maptypes#WorldCoordinates
	# 	 - http://stackoverflow.com/questions/6048975/google-maps-v3-how-to-calculate-the-zoom-level-for-a-given-bounds
	# 	:param zoom_max: maximal zoom level based on Google Map API
	# 	:return:
	# 	"""
 
	# 	# at zoom level 0 the entire world can be displayed in an area that is 256 x 256 pixels
	# 	world_heigth_pix = 256
	# 	world_width_pix = 256
 
	# 	# get boundaries of the activity route
	# 	max_lat = max(x[0] for x in self._points)
	# 	min_lat = min(x[0] for x in self._points)
	# 	max_lon = max(x[1] for x in self._points)
	# 	min_lon = min(x[1] for x in self._points)
 
	# 	# calculate longitude fraction
	# 	diff_lon = max_lon - min_lon
	# 	if diff_lon < 0:
	# 		fraction_lon = (diff_lon + 360) / 360
	# 	else:
	# 		fraction_lon = diff_lon / 360
 
	# 	# calculate latitude fraction
	# 	fraction_lat = (self._lat_rad(max_lat) - self._lat_rad(min_lat)) / math.pi
 
	# 	# get zoom for both latitude and longitude
	# 	zoom_lat = math.floor(math.log(map_height_pix / world_heigth_pix / fraction_lat) / math.log(2))
	# 	zoom_lon = math.floor(math.log(map_width_pix / world_width_pix / fraction_lon) / math.log(2))
 
	# 	return min(zoom_lat, zoom_lon, zoom_max)
 
	def __str__(self, coordinates):
		"""
		A Python wrapper around Google Map Api v3; see
		 - https://developers.google.com/maps/documentation/javascript/
		 - https://developers.google.com/maps/documentation/javascript/examples/polyline-simple
		 - http://stackoverflow.com/questions/22342097/is-it-possible-to-create-a-google-map-from-python
		:return: string to be stored as html and opened in a web browser
		"""
		# # center of the activity route
		# center_lat = (max((x[0] for x in self._points)) + min((x[0] for x in self._points))) / 2
		# center_lon = (max((x[1] for x in self._points)) + min((x[1] for x in self._points))) / 2
 
		# # get zoom needed for the route
		# zoom = self._get_zoom()
 
		# # string with points for the google.maps.Polyline
		# activity_coordinates = ",\n".join(
		# 	["{{lat: {lat}, lng: {lon}}}".format(lat=x[0], lon=x[1]) for x in self._points])
		zoom = 11
		center_lat=1.35527
		center_lon=103.811959

		return """
			<script src="https://maps.googleapis.com/maps/api/js?v=3.exp&sensor=false"></script>
			<div id="map-canvas" style="height: 60%; width: 60%"></div>
			<script type="text/javascript">
				var map;
				function show_map() {{
					map = new google.maps.Map(document.getElementById("map-canvas"), {{
						zoom: {zoom},
						center: new google.maps.LatLng({center_lat}, {center_lon}),
						mapTypeId: 'roadmap'
					}});""".format(zoom=zoom, center_lat=center_lat, center_lon=center_lon) + """
 
					var busstop_coordinates0 = """ + list(coordinates[0].values())[0] + """
					var busstop_coordinates1 = """ + list(coordinates[1].values())[0] + """
					var busstop_coordinates2 = """ + list(coordinates[2].values())[0] + """
					var busstop_coordinates3 = """ + list(coordinates[3].values())[0] + """
					var busstop_coordinates4 = """ + list(coordinates[4].values())[0] + """

					var polyline_colors = ["#FF0000", "#32CD32", "#FF4500", "#EE82EE", "#000000"]

					var bus_route0 = new google.maps.Polyline({{
						path: busstop_coordinates0,
						geodesic: true,
						strokeColor: polyline_colors[0],
						strokeOpacity: 1.0,
						strokeWeight: 4
						}});
					var bus_route1 = new google.maps.Polyline({{
						path: busstop_coordinates1,
						geodesic: true,
						strokeColor: polyline_colors[1],
						strokeOpacity: 1.0,
						strokeWeight: 4
						}});
					var bus_route2 = new google.maps.Polyline({{
						path: busstop_coordinates2,
						geodesic: true,
						strokeColor: polyline_colors[2],
						strokeOpacity: 1.0,
						strokeWeight: 4
						}});
					var bus_route3 = new google.maps.Polyline({{
						path: busstop_coordinates3,
						geodesic: true,
						strokeColor: polyline_colors[3],
						strokeOpacity: 1.0,
						strokeWeight: 4
						}});
					var bus_route4 = new google.maps.Polyline({{
						path: busstop_coordinates4,
						geodesic: true,
						strokeColor: polyline_colors[4],
						strokeOpacity: 1.0,
						strokeWeight: 4
						}});
 
					bus_route0.setMap(map);
					bus_route1.setMap(map);
					bus_route2.setMap(map);
					bus_route3.setMap(map);
					bus_route4.setMap(map);
				}}
				google.maps.event.addDomListener(window, 'load', show_map);
			</script>
			<script async defer
				src="https://maps.googleapis.com/maps/api/js?key=AIzaSyBOtjVkTQjkvzYNoq9poBhprKOlIlc7JLk&callback=show_map" type='text/javascript'>
			</script>
		""".format()
