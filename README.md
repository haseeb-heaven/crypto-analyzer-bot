# Market-Analyzer-Bot
This bot analyze crypto market using Binance for token and alert using Voice or WhatsApp message.
Here we are using [CCXT CryptoCurrency eXchange Trading Library]( https://github.com/ccxt/ccxt) for connecting to the Binance server and sending alert using Speech to text libraries and WhatsApp API using Twilio API.

## Prerequisite.
- Python 3.0: Get [Python 3.0](https://www.python.org/downloads/) and setup in your machine.
- Binance Account: [Click here to register](https://accounts.binance.com/en/register).
- Twilio Account: [Click here to register](https://www.twilio.com/try-twilio).
- Twilio WhatsApp API: You need to configure Sandbox API for WhatsApp [from here](https://www.twilio.com/docs/whatsapp/sandbox) and after configuring them you can recieve and send messages from their API.
- [CCXT CryptoCurrency eXchange Trading Library]( https://github.com/ccxt/ccxt) : Or use `pip install ccxt`
- Pyttsx3 Python speech-to-text library: use `pip install pyttsx3`.

**NOTE:** This **BOT** and **VIDEO** is for **Educational Purpose** only and learning how to integrate _Binance_ and other API's like _Twilio_.

## Bot Config.
In order to run bot you need to configure it as per your requirements.</br>
Go to file `BotConfig.py` and change parameters as per required.</br>
### Bot Authentication:
**Binance** Authentication change following line:</br>
`api_key = "" #Binance API Key here.`</br>
`secret_key = "" #Binance Secret Key here.#`</br></br>
**Twilio** Authentication change following line:</br>
`account_sid = "" #Twilio Account SID here.`</br>
`auth_token = "" #Twilio Auth token here.`</br>
`from_contact = "" #Twilio From Contact here.`</br>
`to_contact = "" #Twilio To Contact here.`</br>

### Bot TOKEN:
To set your token change following line:</br>
`_quote_curr:str = "LUNA" #Symbol select.`</br>
`_base_curr:str = "BUSD" #Currency select.`</br>

### Bot Alert type:
To Change bot alert type to 'Voice' or 'Text Message' change following line:</br>
`bot_alert_type = "voice"` or `bot_alert_type = "message"`</br>

### Bot Candle Timestamp:
To Change candle timestamps change following line:</br>
`candle_timestamp = candle_timestamps[1] #For 3 Min candle timestamp.`</br>

## BOT Features.
- Market Analyzer: Bot analyze the market in certain candle sticks which is customisable and efficient.</br>
- Alert Type: Bot alert using Voice and Text messages mode.</br>
- API Integration: CCXT is very fast and reliable library for Binance and other cyrpto exchanges.</br>
- Cyprto Exchanges : All of the crypto exchanges supported by ccxt.</br>
- Easy Config : Bot is easy to configure and customisable for other exchanges using ccxt.</br>

# Bot Demo on YouTube :
[![BOT Demo](https://img.youtube.com/vi/n1g-XPzOPOI/0.jpg)](https://www.youtube.com/watch?v=n1g-XPzOPOI)

written and maintained by Haseeb Mir (haseebmir.hm@gmail.com)
