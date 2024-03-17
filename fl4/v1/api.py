import flask
from flask import request, jsonify, abort 
#from flask.json import jsonify
#from flask_restful import Api, Resource, abort, reqparse

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data
STARTING_SEQUENCE_NUMBER = 1
DEFAULT_INCREMENT= 1
DEFAULT_CATEGORIE_NAME= 'U'
DEFAULT_CATEGORIE_DESCRIPTION= 'categorie par defaut'
DEFAULT_DELIMITER='-'
categories = [
    {'name': DEFAULT_CATEGORIE_NAME,
     'sequence': STARTING_SEQUENCE_NUMBER,
     'increment': DEFAULT_INCREMENT,
     'description': DEFAULT_CATEGORIE_DESCRIPTION,
     },
    {'name': 'R',
     'sequence': STARTING_SEQUENCE_NUMBER,
     'increment': DEFAULT_INCREMENT,
     'description': 'Reclamation',},
    {'name': 'P',
     'sequence': STARTING_SEQUENCE_NUMBER,
     'increment': DEFAULT_INCREMENT,
     'description': 'Paiement'},
]

#find a categ by its name
#return false if it doesn't exist in library
#return the categ if it exist
def find_categ_by_name(categ_name:str):
    result = False
    #print(type(book_id))
    if len(categories)>0:
        i = 0
        found=False
        while (i < len(categories) and found==False):
            local_name=categories[i]['name']            
            #if str(local_id)==str(book_id):               
            if local_name==categ_name:              
                found=True
                result=categories[i]
            i = i + 1
    
    return result

@app.route('/', methods=['GET'])
def home():
    return '''<h1>New Ticket generating api</h1>
<p>A prototype API for simulate ticket number generation in a waiting line.</p>'''


# @app.errorhandler(404)
# def custom404(error):
#     response = jsonify({'message': error.description})
#     response.status_code = 404
#     response.status = 'error.Bad Request'
#     return jsonify(response)



# A route to return all of the available categories statuses
@app.route('/api/v1/resources/newtickets/status', methods=['GET'])
def api_status():
    return jsonify(categories)

# A route to return a new ticket but categorie is not specified
@app.route('/api/v1/resources/newtickets', methods=['GET'])
def api_get_new_default_ticket():
    #find in the dictionnary the categ elemnt with the default name
    categorie = find_categ_by_name(DEFAULT_CATEGORIE_NAME)
    if (categorie==False) : 
        abort(404,"CRITICAL ERROR: default categorie not found")
    else:
        generated_ticket=categorie['name']+DEFAULT_DELIMITER+ f"{categorie['sequence']:04}"
        categorie['sequence']+=categorie['increment']
        return jsonify(generated_ticket)

app.run(host='0.0.0.0',port='8080')