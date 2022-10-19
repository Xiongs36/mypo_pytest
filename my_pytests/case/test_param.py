import  pytest
def get_data():
    return [('a','bs'),('c','d')]
class Test001(object):
    # #参数化，调用时参数值与parametrize要一致
    # @pytest.mark.parametrize('li',[1,2])
    # def test002(self,li):
    #     assert li==1
   #参数化多个数据 参数名称有，分割
    @pytest.mark.parametrize('test,test1',get_data())
    def test003(self,test,test1):
        print(test,test1)











