from src.tests import testApp, token, user, teardownUser

def setup_module(module):
  user('admin')
  user('user')

def test_create_user(testApp, token):
    response = testApp.post(
        "/users",
        headers={'Authorization': token().auth},
        json={"username": "nonexistinguser", "password": "nopassword", "role": "user"}
    )
    assert response.status_code == 200
    assert response.json() == { 'id': 3, 'is_active': True, 'role': 'user', 'username': 'nonexistinguser'}

def test_create_existing_user(testApp, token):
    response = testApp.post(
        "/users",
        headers={'Authorization': token().auth},
        json={"username": "nonexistinguser", "password": "nopassword", "role": "user"}
    )
    assert response.status_code == 400
    assert response.json() == {'detail': "{'username': ['Username already exist']}"}

def test_get_user_list(testApp, token):
    response = testApp.get(
        "/users",
        headers={'Authorization': token().auth},
    )
    assert response.status_code == 200
    assert response.json() == {
        'page': 0,
        'total': 3,
        'limit': 10,
        'items': [
            {'id': 1, 'is_active': True, 'role': 'admin', 'username': 'admintest'},
            {'id': 2, 'is_active': True, 'role': 'user', 'username': 'usertest'},
            {'id': 3, 'is_active': True, 'role': 'user', 'username': 'nonexistinguser'}
        ],
    }
    
def test_get_user_list_with_user_no_valid_role(testApp, token):
    response = testApp.get(
        "/users",
        headers={'Authorization': token('user').auth},
    )
    assert response.status_code == 403


def test_get_user(testApp, token):
    response = testApp.get(
        "/users/1",
        headers={'Authorization': token().auth},
    )
    assert response.status_code == 200
    assert response.json() == {'id': 1, 'is_active': True, 'role': 'admin', 'username': 'admintest'}

def test_get_non_existing_client(testApp, token):
    response = testApp.get(
        "/users/5",
        headers={'Authorization': token().auth},
    )
    assert response.status_code == 400
    assert response.json() == {'detail': 'User does not exist'}

def test_update_user(testApp, token):
    response = testApp.put(
        "/users/3",
        headers={'Authorization': token().auth},
        json={"username": "updated user", "role": "user", 'is_active': False, 'password': 'ninguna' }
    )
    assert response.status_code == 200
    assert response.json() == {'id': 3, 'is_active': False, 'role': 'user', 'username': 'updated user'}

def test_update_user_with_invalid_fields(testApp, token):
    response = testApp.put(
        "/users/3",
        headers={'Authorization': token().auth},
        json={"username": "", "role": "user", 'is_active': False, 'password': 'ninguna' }
    )
    assert response.status_code == 400
    assert response.json() == {'detail': "{'username': ['is Required']}"}

def test_update_non_existing_user(testApp, token):
    response = testApp.put(
        "/users/5",
        headers={'Authorization': token().auth},
        json={"username": "updated user", "role": "user", 'is_active': False, 'password': 'ninguna' }
    )
    assert response.status_code == 400
    assert response.json() == {'detail': 'User does not exist'}

def test_delete_user(testApp, token):
    response = testApp.delete(
        "/users/3",
        headers={'Authorization': token().auth}
    )
    assert response.status_code == 200

def test_delete_non_existing_user(testApp, token):
    response = testApp.delete(
        "/users/3",
        headers={'Authorization': token().auth}
    )
    assert response.status_code == 400
    assert response.json() == {'detail': 'User does not exist'}

def teardown_module(module):
  teardownUser()
