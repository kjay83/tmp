import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]

#find a book by its id
#return false if it doesn't exist in library
#return the book if it exist
def find_book_by_id(book_id:int):
    result = False
    print(type(book_id))
    if len(books)>0:
        i = 0
        found=False
        while (i < len(books) and found==False):
            local_id=books[i]['id']            
            #if str(local_id)==str(book_id):               
            if local_id==book_id:              
                found=True
                result=books[i]
            i = i + 1
    
    return result


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''


# A route to return all of the available entries in our catalog.
@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)

# A route to return a uniq book in the catalog using its id
@app.route('/api/v1/resources/books/<int:book_id>', methods=['GET'])
def api_book_by_id(book_id):
    book_found= find_book_by_id(book_id)
    if book_found==False:
        flask.abort(404,'book non existent')
    else:
        return jsonify(book_found)



app.run(host='0.0.0.0',port='8080')