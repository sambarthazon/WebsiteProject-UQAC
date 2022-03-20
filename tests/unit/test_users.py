<<<<<<< HEAD
from website import create_app
=======
>>>>>>> newDev
from website.models import User
from tests.conftest import create_app


flask_app = create_app()
user = User(id=1, email="patoche@gmail.com", username="patoche")


def test_list_user():
    with flask_app.test_client() as test_client:
        response = test_client.get('/users/list')
<<<<<<< HEAD
        assert response.status_code == 302
=======
        assert response.status_code == 200
>>>>>>> newDev
        assert b"User's informations" not in response.data
    