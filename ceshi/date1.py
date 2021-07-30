from urllib.parse import urljoin
import requests
import pytest
import time
from utils.yaml_operation import yamlopertion



class Testlogin:
    send = yamlopertion.read_yaml("self", "../cp/api.yaml", "testlogin")
    login_in = yamlopertion.read_yaml("self", "../cp/api.yaml", "login_in")
    base_url = "http://47.241.102.180:8089"

    @pytest.mark.parametrize('send', send)
    def test_sendcode(self,send):
        url = urljoin(self.base_url, "/api/user/email/sendcode?")
        data = {'email': send['email']
                }
        re = requests.post(url, data=data).json()
        aa = re['code']
        if aa == 200005:
            print('上限了')
        elif aa == 200008:
            print('两分钟内')
        else:
            print('成了')


    @pytest.mark.parametrize('login_in', login_in)
    def test_login(self,login_in):
        url = urljoin(self.base_url, "/api/user/loginByEmail?")
        data1 = {'email': login_in['email'],
                 'code':login_in['code']}
        re = requests.post(url , data=data1).json()
        aa = re['code']
        if aa == 300016:
            print('过期了')
        else:
            print('成了')

        print(re)
        token = aa['data']['token']
        print(token)
        return token



