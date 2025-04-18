import pytest
import requests
from csv_importer import get_data

def test_home():
    response = requests.get("http://127.0.0.1:5000/")
    assert response.status_code == 200
    assert response.json()["message"] == "Hello, World!"
    
    
def test_import_page():
    response = requests.get("http://127.0.0.1:5000/importer/")
    data = get_data()
    
    assert response.status_code == 200
    assert response.json()["message"] == "imported data: " + str(data)