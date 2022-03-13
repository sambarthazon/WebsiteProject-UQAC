def test_new_user(new_user):
    assert new_user.username == "patkennedy"
    assert new_user.email == "patkennedy79@gmail.com"
    
    
def test_new_post(new_post):
    assert new_post.author == "Johann"
    assert new_post.text == "Test"