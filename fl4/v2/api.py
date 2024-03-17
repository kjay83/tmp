import flask, json
from flask import request, jsonify, abort 

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data
FILE_TO_SAVE='categories.json'
STARTING_SEQUENCE_NUMBER = 1
DEFAULT_INCREMENT= 1
DEFAULT_CATEGORIE_NAME= 'U'
DEFAULT_CATEGORIE_DESCRIPTION= 'categorie par defaut: UNDEFINED'
DEFAULT_DELIMITER='-'
categories = {
    DEFAULT_CATEGORIE_NAME: {
        'sequence': STARTING_SEQUENCE_NUMBER,
        'increment': DEFAULT_INCREMENT,
        'description': DEFAULT_CATEGORIE_DESCRIPTION,
        }, 
}

def reload_if_empty(cat):    
    # print(cat)
    if cat == {} or None:        
        with open(FILE_TO_SAVE,'r+' ) as file:
            cat=json.load(file) 
    return cat

@app.route('/', methods=['GET'])
def home():
    # categories=reload_if_empty(categories)
    return '''<h1>New Ticket generating api V2</h1>
<p>A prototype API for simulate ticket number generation in a waiting line.</p>'''



# A route to return all of the available categories statuses
@app.route('/api/v2/resources/newtickets/status', methods=['GET'])
def api_status():
    #categories=reload_if_empty(categories)
    print(categories)
    return jsonify(categories)

# A route to return a new ticket but categorie is not specified
@app.route('/api/v2/resources/newtickets', methods=['GET'])
def api_get_new_default_ticket():
    #categories=reload_if_empty(categories)
    #find in the dictionnary the categ elemnt with the default name
    categorie = categories.get(DEFAULT_CATEGORIE_NAME) 
    if (categorie==None) : 
        abort(404,"CRITICAL ERROR: default categorie not found")
    else:
        generated_ticket=DEFAULT_CATEGORIE_NAME+DEFAULT_DELIMITER+ f"{categorie['sequence']:04}"
        categorie['sequence']+=categorie['increment']
        return jsonify(generated_ticket)

# A route to return a new ticket from a specified categorie
@app.route('/api/v2/resources/newtickets/<categ_name>', methods=['GET'])
def api_get_new_categ_ticket(categ_name):
    # categories=reload_if_empty(categories)
    #find in the dictionnary the categ elemnt with the default name
    categorie = categories.get(categ_name) 
    if (categorie==None) : 
        abort(404,f"Ressource {categ_name} was not found")
    else:
        generated_ticket=categ_name+DEFAULT_DELIMITER+ f"{categorie['sequence']:04}"
        categorie['sequence']+=categorie['increment']
        return jsonify(generated_ticket)

# A route to create a new categorie
@app.route('/api/v2/resources/newtickets/<categ_name>', methods=['POST'])
def api_post_new_categ(categ_name):
    # categories=reload_if_empty(categories)
    #find in the dictionnary the categ elemnt with the default name
    categorie = categories.get(categ_name) 
    if (categorie==None) : 
        categories[categ_name]={
        'sequence': STARTING_SEQUENCE_NUMBER,
        'increment': DEFAULT_INCREMENT,
        'description': categ_name,
        }        
        return jsonify(categories[categ_name])
    else:
        abort(404,f"Ressource {categ_name} already exist cannot be created!")
        
    
# A route to save the current status of all sequences
@app.route('/api/v2/resources/newtickets/save', methods=['GET'])
def api_save():
    # categories=reload_if_empty(categories)
    with open(FILE_TO_SAVE,'w+' ) as file:
        json.dump(categories, file) 
    return jsonify(categories)

# A route to force reload the status of all sequences using the file
# @app.route('/api/v2/resources/newtickets/reload', methods=['GET'])
# def api_reload():
#     # categories=reload_if_empty(categories)
#     # print(categories)
#     # print(f"before reload categ={categories}")
#     categories={}
#     with open(FILE_TO_SAVE,'r+' ) as file:
#         categories=json.load(file) 
#     print(f"after reload categ={categories}")
#     return jsonify(categories)

app.run(host='0.0.0.0',port='8080')