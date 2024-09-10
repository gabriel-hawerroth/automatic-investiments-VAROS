import yfinance as yf

tickers = [
    "^BVSP",  # IBOVESPA
    "^GSPC",  # S&P500
    "BRL=X",  # USD
]
dados_mercado = yf.download(tickers, period="6mo")
print(dados_mercado)
