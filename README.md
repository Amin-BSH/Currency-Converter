# Currency Converter Project

The Currency Converter Project is designed to be a practical application leveraging the Python programming language to create a tool that allows users to convert amounts between different currencies. This project utilizes the ExchangeRate-API for fetching real-time exchange rate data and provides an interface for users to specify the amount in one currency and get the equivalent amount in another currency. Additionally, the project features a user-friendly UI using Streamlit, making it accessible for non-technical users to perform currency conversions with ease.


# Project Structure

```
|
|- src
|  |- app.py
|  |- currency_converter.py
|  |- constants.py
|- README.md
|- requirements.txt
```

# Installation

1. make sure you have Python 3.x installed.
2. Install the required dependencies by running:

```bash
pip install -r requirements.txt
```

You need to get an api key from this site ```https://www.exchangerate-api.com/```.

Then go to this ```currency_converter.py``` file then replace your api key in the url variable:

```url = f"your_api_key/{base_currency}"```

# Usage

1. Open a terminal or command prompt.
2. If you are using Linux or WSL or Mac you need to add the src path to the Python path with this command:

```bash
export PYTHONPATH=$PYTHONPATH:$(pwd)
```

> Run this command in the root directory of the project.

3. After installing the requirements you can run the program with this command:

```bash
streamlit run src/app.py
```

It will run the web page at the localhost.