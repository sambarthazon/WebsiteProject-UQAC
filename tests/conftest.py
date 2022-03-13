import email
import pytest
from app import create_app
from website.auth import login
from website.models import User, Post


@pytest.fixture(scope='module')
def test_app():
    return create_app()


@pytest.fixture(scope='module')
def new_user():
    user = User(email="patkennedy79@gmail.com", username="patkennedy")
    return user


@pytest.fixture(scope='module')
def new_post():
    post = Post(text="Test", author="Johann")