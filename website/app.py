from flask import Flask,request,jsonify
import pickle
import numpy as np


# setup application
app = Flask(__name__)




#Hotel API

def predictionHotel(lst):
    filename = 'model/HotelRatingPredictor.pickle'
    with open(filename, 'rb') as file:
        model = pickle.load(file)
    pred_value = model.predict([lst]).tolist()
    return pred_value

@app.route('/hotel', methods=['POST', 'GET'])
def hotel():
    pred=0
    if request.method == 'POST':
        Attraction_Place = request.json['AttractionPlace']
        Transportation_Modes = request.json['TransportationModes']
        if ( isinstance(Attraction_Place, int) and  isinstance(Transportation_Modes, int) ): 
            feature_list = []

            feature_list.append(int(Attraction_Place))
            feature_list.append(int(Transportation_Modes))

            pred = predictionHotel(feature_list)
            print(pred)

            return jsonify({'data': pred[0]})
            
        else :
            if(not isinstance(Attraction_Place, int)):
                return jsonify({'Error': "Acttraction Places Are Missing !"})
            else :
                return jsonify({'Error': "Transportation Modes Are Missing!"})
            
        

#Restaurant API
        
def predictionRestaurant(lst):
    filename = 'model/RestaurantRatingPredictor.pickle'
    with open(filename, 'rb') as file:
        model = pickle.load(file)
    pred_value = model.predict([lst]).tolist()
    return pred_value      

@app.route('/restaurant', methods=['POST', 'GET'])
def restaurant():
    if request.method == 'POST':
        Shoping_Area = request.json['ShopingArea']
        Distance_ToCity = request.json['DistanceToCity']
        if ( isinstance(Shoping_Area, int) and  (isinstance(Distance_ToCity, float) or isinstance(Distance_ToCity, int) ) ): 
            feature_list = []

            feature_list.append(int(Shoping_Area))
            if(isinstance(Distance_ToCity, float)):
                feature_list.append(float(Distance_ToCity))
            else:
                feature_list.append(int(Distance_ToCity))
            pred = predictionRestaurant(feature_list)
            print(pred)

            return jsonify({'data': pred[0]})
            
        else :
            if(not isinstance(Shoping_Area, int)):
                return jsonify({'Error': "Shoping Area's Are Missing !"})
            else :
                return jsonify({'Error': "Distance To City Is Missing!"})



if __name__ =='__main__':
    app.run(debug=True)