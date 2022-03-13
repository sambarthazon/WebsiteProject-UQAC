import pytest


def test_request_login(client):
    response = client.get('/login')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Log in page'
    
    
def test_request_login(client):
    response = client.get('/login')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Log in page'