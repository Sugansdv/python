from core.decorators import cache_rates
from utils.api import fetch_live_rates
from core.history import get_historical_rates

class CurrencyConverter:
    def __init__(self):
        self.rates = self.load_rates()

    @cache_rates
    def load_rates(self):
        return fetch_live_rates()

    def convert(self, from_currency, to_currency, amount):
        try:
            if from_currency not in self.rates or to_currency not in self.rates:
                raise ValueError("Unsupported currency")
            base_amount = amount / self.rates[from_currency]
            return base_amount * self.rates[to_currency]
        except Exception as e:
            print("Error:", e)
            return 0

    def get_supported_currencies(self):
        return list(self.rates.keys())

    def historical_rates(self, from_currency, to_currency):
        return get_historical_rates(from_currency, to_currency)
