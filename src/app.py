import streamlit as st
from src.constants import CURRENCIES
from currency_converter import convert_currency, get_exchange_rate
from typing import Optional


st.title(":dollar: Currency Converter")

st.write(
    "**This tool allows you to instantly convert amounts between different currencies 🌍. Enter the amount and choose the currencies to see the result.**"
)

base_currency: str = st.selectbox("From currency (Base):", CURRENCIES)
target_currency: str = st.selectbox("To currency (Target):", CURRENCIES)

amount: float = st.number_input(
    "Enter the amount:",
    min_value=0.0,
)

if amount != 0 and base_currency and target_currency:
    exchange_rate: Optional[float] = get_exchange_rate(
        base_currency=base_currency, target_currency=target_currency
    )

    if exchange_rate:
        converted_currency: float = convert_currency(
            amount=amount, exchange_rate=exchange_rate
        )
        st.success(f"✅ Exchange Rate: {exchange_rate:.4f}")
        col1, col2, col3 = st.columns(3)
        col1.metric(label="Base Currency", value=f"{amount:.2f} {base_currency}")
        col2.markdown(
            "<h1 style='text-align: center; margin: 0; color: green;'>&#8594;</h1>",
            unsafe_allow_html=True,
        )
        col3.metric(
            label="Target Currency", value=f"{converted_currency:.2f} {target_currency}"
        )
    else:
        st.error("Error fetching exchange rate.")

st.markdown("---")
st.markdown("### ❕ About This Tool")
st.markdown(
    """
This currency converter uses real-time exchange rates provided by the ExchangeRate-API.
- The conversion updates automatically as you input the amount or change the currency.
- Enjoy seamless currency conversion without the need to press a button!
"""
)
