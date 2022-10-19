import unittest

from  parameterized import  parameterized

from minterf_mtest.my01_api.mybases_login import MyBases
from minterf_mtest.my01_case.myread_yal import mreads_yml
from my_pytests.case.test_param import get_data


def get_datas():
    get_datas = get_data('login_data.json')
    print(type(get_datas))
    data = []
    data.append((get_datas.get('url'), get_datas.get('customerAccount'),get_datas.get('customerPassword'),get_datas.get('code')))
    return data
def get_yaml():
    dat_log=mreads_yml('mydata.yaml')
    lists = []
    lists.append((dat_log.get('url'), dat_log.get('customerAccount'), dat_log.get('customerPassword'), dat_log.get('code')))
    return  lists

class CaseTest(unittest.TestCase):
    def setUp(self) -> None:
        self.at=MyBases()
    @parameterized.expand(get_yaml())
    def test_login(self,url,name,pwd,result):
        re=self.at.test_login(url,name,pwd)
        self.assertEqual(result,re.json()['code'])
        print(re.text)
