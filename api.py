import requests



# SEARCH BY BARCODE

def fetch_product_by_barcode(barcode):
    url = f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"

    try:
        response = requests.get(url, timeout=5)
        data = response.json()

        if data.get("status") == 1:
            product = data["product"]

            return {
                "status": data["status"],
                "product": {
                    "barcode": barcode,
                    "product_name": product.get("product_name", "Unknown"),
                    "brands": product.get("brands", "Unknown"),
                    "ingredients_text": product.get("ingredients_text", "Not available"),
                    "categories": product.get("categories", "Unknown"),
                    "quantity": product.get("quantity", "Unknown")
                }
            }

        return {"error": "Product not found"}

    except requests.exceptions.RequestException:
        return {"error": "API request failed"}



# SEARCH BY PRODUCT NAME

def fetch_product_by_name(name):
    url = f"https://world.openfoodfacts.org/cgi/search.pl?search_terms={name}&json=1"

    try:
        response = requests.get(url, timeout=5)
        data = response.json()

        products = data.get("products", [])

        if not products:
            return {"error": "No products found"}

        first_product = products[0]

        return {
            "status": 1,
            "product": {
                "product_name": first_product.get("product_name", "Unknown"),
                "brands": first_product.get("brands", "Unknown"),
                "ingredients_text": first_product.get("ingredients_text", "Not available"),
                "categories": first_product.get("categories", "Unknown"),
                "quantity": first_product.get("quantity", "Unknown")
            }
        }

    except requests.exceptions.RequestException:
        return {"error": "API request failed"}