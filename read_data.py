import yaml, os
from base.read_yaml_data import read_yaml_data


# {'test_login_001': {'username': '13488834010', 'password': '159357li'}, 'test_login_006': {'username': '13488834010 ', 'password': '9998888'}, 'test_login_003': {'username': '13488834010 ', 'password': '159357li'}, 'test_login_002': {'username': ' 13488834010', 'password': '159357li'}, 'test_login_010': {'username': '中国', 'password': '9998888'}}
# [('13488834010','159357li'),(' 13488834010','159357li'),]

data_list = []
data = read_yaml_data("login_data.yaml")
# print(data)
for i in data.keys():
    data2 = data.get(i)
    name = data2.get("username")
    passwd = data2.get("password")
    data_list.append((name,passwd))

print(data_list)


