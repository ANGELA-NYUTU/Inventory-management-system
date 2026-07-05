import pytest
from unittest.mock import patch
from api import fetch_product_by_barcode



# MOCK OPENFOODFACTS API

@patch("api.requests.get")
def test_fetch_product_by_barcode(mock_get):

    mock_get.return_value.json.return_value = {
        "status": 1,
        "product": {
            "product_name": "Mock Milk",
            "brands": "Mock Brand",
            "ingredients_text": "Mock ingredients",
            "categories": "Mock category",
            "quantity": "1L"
        }
    }

    result = fetch_product_by_barcode("123")

    assert result["status"] == 1
    assert result["product"]["product_name"] == "Mock Milk"