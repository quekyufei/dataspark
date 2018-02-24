from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/results')
def home():
	return render_template('home.html')

@app.route('/form/')
def form():
	return render_template('form.html')

@app.route('/',methods=['POST','GET'])
def process_form():
	if request.method == 'POST':
	#request.form is a dictionary with the values from the form
		return render_template('home.html', age = request.form['age'], gender = request.form['gender'], race = request.form['race'], nationality = request.form['nationality'], location = request.form['location'])
	else:
		return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)