from flask import Flask
from flask import jsonify

app = Flask('pyladies')

@app.route('/pessoas')
def json_api():
    pessoas = [{'nome':'Bruno Rocha'},
                {'nome': 'Beatriz Harumi'},
                {'nome': 'Aline'},
                {'nome': 'Duda'},
                {'nome': 'Paty'},
                ]
    return jsonify(pessoas=pessoas, total=len(pessoas)), 200

app.run()
