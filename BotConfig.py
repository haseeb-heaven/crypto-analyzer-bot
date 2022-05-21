"""
Info: Binance Market Analyzer Bot Config
Bot Type: Market Analyzer
Author: Haseeb Mir.
Date: 17/05/2022
"""

#Bot Configurations.

# Bot init variables.
bot_running = True
bot_alert_type = "message" #"voice" or "message"
    
#Authentication section.

#Binance Auth.
api_key = "" #Binance API Key here.
secret_key = "" #Binance Secret Key here.#

#Twilio Auth.
account_sid = "" #Twilio Account SID here.
auth_token = "" #Twilio Auth token here.
from_contact = "" #Twilio From Contact here.
to_contact = "" #Twilio To Contact here.

#Symbol to trade.
_quote_curr:str = "LUNA" #Symbol select.
_base_curr:str = "BUSD" #Currency select.

candle_timestamps = ['1m','3m','5m','15m','30m'] #Candle timestamps.
candle_max_pnls = [4,4,5,5,5] #Candle PNLS in $.
candle_timestamp_inc:int = 2 #Next cancdle size.
candle_min_pnl:float = 0 #Min profit in candle.
candle_max_pnl:float = 0 #Max profit in candle.
candle_const_pnl:float = 10 #Constant profit

candle_timestamp = candle_timestamps[3] #5 Min candle timestamp.

#DONT EDIT THIS.
symbol = _quote_curr + '/' + _base_curr