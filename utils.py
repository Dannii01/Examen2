import requests


def get_last_price(ticker: str) -> float:
    """
    Esta funcion busca usando la API de yahoo finance el ultimo precio disponible del instrumento cuyo ticker es 'ticker'.
    @:param ticker: ticker de la empresa a consultar
    """

    cnbc_url = f"https://quote.cnbc.com/quote-html-webservice/restQuote/symbolType/symbol?symbols={ticker}"
    headers = {'User-agent': 'Mozilla/5.0'}
    r = requests.get(url=cnbc_url, headers=headers)
    price = r.json().get('FormattedQuoteResult').get('FormattedQuote')[0].get('last')

    return price
