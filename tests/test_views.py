import pytest
    
    
@pytest.fixture(scope='module')
def test_request_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Home Page'