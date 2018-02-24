from .map import Map
import os

def generate_html(coordinates):
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
