"""
Info: Binance Market Analyzer Bot
Bot Type: Market Analyzer
Author: Haseeb Mir.
Date: 17/05/2022
"""
# %%
# Imports.
import sys
from datetime import datetime
import ccxt
import pyttsx3
from twilio.rest import Client
import BotConfig as cfg


# Globals:
symbol = cfg.SYMBOL
voice_engine = None
twilio_client,exchange = None,None

# %%
# Connect binance
def init_binance(api_key:str,secret_key:str,rate_limit:bool=True,verbose_mode:bool=False):
    exchange_id = 'binance'
    exchange_class = getattr(ccxt, exchange_id)
    exchange = ccxt.binance({
        'apiKey': api_key,
        'secret': secret_key,
        'enableRateLimit': rate_limit,
        "options": {"options": {"adjustForTimeDifference": True}},
    })
    exchange.nonce = lambda: exchange.milliseconds() - 1000
    exchange.load_markets()
    exchange.verbose = verbose_mode  # enable verbose mode after loading the markets
    return exchange

# %%
# Connect Twilio
def init_twilio(account_sid:str,auth_token:str):
    try:
        client = Client(account_sid, auth_token)
        return client
    except Exception as ex:
        print("Exception in Twilio : " + str(ex))

# Init Voice engine, voice_idx = 0 - N (No. of Voices support by your system) [0-Male,1-Female].
def init_voice_engine(voice_idx:int=0) -> None:
    try:
        voice_engine = pyttsx3.init()
        voices = voice_engine.getProperty('voices')
        voice_id = voices[voice_idx].id
        voice_engine.setProperty('voice',voice_id)
    except Exception as ex:
        print("Exception in Voice Engine: " + str(ex))
        

# Print format.
def printf(format, *args):
    sys.stdout.write(format % args)

# Get Wallet balance from Binance.
def get_wallet_balance():
    balances = exchange.fetch_balance()
    wallet_balance = ""
    for balance in balances['info']['balances']:
        if float(balance['free']) > 0:
            wallet_balance += "" + \
                balance['asset'] + ": " + balance['free'] + '\n'
    return wallet_balance


def percentage_diff(previous, current) -> float:
    try:
        percentage = abs(previous - current)/((previous + current)/2) * 100
    except ZeroDivisionError:
        percentage = float('inf')
    return percentage

# Get Candle data from Binance.
def get_candle_data(market_price: float, candle_low: float, candle_high: float):
    candle_pnl = abs(candle_high-candle_low)
    candle_low_optimal = percentage_diff(market_price, candle_low)
    candle_high_optimal = percentage_diff(market_price, candle_high)
    return candle_pnl, candle_low_optimal, candle_high_optimal

# Send Whatsapp notification.
def whatsapp_send(contact_no: str, message: str):
    message = twilio_client.messages.create(body=message, from_='whatsapp:'+cfg.FROM_CONTACT, to='whatsapp:'+contact_no)
    print(message.sid)

def bot_alert(message:str):
    if cfg.BOT_ALERT_TYPE == "voice":
        voice_engine.say(message)
        voice_engine.runAndWait()
        
    elif cfg.BOT_ALERT_TYPE == "message":
        whatsapp_send(cfg.TO_CONTACT,message)
        
# Main Function.
if __name__ == '__main__':

    try:
        # Binance Account init.
        exchange = init_binance(cfg.API_KEY,cfg.SECRET_KEY)
        
        if cfg.BOT_ALERT_TYPE == "voice":
            init_voice_engine()
            
        # Twilio Account init.
        if cfg.BOT_ALERT_TYPE == "message":
            twilio_client = init_twilio(cfg.ACCOUNT_SID,cfg.AUTH_TOKEN)

        # Print BOT Tag.
        date_now = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        print("BOT Started at Date " + date_now)

        while cfg.BOT_RUNNING:
            
                # Print Balance (Requires API Key).
                #print("Starting Balance: ",get_wallet_balance())

                # Get current market price.
                ohlcv = exchange.fetch_ohlcv(symbol, cfg.candle_timestamps[0], limit=1) #Get current price for 1m candle.
                ohlcv_candle = exchange.fetch_ohlcv(symbol,cfg.CANDLE_TIMESTAMP,limit=1)

                # Get Candle data.
                market_price = ohlcv[0][4]
                candle_high = ohlcv_candle[0][2]
                candle_low = ohlcv_candle[0][3]

                printf(symbol + ": '%.10f' High: '%.10f' Low: '%.10f'\n",market_price, candle_high, candle_low)

                if market_price <= candle_low:
                    bot_alert(symbol + " Low,Price $" + str(market_price))

                if market_price >= candle_high:
                    bot_alert(symbol + " High,Price $" + str(market_price))

    except Exception as ex:
        print("Exception occurred: " + str(ex))