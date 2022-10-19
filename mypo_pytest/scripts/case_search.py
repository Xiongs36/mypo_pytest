import os,sys

from mypo_pytest.Page.page_search import PageSearch
from mypo_pytest.Page.page_union import PageUinon

sys.path.append(os.getcwd())
# from mypo_pytest.Page.page_search import PageSearch
from mypo_pytest.scripts.init_webdriver import InitWebdriver
import pytest

class CaseSearch():
    def setup_class(self):
        self.driver = InitWebdriver().init_driver()
        #self.pu=PageSearch(self.driver)
        self.pu=PageUinon().union_page_serch(self.driver)
    def teardown_class(self):
        self.pu.page_click_return()
        self.driver.quit()
    #设置-搜索
    @pytest.mark.parametrize('test',['va','test1'])
    def test_serch(self,test):
        self.pu.page_click_set()
        self.pu.page_input_keys(test)


