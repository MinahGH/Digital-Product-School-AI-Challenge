from flask import Flask, request,jsonify
from utils import load_pickle_file
from data_processing import DataProcessing
import os

def predict_data(data):
    model = load_pickle_file(os.path.join(os.getcwd(),"model/DPS_xgb_reg.pkl"))
    return model.predict(data)

app = Flask(__name__)  

    
@app.route('/prediction')
def index(methods=['POST','GET']):
    data = request.get_json()
    year = data['year']
    month = data['month']
    features = DataProcessing(year,month).process_data()
    
    output = predict_data(year)
    response = {"prediction": int(output[0])}
    return jsonify(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8000, debug=True)
