import pytest
import sys, os

# Ensure Python can find app.py in the parent directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app  # import AFTER fixing sys.path

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_login_page(client):
    rv = client.get('/')
    # Check that the login page contains the word "Login"
    assert b'Login' in rv.data or b'Energy Dashboard Login' in rv.data

def test_valid_login(client):
    rv = client.post('/', data={'username': 'admin', 'password': 'opensesame'}, follow_redirects=True)
    # Should redirect to report page containing the analysis heading
    assert b'Romania Electricity Analysis' in rv.data

def test_invalid_login(client):
    rv = client.post('/', data={'username': 'wrong', 'password': 'wrong'})
    # Should show invalid credentials message
    assert b'Invalid credentials' in rv.data