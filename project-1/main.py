import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import mplcyberpunk

tickers = [
    "^BVSP", # IBOVESPA
    "^GSPC", # S&P500
    "BRL=X" # USD
]
dados_mercado = yf.download(tickers, period = "6mo")
print(dados_mercado)
