import pytest
import  os,sys
import requests
sys.path.append(os.getcwd())
from minterf_mtest.my01_case.myread_yal import mreads_yml



class MyBases():
    def test_login(self,url,customerAccount,customerPassword,headers={'content-type':'application/json'}):
        data={"customerAccount":customerAccount,"customerPassword":customerPassword}
        res= requests.post(url, json=data, headers=headers)
        return  res

def get_yaml():
    dat_log=mreads_yml('mydata.yaml')
    lists = []
    lists.append((dat_log.get('url'), dat_log.get('customerAccount'), dat_log.get('customerPassword')))
    return  lists

class CaseTest():
    def setup_class(self) -> None:
        self.at=MyBases()
    @pytest.mark.parametrize('url,name,pwd',get_yaml())
    def test_login(self,url,name,pwd):
        re=self.at.test_login(url,name,pwd)
        print(re.text)
if __name__ == '__main__':
    pytest.main(['-s','case_pytest.py'])