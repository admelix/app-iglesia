from flask import Flask, jsonify, request, render_template,url_for
from flask_cors import cross_origin


app = Flask(__name__)
app.config['SECRETKEY'] = 'e98bff72d611f311f58ad6b0c4ca87381e08be10'



@app.route('/', methods = [''])
@cross_origin()
def login_endpoint():
    try:
        return render_template('index.html')
    except Exception as e:
        return e


@app.route('/login', methods = ['POST'])
@cross_origin()
def login_endpoint():
    try:
        return render_template('index.html')
    except Exception as e:
        return e


if __name__ == '__main__':

    app.run(host="localhost", port=8989, debug=True)