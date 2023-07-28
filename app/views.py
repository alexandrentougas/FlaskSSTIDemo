from flask import Flask, render_template, render_template_string, request, redirect, url_for

app = Flask(__name__)
app.config.from_object('config')

@app.route('/', methods=('GET', 'POST'))
def index():

    if request.method == 'POST':
        
        name = request.form["name"]
        return redirect(url_for('result', name=name))
        #return render_template('result.html', name=name)                

    else:
        return render_template('index.html')

@app.route('/result')
def result():
    return render_template_string(
        "<h1>"+ request.args.get('name') + "</h1>"
        ) 