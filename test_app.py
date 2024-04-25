import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_login_page(client):
    """Test login page rendering."""
    response = client.get('/')
    assert b'Login' in response.data

def test_valid_login(client):
    """Test valid login."""
    response = client.post('/login', data=dict(
        username='sai',
        password='sai@123'
    ), follow_redirects=True)
    assert b'Welcome, sai!' in response.data

def test_invalid_login(client):
    """Test invalid login."""
    response = client.post('/login', data=dict(
        username='invaliduser',
        password='invalidpassword'
    ), follow_redirects=True)
    assert b'Invalid username or password' in response.data

def test_dashboard_unauthenticated(client):
    response = client.get('/dashboard')
    assert response.status_code == 302
    assert response.headers['Location'] == '/'

def test_logout(client):
    """Test logout functionality."""
    response = client.get('/logout', follow_redirects=True)
    assert b'Login' in response.data
