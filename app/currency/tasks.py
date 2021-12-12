from bs4 import BeautifulSoup

from celery import shared_task

from currency import consts, model_choices as mch
from currency.utils import *

from django.conf import settings
from django.core.mail import send_mail

import requests


def add_rates_in_db(currency_type, source, buy, sale):
    from currency.models import Rate
    last_rate = Rate.objects \
        .filter(type=currency_type, source=source) \
        .order_by('-created') \
        .first()

    if last_rate is None or \
            last_rate.buy != buy or \
            last_rate.sale != sale:
        Rate.objects.create(
            buy=buy,
            sale=sale,
            type=currency_type,
            source=source,
        )


@shared_task
def parse_privatbank():
    from currency.models import Source

    code_name = consts.CODE_NAME_PRIVATBANK
    source = Source.objects.filter(code_name=code_name).last()
    if source is None:
        source = Source.objects.create(code_name=code_name, name='PrivatBank')

    response = requests.get(consts.API_PRIVATBANK_URL)
    response.raise_for_status()
    rates = response.json()
    available_currency_types = {
        'USD': mch.RateTypeChoices.USD,
        'EUR': mch.RateTypeChoices.EUR,
    }

    for rate in rates:
        buy = to_decimal(rate['buy'])
        sale = to_decimal(rate['sale'])
        currency_type = rate['ccy']

        if currency_type not in available_currency_types:
            continue

        add_rates_in_db(currency_type, source, buy, sale)


@shared_task
def parse_monobank():
    from currency.models import Source

    code_name = consts.CODE_NAME_MONOBANK
    source = Source.objects.filter(code_name=code_name).last()
    if source is None:
        source = Source.objects.create(code_name=code_name, name='Monobank')

    response = requests.get(consts.API_MONOBANK_URL)
    response.raise_for_status()
    rates = response.json()
    available_currency_types = {
        '840': mch.RateTypeChoices.USD,
        '978': mch.RateTypeChoices.EUR,
    }
    for rate in rates:
        currency_type = rate['currencyCodeA']
        if currency_type not in available_currency_types:
            continue
        else:
            buy = to_decimal(rate['rateBuy'])
            sale = to_decimal(rate['rateSell'])

        add_rates_in_db(currency_type, source, buy, sale)


@shared_task
def parse_vkurse_dp():
    from currency.models import Source

    code_name = consts.CODE_NAME_VKURSE
    source = Source.objects.filter(code_name=code_name).last()
    if source is None:
        source = Source.objects.create(code_name=code_name, name='vkurse.dp.ua')

    response = requests.get(consts.URL_VKURSE_DP)
    response.raise_for_status()
    rates = response.json()

    # for Dollar
    buy = to_decimal(rates['Dollar']['buy'])
    sale = to_decimal(rates['Dollar']['sale'])
    currency_type = mch.RateTypeChoices.USD

    add_rates_in_db(currency_type, source, buy, sale)

    # for EURO
    buy = to_decimal(rates['Euro']['buy'])
    sale = to_decimal(rates['Euro']['sale'])
    currency_type = mch.RateTypeChoices.EUR

    add_rates_in_db(currency_type, source, buy, sale)


@shared_task
def parse_kredo():
    from currency.models import Source

    code_name = consts.CODE_NAME_KREDO
    source = Source.objects.filter(code_name=code_name).last()
    if source is None:
        source = Source.objects.create(code_name=code_name, name='KredoBank')

    response = requests.get(consts.KREDO_URL)
    source_code = response.text
    soup = BeautifulSoup(source_code)

    table = soup.find('div', {'class': 'l-twotables'})
    body_table = table.find('tbody')

    # for dollars
    only = body_table.find('tr')
    final = only.findAll('td')
    buy = to_decimal(final[2].text)
    sale = to_decimal(final[3].text)
    currency_type = mch.RateTypeChoices.USD

    add_rates_in_db(currency_type, source, buy, sale)

    # for eur
    only = body_table.findAll('tr')
    only_eur = only[1]
    final = only_eur.findAll('td')
    buy = to_decimal(final[2].text)
    sale = to_decimal(final[3].text)
    currency_type = mch.RateTypeChoices.EUR

    add_rates_in_db(currency_type, source, buy, sale)


@shared_task
def parse_kredit_dnepr():
    from currency.models import Source

    code_name = consts.CODE_NAME_KREDIT_DNEPR
    source = Source.objects.filter(code_name=code_name).last()
    if source is None:
        source = Source.objects.create(code_name=code_name, name='CreditDnepr')

    response = requests.get(consts.CREDIT_DNEPR_URL)
    source_code = response.text
    soup = BeautifulSoup(source_code)

    table = soup.find('table', {'class': 'table-s1'})
    body_table = table.find('tbody')

    # for dollars
    only = body_table.find('tr', {'class': 'even'})
    final = only.findAll('td')
    buy = to_decimal(final[1].text)
    sale = to_decimal(final[2].text)
    currency_type = mch.RateTypeChoices.USD

    add_rates_in_db(currency_type, source, buy, sale)

    # for eur
    only = body_table.findAll('tr', {'class': 'odd'})
    only_eur = only[1]
    final = only_eur.findAll('td')
    buy = to_decimal(final[1].text)
    sale = to_decimal(final[2].text)
    currency_type = mch.RateTypeChoices.EUR

    add_rates_in_db(currency_type, source, buy, sale)


@shared_task
def parse_agricole():
    from currency.models import Source

    code_name = consts.CODE_NAME_AGRICOLE
    source = Source.objects.filter(code_name=code_name).last()
    if source is None:
        source = Source.objects.create(code_name=code_name, name='CreditAgricole')

    response = requests.get(consts.AGRICOLE_URL)
    source_code = response.text
    soup = BeautifulSoup(source_code)

    table = soup.find('div', {'class': 'exchange-rates-table'})
    body_table = table.find('tbody')

    # for dollars
    only = body_table.find('tr')
    final = only.findAll('td')
    buy = to_decimal(final[1].text)
    sale = to_decimal(final[2].text)
    currency_type = mch.RateTypeChoices.USD

    add_rates_in_db(currency_type, source, buy, sale)

    # for eur
    only = body_table.findAll('tr')
    only_eur = only[1]
    final = only_eur.findAll('td')
    buy = to_decimal(final[1].text)
    sale = to_decimal(final[2].text)
    currency_type = mch.RateTypeChoices.EUR

    add_rates_in_db(currency_type, source, buy, sale)


@shared_task(
    autoretry_for=(ConnectionError,),
    retry_kwargs={'max_retries': 5},
)
def send_email_in_background(subject, body):
    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [settings.DEFAULT_FROM_EMAIL],
        fail_silently=False,
    )
