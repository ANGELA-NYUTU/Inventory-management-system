import pytest
from app import app


@pytest.fixture
def client():
    app.testing = True
    return app.test_client()


# TEST GET ALL ITEMS

def test_get_all_items(client):
    response = client.get("/inventory")
    assert response.status_code == 200
    assert isinstance(response.json, list)



# TEST GET SINGLE ITEM

def test_get_single_item(client):
    response = client.get("/inventory/1")
    assert response.status_code in [200, 404]



# TEST CREATE ITEM

def test_create_item(client):
    new_item = {
        "status": 1,
        "product": {
            "product_name": "Test Product",
            "brands": "Test Brand",
            "ingredients_text": "Test ingredients",
            "categories": "Test category",
            "quantity": "1 unit"
        },
        "price": 100,
        "stock": 10
    }

    response = client.post("/inventory", json=new_item)
    assert response.status_code == 201


# TEST UPDATE ITEM

def test_update_item(client):
    update_data = {"price": 999}

    response = client.patch("/inventory/1", json=update_data)
    assert response.status_code in [200, 404]



# TEST DELETE ITEM

def test_delete_item(client):
    response = client.delete("/inventory/1")
    assert response.status_code in [200, 404]