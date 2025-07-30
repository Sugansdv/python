def get_historical_rates(from_currency, to_currency):
    mock_history = {
        "2025-07-27": 83.2,
        "2025-07-28": 83.4,
        "2025-07-29": 83.6
    }
    for date, rate in mock_history.items():
        yield (date, rate)
