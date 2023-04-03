import requests
from twilio.rest import Client

ticker = 'PLTR'
company_name = 'Palantir Technologies'
# For Alpha Vantage API
api_key = 'W553QA4RJ640XE8M'
# For News API
api_key_news = '564edbd6f4824320a04a85ae4e09401b'

url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={ticker}&apikey={api_key}'
r = requests.get(url)
data = r.json()["Time Series (Daily)"]
data_list = [value for key, value in data.items()]
last_trading_day_open = float(data_list[0]['1. open'])
last_trading_day_close = float(data_list[0]['4. close'])
previous_trading_day_close = float(data_list[1]['4. close'])
change = round((last_trading_day_close / previous_trading_day_close - 1) * 100, 3)

news_url = f'https://newsapi.org/v2/everything?q={company_name}&apiKey={api_key_news}'
news_response = requests.get(news_url)
articles = news_response.json()["articles"]
top_3_headlines = [e['title'] for e in articles[0:3]]

# for e in articles[0:3]:
#     a = e['title']
#     top_3_headlines.append(a)

account_sid = 'ACc4571e376dbaa8f0bec5b49be097280a'
auth_token = '667c423de63177af70baf22eba7a9ab4'
api_key = 'd78e49069b5aa160258b447776f9ac60'
client = Client(account_sid, auth_token)
message = client.messages \
    .create(
    body = f'{company_name} closed at {last_trading_day_close}',
    from_='+19896747379',
    to='+61459886112'
)
print(top_3_headlines)
