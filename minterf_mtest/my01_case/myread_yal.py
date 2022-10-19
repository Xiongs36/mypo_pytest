
import  yaml

def mreads_yml(pathname):
    pathname = '/CloudMusic/minterf_mtest/datap/'+pathname
    with open(pathname) as f:
        data = yaml.safe_load(f)
        dat_log = data.get('login')
        return dat_log
        # lists = []
        # lists.append((dat_log.get('url'), dat_log.get('customerAccount'), dat_log.get('customerPassword'), dat_log.get('code')))


#写入中文需设置encodin，allow_unicode=True
# data={"logoin":{"test1":{"name":'熊','age':32}}}
# with open('../data/data.yaml','w') as f:
#     data=yaml.safe_dump(data,f,encoding='utf-8',allow_unicode=True)
# print(reads_yaml('data.yaml'))