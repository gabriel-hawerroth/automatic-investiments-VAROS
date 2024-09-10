import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import mplcyberpunk
import win32com.client as win32

tickers = [
    "^BVSP",  # IBOVESPA
    "^GSPC",  # S&P500
    "BRL=X",  # USD
]

ibov = "IBOVESPA"
sep = "S&P500"
dol = "DOLAR"

dados_mercado = yf.download(tickers, period="6mo")
dados_mercado = dados_mercado["Adj Close"]

dados_mercado = dados_mercado.dropna()

dados_mercado.columns = [dol, ibov, sep]

plt.style.use("cyberpunk")

plt.plot(dados_mercado[ibov])
plt.title(ibov)
plt.savefig("ibovespa.png")

plt.plot(dados_mercado[[dol]])
plt.title(dol)
plt.savefig("dolar.png")

plt.plot(dados_mercado[sep])
plt.title(sep)
plt.savefig("sp500.png")

retornos_diarios = dados_mercado.pct_change()

retorno_dolar = retornos_diarios[dol].iloc[-1]
retorno_ibovespa = retornos_diarios[ibov].iloc[-1]
retorno_sp = retornos_diarios[sep].iloc[-1]

retorno_dolar = str(round(retorno_dolar * 100, 2)) + "%"
retorno_ibovespa = str(round(retorno_ibovespa * 100, 2)) + "%"
retorno_sp = str(round(retorno_sp * 100, 2)) + "%"

outlook = win32.Dispatch("outlook.application")

email = outlook.CreateItem(0)

email.To = "gabrielhawerroth04@gmail.com"
email.Subject = "Relatório de Mercado"
email.Body = f"""Prezado diretor, segue o relatório de mercado:

* O Ibovespa teve o retorno de {retorno_ibovespa}
* O Dólar teve o retorno de {retorno_dolar}
* O S&P500 teve o retorno de {retorno_sp}

Segue em anexo a performance dos ativos nos últimos 6 meses.

Att,
Melhor dev do mundo

"""

anexo_ibovespa = r"C:\Users\Gabriel.Hawerroth\Downloads\project-1-varos\ibovespa.png"
anexo_dolar = r"C:\Users\Gabriel.Hawerroth\Downloads\project-1-varos\dolar.png"
anexo_sp = r"C:\Users\Gabriel.Hawerroth\Downloads\project-1-varos\sp500.png"

email.Attachments.Add(anexo_ibovespa)
email.Attachments.Add(anexo_dolar)
email.Attachments.Add(anexo_sp)

email.Send()
