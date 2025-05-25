# Transitioning from OneTick to KX products: A Series of Use Cases

**Alpaca Trading API Documentation (Required in case you want to download market data)**

Historical trades (single symbol): [Stock Trades](https://docs.alpaca.markets/reference/stocktradesingle-1)  
Historical quotes (single symbol): [Stock Quotes](https://docs.alpaca.markets/reference/stockquotesingle-1)

Base URL for trades: https://data.alpaca.markets/v2/stocks/{symbol}/trades  
Base URL for quotes: https://data.alpaca.markets/v2/stocks/{symbol}/quotes

**KX Documentation**

Database and Programming Language: [kdb+ and q](https://code.kx.com/q)

Python interface library: [PyKX](https://code.kx.com/pykx)

**OneTick Documentation**  

As Of (Prevailing): [As Of Join](https://sql.docs.sol.onetick.com/asof.html)  

**Environment Setup**

Create Virtual Environment: `python -m venv .venv`

Activate Virtual Environment: `source .venv/bin/activate`

Install Libraries: `pip install requests pykx matplotlib`  