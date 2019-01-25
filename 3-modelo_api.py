import flask
from flask import request, jsonify
import pickle
# and later you can load it
with open('/Users/laiunce/Documents/codigos/modelo_api/2-modelo.pkl', 'rb') as f:
    clf = pickle.load(f)
    

app = flask.Flask(__name__)
app.config["DEBUG"] = True

#curl http://127.0.0.1:5000/api/v1/resources/post -d '{"foo": "bar"}' -H 'Content-Type: application/json'
#curl -H 'Content-Type: application/json' http://127.0.0.1:5000/api/v1/resources/post -d @data.json
@app.route('/api/v1/resources/post', methods=['POST'])
def post_route():
    if request.method == 'POST':

        data = request.get_json()

        pred = [data['v1'],data['v2'],data['v3'],data['v4']]
        
        prediccion = clf.predict(pred) 
        
        return jsonify(int(prediccion[0]))

#curl http://127.0.0.1:5000/api/v1/resources/get?v1=5
#http://127.0.0.1:5000/api/v1/resources/get?v1=5&v2=5&v3=5&v4=5
@app.route('/api/v1/resources/get', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    
    pred = [request.args['v1'],request.args['v2'],request.args['v3'],request.args['v4']]
    prediccion = clf.predict(pred) 
    return jsonify(int(prediccion[0]))


app.run()