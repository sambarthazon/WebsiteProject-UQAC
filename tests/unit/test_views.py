from website import create_app, create_database
from tests.conftest import create_app

flask_app = create_app()

def test_home_page():
    with flask_app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200
        assert b"Post" in response.data
        
        
# def test_create_post():
#     with flask_app.test_client() as test_client:
#         response = test_client.post('/post/create')
#         assert response.status_code == 302
#         assert b"Home" not in response.data
#         assert b"Make a Post" in response.data