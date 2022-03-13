def test_app_is_created(app):
    assert app.name == 'app'
    
    
def test_config_is_load(config):
    assert config["DEBUG"] is True
    

def test_request_returns_404(client):
    assert client.get("/url_does_not_exist").status_code == 404