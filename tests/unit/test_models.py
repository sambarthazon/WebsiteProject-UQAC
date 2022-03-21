from website.models import User, Post, Comment, Like


def test_new_user():
    user = User(email='patkennedy79@gmail.com', username='patoche', password='FlaskIsAwesome')
    assert user.email == 'patkennedy79@gmail.com'
    assert user.username != 'Sam'
    assert user.password == 'FlaskIsAwesome'
    
    
def test_new_post():
    post = Post(text='azert', author='patoche')
    assert post.text == 'azert'
    assert post.author == 'patoche'
    
    
def test_new_comment():
    comment = Comment(text='abc', author='patoche', post_id='123')
    assert comment.text == 'abc'
    assert comment.author != 'Victorleplusbeau'
    assert comment.post_id == '123'
    
    
def test_new_like():
    like = Like(author='patoche', post_id='2')
    assert like.author == 'patoche'
    assert like.post_id != '3'


# Tester le login (avec flask_login)