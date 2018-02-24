from .map import Map
import os

def generate_html(top_locations, coordinates):
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
		<img src="/static/heatmap.png"></br>
	''' + '''
	<table style="width:50%">
		<tr>
			<th>Location Code</th>
			<th>Locations Name</th> 
			<th>Expected Outreach</th>
		</tr>
		<tr>
			<td>''' + top_locations[0][0] + '''</td>
			<td>{name0}</td> 
			<td>''' + top_locations[0][2] + '''</td>
		</tr>
		<tr>
			<td>''' + top_locations[1][0] + '''</td>
			<td>{name0}</td> 
			<td>''' + top_locations[1][2] + '''</td>
		</tr>
		<tr>
			<td>''' + top_locations[2][0] + '''</td>
			<td>{name0}</td> 
			<td>''' + top_locations[2][2] + '''</td>
		</tr>
		<tr>
			<td>''' + top_locations[3][0] + '''</td>
			<td>{name0}</td> 
			<td>''' + top_locations[3][2] + '''</td>
		</tr>
		<tr>
			<td>''' + top_locations[4][0] + '''</td>
			<td>{name0}</td> 
			<td>''' + top_locations[4][2] + '''</td>
		</tr>
	</table>
	'''

	second_half_html='''
			 </div>
		</body>
	</html>
	'''

	final_html = first_half_html + map_html_string + second_half_html

	# save as html

	with open(os.path.dirname(__file__) + '/../templates/results.html', "w") as out:
		print(final_html, file=out)
