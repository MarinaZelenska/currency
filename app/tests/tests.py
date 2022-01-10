
def test_index(client):
    response = client.get('/')
    assert response.status_code == 200


def test_rate_list(client):
    response = client.get('/currency/rate/list/')
    assert response.status_code == 200


def test_login(client):
    response = client.get('/auth/login/')
    assert response.status_code == 200
