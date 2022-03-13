import pytest
    
    
@pytest.fixture(scope='module')
def test_request_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Home Page'
    
    
@pytest.fixture(scope='module')
def test_request_create_post(client):
    response = client.get('/create-post')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Create post page'