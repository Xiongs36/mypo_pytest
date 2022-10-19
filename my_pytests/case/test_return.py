import  pytest
@pytest.fixture(params=[1,2,3])
def test_fun(request):
    return  request.param

class Test001(object):
    #需要用返回值，必须传入fixture函数
    def test001(self,test_fun):
        assert  test_fun==4
    #@pytest.mark.skip('跳过')
    #@pytest.mark.skipif(2<1,reason="版本问题")
    @pytest.mark.xfail(2>1,reason='标记失败')
    def test002(self,fist):
        assert 'c'==fist


