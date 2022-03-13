def test_request_login(new_auth):
    response = new_auth.get('/login')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Log in page'
    
    
def test_request_signup(new_auth):
    response = new_auth.get('/sign-up')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Sign up page'
    
    
def test_request_logout(new_auth):
    response = new_auth.get('/logout')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Logout page'