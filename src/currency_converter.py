import requests
from cachetools import cached, TTLCache
from typing import Optional

cache = TTLCache(maxsize=100, ttl=3 * 60 * 60)

@cached(cache)
def get_exchange_rate(base_currency: str, target_currency: str) -> Optional[float]:
    """
    Retrieve the exchange rate between two currencies from an external API.

    Args:
        base_currency (str): The currency from which to convert.
        target_currency (str): The currency to which to convert.

    Returns:
        Optional[float]: The exchange rate from base_currency to target_currency,
        or None if the request fails or the currency is not found.
    """
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()["conversion_rates"].get(target_currency)

def convert_currency(amount: float, exchange_rate: float) -> float:
    """
    Convert an amount of currency using the provided exchange rate.

    Args:
        amount (float): The amount of currency to convert.
        exchange_rate (float): The exchange rate to use for conversion.

    Returns:
        float: The converted amount in the target currency.
    """
    return amount * exchange_rate

if "__main__" == __name__:
    base_currency = input("Enter your base currency: ").upper()
    target_currency = input("Enter your target currency: ").upper()
    amount = float(input("Enter your amount: "))  # Changed to float for currency precision
    exchange_rate = get_exchange_rate(base_currency=base_currency, target_currency=target_currency)

    if exchange_rate is not None:
        converted_currency = convert_currency(amount=amount, exchange_rate=exchange_rate)
        print(f"{amount} {base_currency} is {converted_currency} {target_currency}")
    else:
        print("Exchange rate could not be retrieved.")
