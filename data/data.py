from HuobiDMService import HuobiDM
from pprint import pprint
import pandas as pd
import time
#### input huobi dm url
URL = 'https://api.hbdm.com'

####  input your access_key and secret_key below:
ACCESS_KEY = 'f65d11ed-36c9546b-ghxertfvbf-a3941'
SECRET_KEY = 'b6e59f8b-89b2d764-8c2950ce-22965'


dm = HuobiDM(URL, ACCESS_KEY, SECRET_KEY)

#print (u' 获取K线数据 ')
#pprint (dm.get_contract_kline(symbol='BTC_CQ', period='60min', size=750))

def get_data(name='BTC_CQ'):

    BTC = dm.get_contract_kline(symbol=name, period='60min', size=750)
    df = pd.DataFrame(BTC['data'][182:537])
    df['date'] = df['id']
    df['date'] = df['date'].apply(lambda x:time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(x)))
    df.to_csv(name+'.csv')

get_data('BTC_CQ')
get_data('XRP_CQ')
get_data('LTC_CQ')
