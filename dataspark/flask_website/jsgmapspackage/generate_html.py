from .map import Map
import os

from backend.get_subzone import *

def generate_html(top_locations, coordinates, top_od_pairs):
	# init map
	loc_map = Map()

	# save as html
	map_html_string = loc_map.__str__(coordinates)


	first_half_html='''
	<html>
	<body>
	 <div class="home">
		 <h1>results</h1>
		 <p>These are the filters that you have selected.</p>
		 <p>
			{% if age %}
				Age: {{ age }}</br>
			{% endif %}

			{% if gender %}
				Gender: {{ gender }}</br>
			{% endif %}

			{% if race %}
				Race: {{ race }}</br>
			{% endif %}

			{% if nationality %}
				Nationality: {{ nationality }}</br>
			{% endif %}

			{% if location %}
				Location: {{ location }}</br>
			{% endif %}
		</p>
		</br>
		</br>

		<h2>Heat Map</h2>
		<img src="/static/heatmap2.png"></br>
	''' + '''
		<table style="width:50%" align="center">
			<tr>
				<th>Location Code</th>
				<th>Locations Name</th> 
				<th>Expected Outreach</th>
			</tr>
			<tr>
				<td>''' + top_locations[0][0] + '''</td>
				<td>''' + get_subzone(top_locations[0][0]) + '''</td> 
				<td>''' + str(top_locations[0][1]) + '''</td>
			</tr>
			<tr>
				<td>''' + top_locations[1][0] + '''</td>
				<td>''' + get_subzone(top_locations[1][0]) + '''</td> 
				<td>''' + str(top_locations[1][1]) + '''</td>
			</tr>
			<tr>
				<td>''' + top_locations[2][0] + '''</td>
				<td>''' + get_subzone(top_locations[2][0]) + '''</td> 
				<td>''' + str(top_locations[2][1]) + '''</td>
			</tr>
			<tr>
				<td>''' + top_locations[3][0] + '''</td>
				<td>''' + get_subzone(top_locations[3][0]) + '''</td> 
				<td>''' + str(top_locations[3][1]) + '''</td>
			</tr>
			<tr>
				<td>''' + top_locations[4][0] + '''</td>
				<td>''' + get_subzone(top_locations[4][0]) + '''</td> 
				<td>''' + str(top_locations[4][1]) + '''</td>
			</tr>
		</table>
	</br>
	</br>
	</br>
	<h2> Most-Travelled Routes </h2>
	'''

	second_half_html='''
	<table style="width:50%" align="center">
		<tr>
			<th>Bus Number</th>
			<th>Expected Outreach</th>
		</tr>
		<tr>
			<td>''' + list(coordinates[0].keys())[0] + '''</td>
			<td>''' + str(top_od_pairs[0][2]) + '''</td>
		</tr>
		<tr>
			<td>''' + list(coordinates[1].keys())[0] + '''</td>
			<td>''' + str(top_od_pairs[1][2]) + '''</td>
		</tr>
		<tr>
			<td>''' + list(coordinates[2].keys())[0] + '''</td>
			<td>''' + str(top_od_pairs[2][2]) + '''</td>
		</tr>
		<tr>
			<td>''' + list(coordinates[3].keys())[0] + '''</td>
			<td>''' + str(top_od_pairs[3][2]) + '''</td>
		</tr>
		<tr>
			<td>''' + list(coordinates[4].keys())[0] + '''</td>
			<td>''' + str(top_od_pairs[4][2]) + '''</td>
		</tr>
	</table>
			 </div>
		</body>
	</html>
	'''

	final_html = first_half_html + map_html_string + second_half_html

	# save as html

	with open(os.path.dirname(__file__) + '/../templates/results.html', "w") as out:
		print(final_html, file=out)
