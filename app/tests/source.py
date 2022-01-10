from currency.models import Source


def test_get_source_create(client):
    response = client.get('/currency/source/create/')
    assert response.status_code == 200


def test_get_source_list(client):
    response = client.get('/currency/source/list/')
    assert response.status_code == 200


def test_post_source_create_positive(client):
    initial_count = Source.objects.count()
    payload = {
        'source_url': 'www.privatbank.com',
        'name': 'Privatbank',
        'logo': 'https://lenta.ru/articles/2021/04/29/nft/',
        'code_name': 'PB',
    }
    response = client.post('/currency/source/create/', data=payload)
    assert response.status_code == 302
    assert Source.objects.count() == initial_count + 1


def test_post_source_create_negative_source_url(client):
    initial_count = Source.objects.count()
    payload = {
        'source_url': '',
        'name': 'Privatbank',
        'logo': 'https://lenta.ru/articles/2021/04/29/nft/',
        'code_name': 'PB',
    }
    response = client.post('/currency/source/create/', data=payload)
    assert response.status_code == 200
    assert response.context_data['form'].errors == {'source_url': ['This field is required.']}
    assert Source.objects.count() == initial_count


def test_post_source_create_negative_source_name(client):
    initial_count = Source.objects.count()
    payload = {
        'source_url': 'www.privatbank.com',
        'name': '',
        'logo': 'https://lenta.ru/articles/2021/04/29/nft/',
        'code_name': 'PB',
    }
    response = client.post('/currency/source/create/', data=payload)
    assert response.status_code == 200
    assert response.context_data['form'].errors == {'name': ['This field is required.']}
    assert Source.objects.count() == initial_count


def test_post_source_create_logo(client):  # logo is not required
    initial_count = Source.objects.count()
    payload = {
        'source_url': 'www.privatbank.com',
        'name': 'PB',
        'logo': '',
        'code_name': 'PB',
    }
    response = client.post('/currency/source/create/', data=payload)
    assert response.status_code == 302
    assert Source.objects.count() == initial_count + 1


def test_post_source_create_negative_code_name(client):
    initial_count = Source.objects.count()
    payload = {
        'source_url': 'www.privatbank.com',
        'name': 'pb',
        'logo': 'https://lenta.ru/articles/2021/04/29/nft/',
        'code_name': '',
    }
    response = client.post('/currency/source/create/', data=payload)
    assert response.status_code == 200
    assert response.context_data['form'].errors == {'code_name': ['This field is required.']}
    assert Source.objects.count() == initial_count
