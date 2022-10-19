import  pytest
@pytest.fixture(params=['a','b'])
#此模块最最优先执行，不管设置与否
def fist(request):
    return request.param