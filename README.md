# Inventory Management System (Flask REST API)
## Project Overview
This project is a Python-based Inventory Management System built using Flask. It provides a REST API for managing inventory items and a command-line interface (CLI) for user interaction. The system also integrates with the OpenFoodFacts API to fetch real product information using barcodes or product names.
The data is stored in a temporary in-memory list to simulate a database.

## Features
- Flask REST API
- Full CRUD operations (Create, Read, Update, Delete)
- CLI-based user interface
- External API integration (OpenFoodFacts)
- In-memory mock database
- Unit testing using pytest
- Mocking external API calls using unittest.mock

## Project Structure
inventory-management-system/
app.py
inventory.py
api.py
cli.py
README.md
requirements.txt
.gitignore
data/
    inventory_data.py
tests/
    test_api.py
    test_cli.py
    test_external_api.py
venv/

## Installation Instructions
### 1. Clone the repository
git clone <https://github.com/ANGELA-NYUTU/Inventory-management-system.git>
cd inventory-management-system
### 2. Create a virtual environment
python -m venv venv
### 3. Activate the virtual environment
Windows:
venv\Scripts\activate

### 4. Install dependencies
pip install -r requirements.txt

## Running the Flask API

Start the server using:
python app.py
The server will run at:
http://127.0.0.1:5000/inventory


## API Endpoints
### Get all inventory items
GET /inventory
### Get a single item by ID
GET /inventory/<id>
### Add a new item
POST /inventory
### Update an existing item
PATCH /inventory/<id>
### Delete an item
DELETE /inventory/<id>

## External API Integration (OpenFoodFacts)
### Search product by barcode
GET /search?barcode=<barcode>
### Search product by name
GET /search?name=<product_name>

## Running the CLI
Run the command-line interface using:
python cli.py
CLI Options:
1. View Inventory
2. View Item
3. Add Item
4. Update Item
5. Delete Item
6. Search Product on OpenFoodFacts
7. Exit

## Running Tests
Run all tests using:
python -m pytest

## Technologies Used

- Python
- Flask
- Requests
- Pytest
- unittest.mock

## Project Description

This system demonstrates how to build a RESTful API using Flask, integrate external APIs, and create a CLI-based interface. It also includes unit testing to ensure functionality and reliability.
The project follows a modular structure separating API logic, business logic, data storage, and testing.
