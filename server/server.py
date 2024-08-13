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

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    try:
        # Extract data from the form with default values and type checks
        location = request.form.get('location')
        bath = int(request.form.get('bath', 0)) if request.form.get('bath') else 0
        bedrooms = int(request.form.get('bedrooms', 0)) if request.form.get('bedrooms') else 0
        area_unit = int(request.form.get('area_unit', 0)) if request.form.get('area_unit') else 0
        area_size = float(request.form.get('area_size', 0.0)) if request.form.get('area_size') else 0.0
        type = request.form.get('type')

        # Ensure all required fields are present
        if not location or not type:
            return jsonify({'error': 'Missing required parameters'}), 400

        # Generate the price estimate
        estimated_price = util.get_estimated_price(location, bath, bedrooms, area_size, area_unit, type)
        
        # Prepare the response
        response = jsonify({
            'estimated_price': estimated_price
        })
        response.headers.add('Access-Control-Allow-Origin', '*')

        return response

    except ValueError as e:
        # Handle conversion errors
        return jsonify({'error': 'Invalid input data'}), 400

    except Exception as e:
        # Handle any other unexpected errors
        return jsonify({'error': 'An error occurred', 'message': str(e)}), 500


if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run()