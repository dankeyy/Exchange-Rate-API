import pytest
from exchange_rates import low_rates

# might change, but that's the mock data at least
expects = ['AED', 'ANG', 'AUD', 'AWG', 'AZN', 'BAM', 'BBD', 'BGN', 'BHD', 'BMD', 'BND', 'BOB', 'BRL', 'BSD', 'BTC', 'BYN', 'BZD', 'CAD', 'CHF', 'CLF', 'CNY', 'CUC', 'DKK', 'EUR', 'FJD', 'FKP', 'GBP', 'GEL', 'GGP', 'GIP', 'GTQ', 'HKD', 'HRK', 'ILS', 'IMP', 'JEP', 'JOD', 'KWD', 'KYD', 'LTL', 'LVL', 'LYD', 'MOP', 'MYR', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PLN', 'QAR', 'RON', 'SAR', 'SBD', 'SGD', 'SHP', 'SVC', 'TMT', 'TND', 'TOP', 'TTD', 'USD', 'WST', 'XAG', 'XAU', 'XCD', 'XDR']

assert low_rates(prod=False) == expects

# idk if that was the intention but it does test it hehe
try:
    assert low_rates(prod=True) == expects
except Exception as e:
    pytest.fail(e)
