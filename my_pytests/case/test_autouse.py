import  pytest
#通过scope设置运行的范围，autouse设置自动运行
@pytest.fixture(scope='class',autouse=True)
def test_fun():
    print('首先执行test_funs')

class Test001(object):
    def test001(self):
        print('001')
        assert  True
    def test002(self):
        print('002')
        assert  False