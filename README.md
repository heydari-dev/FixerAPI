# FixerAPI - Currency Exchange Rate Fetcher  

## Project Description  

**FixerAPI** is a Python package that provides a simple way to fetch real-time exchange rates using the [Fixer.io](https://fixer.io) API. It allows users to retrieve exchange rate data efficiently.  

## Installation  

You can install the package using:  

```bash
pip install git+https://github.com/heydari-dev/RequestDataFromFixer.git
```

Or install it from source:  

```bash
git clone https://github.com/heydari-dev/RequestDataFromFixer.git  
cd RequestDataFromFixer  
pip install .
```

## Usage  

First, import the package and use the `get_data` function to fetch exchange rates:  

```python
from fixer import get_data

api_key = "YOUR_FIXER_IO_API_KEY"
rates = get_data(api_key)

if rates and rates.get("success"):
    print("Exchange Rates:", rates["rates"])
else:
    print("Failed to retrieve exchange rates.")
```

## Features  

- Fetch real-time exchange rates from **Fixer.io**  
- Simple and lightweight implementation  
- Easy integration into Python applications  

## License  

This project is licensed under the **MIT License**.

