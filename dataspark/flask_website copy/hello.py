from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/form/')
def form():
    return render_template('form.html')

@app.route('/index/',methods=['POST','GET'])
def process_form():
    if request.method == 'POST':
       form_input = request.form['name']
       return render_template('index.html',name=form_input)
    else:
       return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)