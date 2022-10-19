
import  requests
class MyBases():
    def test_login(self,url,customerAccount,customerPassword,headers={'content-type':'application/json'}):
        data={"customerAccount":customerAccount,"customerPassword":customerPassword}
        res=requests.post(url,json=data,headers=headers)
        return  res

# url='https://s2b.wanmi.com/pcbff/login?reqId=e86abe11-de71-45a8-a646-a486dea78cfc'
# data={"customerAccount": "MTg3MTg1MjkzOTc=", "customerPassword": "eGlvbmdzMzY="}
# a=ApiTest()
# data=a.test_login(url,'MTg3MTg1MjkzOTc=','eGlvbmdzMzY=')
# print(data.text)