from flask import Flask, render_template, request, redirect

app = Flask(__name__)
number = 0

@app.route('/', methods=['GET', 'POST'])
def index():
    global number
    if request.method == 'GET':
        return render_template('index.html', number=number) 
    else:
        number = request.form.get('number')
        return redirect('/')

