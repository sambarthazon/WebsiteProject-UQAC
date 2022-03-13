import pytest
from app import create_app


@pytest.fixture(scope='module')
def test_app():
    return create_app()


@pytest.fixture(scope='module')
def test_app_is_created(app):
    assert app.name == 'app'
    
    
@pytest.fixture(scope='module')
def test_config_is_load(config):
    assert config["DEBUG"] is True
    

@pytest.fixture(scope='module')
def test_request_returns_404(client):
    assert client.get("/url_does_not_exist").status_code == 404
    

# def test_create_database(app):
    