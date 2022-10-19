import  pytest
@pytest.fixture()
def test_fun():
    print('首先执行test_funs')

class Test001(object):
    #通过fixture方法名使用
    def test001(self,test_fun):
        print('001')
        assert  True
    def test002(self):
        print('002')
        assert  False