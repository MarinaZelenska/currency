from unittest.mock import MagicMock

from currency.models import Rate
from currency.tasks import parse_monobank, parse_privatbank, parse_vkurse_dp


def test_parse_privatbank(mocker):
    privatbank_response = [
        {"ccy": "USD", "base_ccy": "UAH", "buy": "26.90000", "sale": "27.39726"},
        {"ccy": "EUR", "base_ccy": "UAH", "buy": "30.50000", "sale": "30.95975"},
        {"ccy": "RUR", "base_ccy": "UAH", "buy": "0.35600", "sale": "0.38600"},
        {"ccy": "BTC", "base_ccy": "USD", "buy": "45814.5781", "sale": "50637.1653"},
    ]
    requests_get_mock = mocker.patch(
        'requests.get',
        return_value=MagicMock(json=lambda: privatbank_response),
    )

    initial_rate_count = Rate.objects.count()
    parse_privatbank()
    assert Rate.objects.count() == initial_rate_count + 2
    assert requests_get_mock.call_count == 1
    assert requests_get_mock.call_args_list[0][0][0] == 'https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11'  # noqa: E501
    parse_privatbank()
    assert Rate.objects.count() == initial_rate_count + 2
    assert requests_get_mock.call_count == 2


def test_parse_monobank(mocker):
    monobank_response = [
        {"currencyCodeA": 840, "currencyCodeB": 980, "date": 1641373807, "rateBuy": 27.35, "rateSell": 27.53},
        {"currencyCodeA": 978, "currencyCodeB": 980, "date": 1641373807, "rateBuy": 30.75, "rateSell": 31.0405}, ]
    requests_get_mock = mocker.patch(
        'requests.get',
        return_value=MagicMock(json=lambda: monobank_response),
    )

    initial_rate_count = Rate.objects.count()
    parse_monobank()
    assert Rate.objects.count() == initial_rate_count + 2
    assert requests_get_mock.call_count == 1
    parse_monobank()
    assert Rate.objects.count() == initial_rate_count + 2
    assert requests_get_mock.call_count == 2


def test_parse_vkurse_dp(mocker):
    vkurse_dp_response = {
        "Dollar": {"buy": "27.40", "sale": "27.60"},
        "Euro": {"buy": "30.85", "sale": "31.00"},
        "Rub": {"buy": "0.358", "sale": "0.364"}}
    requests_get_mock = mocker.patch(
        'requests.get',
        return_value=MagicMock(json=lambda: vkurse_dp_response),
    )

    initial_rate_count = Rate.objects.count()
    parse_vkurse_dp()
    assert Rate.objects.count() == initial_rate_count + 2
    assert requests_get_mock.call_count == 1
    assert requests_get_mock.call_args_list[0][0][0] == 'http://vkurse.dp.ua/course.json'
    parse_vkurse_dp()
    assert Rate.objects.count() == initial_rate_count + 2
    assert requests_get_mock.call_count == 2
