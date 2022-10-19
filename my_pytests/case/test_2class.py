import  pytest
@pytest.fixture()
def login():
    print('首先执行test_fun')
#通过类方法调用，传入fixture函数名称
@pytest.mark.usefixtures('login')
class Test001(object):
    def test001(self):
        print('001')
        assert  True
    def test002(self):
        print('002')
        assert  False