import pytest


@pytest.fixture(scope='module')
def test_request_login(client):
    response = client.get('/login')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Log in page'
    

@pytest.fixture(scope='module')
def test_request_signup(client):
    response = client.get('/sign-up')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Sign up page'
    
    
@pytest.fixture(scope='module')
def test_request_logout(client):
    response = client.get('/logout')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Logout page'