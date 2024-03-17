from fastapi.testclient import TestClient
import json
from main import app
from main import Category

client = TestClient(app)

def test_read_category_exist():
    response = client.get("/categories/U")
    assert response.status_code == 200
    assert response.json() == {
        "name":"U",
        "description":"default categ", 
        "sequence":1, 
        "increment":1
    }

def test_read_category_inexist():
    response = client.get("/categories/GRT")
    assert response.status_code == 404

def test_get_default_newtickets():
    response = client.get("/newtickets")
    assert response.status_code == 200
    #test le string du ticket reponse
    assert response.json() == "U-0001"
    
    #teste que la sequence de la categ par defaut a ete incremente
    response = client.get("/categories/U")
    assert response.status_code == 200
    assert response.json() == {
        "name":"U",
        "description":"default categ", 
        "sequence":2, 
        "increment":1
    }

def test_get_newtickets_by_categ():
    #la categorie specifiee n'existe pas
    response = client.get("/newtickets/JDFDFDFDF")
    assert response.status_code == 404

    # on recupere le num de sequence actuel de la categorie par defaut
    response = client.get("/categories/U")
    assert response.status_code == 200
    initial_state_categ=response.json()
    actual_sequence= response.json().get("sequence")

    #la categorie existe
    #on fait plusieurs appels de ticket
    nbtry = 7
    for i in range(1,nbtry):
        response = client.get("/newtickets/U")
        assert response.status_code == 200
    
    #verifie un dernier ticket
    response = client.get("/newtickets/U")
    numero_attendu=actual_sequence+nbtry-1
    assert response.json() == "U-"+f"{numero_attendu:04}"

    #verifie 
    #verifie que la sequence de la categorie a ete incrementee
    response = client.get("/categories/U")
    assert response.status_code == 200
    assert response.json().get("sequence") == numero_attendu+1

def test_post_new_categ():
    #creation de nouvelle categorie
    #catego exist deja -- nothing to do  ,http 403 returned
    response = client.post("/categories/U")
    assert response.status_code == 403

    #catego is new, create it, http 201 is returned
    new_category_name="HALLIBURT"
    response = client.post(f"/categories/{new_category_name}")
    assert response.status_code == 201

    #we check the initial values of categ
    response = client.get(f"/categories/{new_category_name}")
    assert response.status_code == 200
    category_created = Category(name=response.json().get("name"),
                                description=response.json().get("description"),
                                sequence=response.json().get("sequence"),
                                increment=response.json().get("increment"))
    
    assert category_created == Category(
        name=new_category_name,
        description="deafult description", 
        sequence=1, 
        increment=1
    )
    
    
    