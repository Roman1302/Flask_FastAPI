from flask import Flask
from flask import render_template

app = Flask(__name__)
@app.route('/')

@app.route('/clothes/')
def clothes():
    return render_template('clothes.html')

@app.route('/hats/')
def jacket():
    return render_template('hats.html')

@app.route('/shoes/')
def shoes():
    return render_template('shoes.html')



if __name__ == '__main__':
    app.run()