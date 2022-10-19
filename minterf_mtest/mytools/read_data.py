import json
import os


def get_data(filename):
    filename='/CloudMusic/interf_test/data/'+filename
    with open(filename) as f:
        files= json.load(f)
        return  files
# print(get_data('login_data.json'))
# print(os.getcwd())
get_datas=get_data('login_data.json')
print(get_datas)
account='customerAccount'
pwd='customerPassword'
data=[]
data.append((get_datas.get('url'),get_datas.get(account),get_datas.get(pwd)))
print(data)