from flask import Flask,request,jsonify
import pickle
import numpy as np


# setup application
app = Flask(__name__)

def prediction(lst):
    filename = 'model/RatingPredictor.pickle'
    with open(filename, 'rb') as file:
        model = pickle.load(file)
    pred_value = model.predict([lst]).tolist()
    return pred_value

@app.route('/hotel', methods=['POST', 'GET'])
def hotel():
    pred=0
    if request.method == 'POST':
        Acttraction_Place = request.json['col_1']
        Transportation_Modes = request.json['col_2']
        feature_list = []

        feature_list.append(int(Acttraction_Place))
        feature_list.append(int(Transportation_Modes))

        pred = prediction(feature_list)
        print(pred)

    return jsonify({'data': pred[0]})

if __name__ =='__main__':
    app.run(debug=True)