from currency.models import ContactUs


def test_get(client):
    response = client.get('/currency/contact-us/create/')
    assert response.status_code == 200


def test_post_empty_form(client):
    response = client.post('/currency/contact-us/create/')
    assert response.status_code == 200
    assert response.context_data['form'].errors == {
        'email_from': ['This field is required.'],
        'subject': ['This field is required.'],
        'message': ['This field is required.'],
    }


def test_post_invalid_email(client):
    initial_count = ContactUs.objects.count()
    payload = {
        'email_from': 'INVALID-EMAIL',
        'subject': 'subject',
        'message': 'body',
    }
    response = client.post('/currency/contact-us/create/', data=payload)
    assert response.status_code == 200
    assert response.context_data['form'].errors == {'email_from': ['Enter a valid email address.']}
    assert ContactUs.objects.count() == initial_count


def test_post_valid_email(client, mailoutbox, settings):
    initial_count = ContactUs.objects.count()
    payload = {
        'email_from': 'test@gmail.com',
        'subject': 'subject',
        'message': 'body',
    }
    response = client.post('/currency/contact-us/create/', data=payload)
    assert response.status_code == 302
    assert response['location'] == '/currency/contact-us/'
    assert len(mailoutbox) == 1
    assert mailoutbox[0].from_email == settings.DEFAULT_FROM_EMAIL
    assert ContactUs.objects.count() == initial_count + 1
