import pickle
import json
import numpy as np

__locations = None
__data_columns = None
__model = None
__type = None

def get_estimated_price(location, baths, bedrooms, area_size, kanal, property_type):    
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    try:
        type_index = __data_columns.index(property_type.lower())
    except:
        type_index = -1

    # Create a zero vector with length equal to the number of features
    x = np.zeros(len(__data_columns))
    
    # Set the values for the numeric features
    x[0] = baths
    x[1] = bedrooms
    x[2] = area_size
    x[3] = kanal
    
    # Set the location index
    if loc_index >= 0:
        x[loc_index] = 1

    # Set the type index
    if type_index >= 0:
        x[type_index] = 1

    # Make prediction using the trained model
    return __model.predict([x])[0]

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __locations
    global __types
    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:7]  # first 3 columns are baths, bedrooms, area_size, kanal
        __types = __data_columns[8:]  # assuming types start from index 8

    global __model
    if __model is None:
        with open('./artifacts/zameen_model.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")

def get_location_names():
    return __locations

def get_data_columns():
    return __data_columns

def get_type():
    return __type

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_type())
    print(get_estimated_price('karachi', 3, 3, 12.2, 1, "house"))
    