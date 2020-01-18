import http.client
import hashlib
import urllib
import random
import json
import os.path
import pickle

def get_token():
    ''' Get app id and secret key from pickle file 
    
    Returns:
        token: {'appid', 'screte_key'}
    '''
    token = None
    token_path = os.path.join(os.path.dirname(__file__), '../token.pickle')

    if os.path.exists(token_path):
        with open(token_path, 'rb') as f:
            token = pickle.load(f)
    if token is None:
        appid = input('Please input your app id: ')
        secret_key = input('Please input your secret key: ')
        token = {'appid': appid, 'key': secret_key}
        with open(token_path, 'wb') as f:
            pickle.dump(token, f)

    return token


def trans(src: str,
          from_lang: str = 'auto',
          to_lang: str = 'zh'):
    ''' Do translation 
    
    Args:
        src: The sentence to be translated
        from_lang: The original language type
        to_lang: Target language type
    '''
    httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
    myurl = '/api/trans/vip/translate'

    token = get_token()

    salt = random.randint(32768, 65536)
    sign = token['appid'] + src + str(salt) + token['key']
    sign = hashlib.md5(sign.encode()).hexdigest()
    myurl = (f'{myurl}'
             f'?appid={token["appid"]}'
             f'&q={urllib.parse.quote(src)}'
             f'&from={from_lang}'
             f'&to={to_lang}'
             f'&salt={str(salt)}'
             f'&sign={sign}') 

    try:
        httpClient.request('GET', myurl)

        response = httpClient.getresponse()
        result_all = response.read().decode("utf-8")
        result = json.loads(result_all)['trans_result'][0]['dst']

        print (result)

    except Exception as e:
        print (e)
    finally:
        if httpClient:
            httpClient.close()


if __name__ == '__main__':
    trans('test')






