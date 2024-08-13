from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/get_types_names', methods=['GET'])
def get_types_names():
    response = jsonify({
        'types': util.get_type_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    # Extract data from the form
    location = request.form.get['location']
    bath = int(request.form.get['bath'])
    bedrooms = int(request.form.get['bedrooms'])
    area_unit = int(request.form.get['area_unit'])
    area_size = float(request.form.get['area_size'])
    type = request.form.get['type']

    response = jsonify({
        'estimated_price': util.get_estimated_price(location, bath, bedrooms, area_size, area_unit, type)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run()